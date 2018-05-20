from collections import deque
import re
from regy.samples.mapper.meta_characters import meta_characters
from regy.samples.mapper.repeat_helper import repeat_info_to_regex
from regy.samples.models.match_anything_info import MatchAnythingInfo
from regy.samples.tokens.case_state import CaseSensitive
from regy.samples.tokens.match_anything import MatchAnything, basic_char_to_re, can_span_across_lines


class MapMatchAnything:

    def __init__(self, info: MatchAnythingInfo, target_lang, case_state):
        self._info = info
        self._target_lang = target_lang
        self._case_state = case_state
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        enclose_in_brackets = True
        case_does_apply = False
        letter_re = re.compile(r'[A-Za-z]')

        if self._info.specific_characters is not None:
            chars = self._escape_special_characters(self._info.specific_characters)
            self._re.append(chars)
            if self._info.can_span_across_lines:
                self._re.appendleft(can_span_across_lines[self._target_lang])

            case_does_apply = letter_re.match(chars) is not None
        elif self._info.specific_character is not None:
            char = self._escape_special_characters(self._info.specific_character)
            self._re.append(char)
            if self._info.can_span_across_lines:
                self._re.appendleft(can_span_across_lines[self._target_lang])

            case_does_apply = letter_re.match(char) is not None
        elif self._info.nothing is not None:
            if self._info.can_span_across_lines:
                self._re.append(can_span_across_lines[self._target_lang])
            else:
                self._re.append('.')
                enclose_in_brackets = False
        elif self._info.basic_characters is not None:
            if len(self._info.basic_characters) == 0 and not self._info.can_span_across_lines:
                self._re.append('.')
                enclose_in_brackets = False

            case_does_apply = MatchAnything.LOWER_CASE_LETTERS in self._info.basic_characters \
                              or MatchAnything.UPPER_CASE_LETTERS in self._info.basic_characters

            basic_to_re = basic_char_to_re[self._target_lang]
            self._re.append(''.join([basic_to_re[i] for i in self._info.basic_characters]))
            if self._info.can_span_across_lines and MatchAnything.LINE_BREAKS not in self._info.basic_characters:
                self._re.append(can_span_across_lines[self._target_lang])

        if enclose_in_brackets:
            self._re.append(']')
            self._re.appendleft('[^')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        if case_does_apply:
            self._add_case_state()

    def _add_case_state(self):
        case_insensitive = self._info.case_insensitive

        if case_insensitive:
            if not self._case_state['case'] == CaseSensitive.OFF:
                self._re.appendleft('(?i)')
                self._case_state['case'] = CaseSensitive.OFF
                self._case_state['hasChanged'] = True
        else:
            if self._case_state['hasChanged']:
                self._re.appendleft('(?-i)')
                self._case_state['case'] = CaseSensitive.ON

            self._case_state['canUseCaseInsensitiveFlag'] = False


    def _escape_special_characters(self, string):
        meta_chars = meta_characters[self._target_lang]
        return ''.join([meta_chars[c] if c in meta_chars else c for c in string])
