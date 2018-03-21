from collections import deque
from regy.samples_and_semantics.mapper.basic_characters_to_re import basic_characters_to_re
from regy.samples_and_semantics.mapper.meta_characters import meta_characters
from regy.samples_and_semantics.tokens.basic_characters_info import BasicCharactersInfo

char_keys = [
    BasicCharactersInfo.LOWER_CASE_LETTERS, BasicCharactersInfo.UPPER_CASE_LETTERS,
    BasicCharactersInfo.DIGITS, BasicCharactersInfo.PUNCTUATION_AND_SYMBOLS,
    BasicCharactersInfo.WHITE_SPACE, BasicCharactersInfo.LINE_BREAKS
]


class MapBasicCharacters:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        global char_keys
        found = 0

        basic_char_to_re = basic_characters_to_re[self._target_lang]
        for char_key in char_keys:
            if self._info[char_key]:
                found += 1
                self._re.append(basic_char_to_re[char_key])

        individual_chars = self._info[BasicCharactersInfo.INDIVIDUAL_CHARACTERS]
        self._re.append(self._escape_special_characters(individual_chars))

        enclose = False
        if self._info[BasicCharactersInfo.MATCH_ALL_EXCEPT_SPECIFIED] and found > 0:
            self._re.appendleft(basic_char_to_re[BasicCharactersInfo.MATCH_ALL_EXCEPT_SPECIFIED])
            enclose = True
        elif found == 1 and (self._info[BasicCharactersInfo.UPPER_CASE_LETTERS]
                                or self._info[BasicCharactersInfo.LOWER_CASE_LETTERS]):
            enclose = True
        elif found > 1:
            enclose = True

        if enclose:
            self._re.appendleft('[')
            self._re.append(']')

    def _escape_special_characters(self, individual_chars):
        meta_chars = meta_characters[self._target_lang]
        return ''.join([meta_chars[c] if c in meta_chars else c for c in individual_chars])
