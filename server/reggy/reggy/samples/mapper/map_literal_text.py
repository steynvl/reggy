from collections import deque
import re
from reggy.samples.constants.meta_characters import meta_characters
from reggy.samples.mapper.repeat_helper import repeat_info_to_regex
from reggy.samples.models.literal_text_info import LiteralTextInfo
from reggy.samples.tokens import LiteralTextTok
from reggy.samples.tokens.case_state import CaseSensitive
from reggy.samples.tokens.repetition import Repetition
from reggy.samples.utils.factorizer import Factorizer


class MapLiteralText:

    def __init__(self, info: LiteralTextInfo, target_lang, case_state):
        self._info = info
        self._target_lang = target_lang
        self._case_state = case_state
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        extra_info = self._info.extra_info
        escaped_strings = self._escape_special_characters(self._info.literal_text)

        if len(escaped_strings) == 1:
            esc_string = escaped_strings[0]
            if len(esc_string) > 1 and esc_string[0] != '\\' and self._info.repetition_info.repeat_info != Repetition.ONE:
                if LiteralTextTok.MATCH_ALL_EXCEPT_SPECIFIED in extra_info:
                    self._re.extend(['(?!', esc_string, ')'])
                else:
                    self._re.extend(['(?:', esc_string, ')'])
            else:
                if LiteralTextTok.MATCH_ALL_EXCEPT_SPECIFIED in extra_info:
                    self._re.append('(?!{})'.format(esc_string))
                else:
                    self._re.append(esc_string)
        else:
            factorized_re = Factorizer(escaped_strings).get_re()
            if LiteralTextTok.MATCH_ALL_EXCEPT_SPECIFIED in extra_info:
                self._re.append('(?!{})'.format(factorized_re))
            else:
                self._re.append(factorized_re)

        if LiteralTextTok.MATCH_ALL_EXCEPT_SPECIFIED in extra_info:
            self._re.append('.')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        self._add_case_state(escaped_strings)

    def _add_case_state(self, escaped_strings):
        if LiteralTextTok.CASE_INSENSITIVE in self._info.extra_info:
            if not self._case_state['case'] == CaseSensitive.OFF:
                self._re.appendleft('(?i)')
                self._case_state['case'] = CaseSensitive.OFF
                self._case_state['hasChanged'] = True
        else:
            if self._case_state['hasChanged']:
                self._re.appendleft('(?-i)')
                self._case_state['case'] = CaseSensitive.ON

            if self._does_contain_letters(escaped_strings):
                self._case_state['canUseCaseInsensitiveFlag'] = False

    def _escape_special_characters(self, strings):
        meta_chars = meta_characters[self._target_lang]

        return [
            ''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in strings
        ]

    @staticmethod
    def _does_contain_letters(escaped_strings):
        letters_re = re.compile(r'[A-Za-z]')
        return any([letters_re.match(i) for i in escaped_strings])
