from collections import deque
import re

from reggy.samples.constants.basic_characters import basic_characters_to_re
from reggy.samples.constants.meta_characters import meta_characters
from reggy.samples.mapper.repeat_helper import repeat_info_to_regex
from reggy.samples.models.basic_characters_info import BasicCharactersInfo
from reggy.samples.tokens.basic_characters_tok import BasicCharactersTok
from reggy.samples.tokens.case_state import CaseSensitive


class MapBasicCharacters:

    def __init__(self, info: BasicCharactersInfo, target_lang, case_state):
        self._info = info
        self._target_lang = target_lang
        self._case_state = case_state
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        found = 0

        basic_char_to_re = basic_characters_to_re[self._target_lang]
        if self._info.upper_case_letters:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.UPPER_CASE_LETTERS])
        if self._info.lower_case_letters:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.LOWER_CASE_LETTERS])
        if self._info.digits:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.DIGITS])
        if self._info.punctuation_and_symbols:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.PUNCTUATION_AND_SYMBOLS])
        if self._info.white_space:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.WHITE_SPACE])
        if self._info.line_breaks:
            found += 1
            self._re.append(basic_char_to_re[BasicCharactersTok.LINE_BREAKS])
        
        individual_chars = self._info.individual_chars
        
        found += len(individual_chars)

        self._re.append(self._escape_special_characters(individual_chars))

        enclose = False
        if self._info.match_all_except_specified:
            self._re.appendleft(basic_char_to_re[BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED])
            enclose = True
        elif found == 1 and (self._info.upper_case_letters or self._info.line_breaks
                                or self._info.lower_case_letters):
            enclose = True
        elif found > 1:
            enclose = True

        if enclose:
            self._re.appendleft('[')
            self._re.append(']')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        self._add_case_state()

    def _add_case_state(self):
        case_insensitive = self._info.case_insensitive

        does_apply = self._info.upper_case_letters or self._info.lower_case_letters \
                     or re.match(r'[a-zA-Z]', self._info.individual_chars) is not None

        if does_apply:
            if case_insensitive:
                if not self._case_state['case'] == CaseSensitive.OFF:
                    self._re.appendleft('(?i)')
                    self._case_state['case'] = CaseSensitive.OFF
                    self._case_state['hasChanged'] = True
            else:
                if self._case_state['hasChanged']:
                    self._re.appendleft('(?-i)')
                    self._case_state['case'] = CaseSensitive.ON

        if does_apply and not case_insensitive:
            self._case_state['canUseCaseInsensitiveFlag'] = False

    def _escape_special_characters(self, individual_chars):
        meta_chars = meta_characters[self._target_lang]
        return ''.join([meta_chars[c] if c in meta_chars else c for c in individual_chars])
