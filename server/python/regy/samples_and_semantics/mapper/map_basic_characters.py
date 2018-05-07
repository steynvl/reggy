from collections import deque
from regy.samples_and_semantics.mapper.meta_characters import meta_characters
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens.basic_characters_ import BasicCharacters, char_keys, basic_characters_to_re


class MapBasicCharacters:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        found = 0

        basic_char_to_re = basic_characters_to_re[self._target_lang]
        for char_key in char_keys:
            if self._info[char_key]:
                found += 1
                self._re.append(basic_char_to_re[char_key])
        
        individual_chars = self._info[BasicCharacters.INDIVIDUAL_CHARACTERS]
        
        found += len(individual_chars)

        self._re.append(self._escape_special_characters(individual_chars))

        enclose = False
        if self._info[BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED]:
            self._re.appendleft(basic_char_to_re[BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED])
            enclose = True
        elif found == 1 and (self._info[BasicCharacters.UPPER_CASE_LETTERS]
                                or self._info[BasicCharacters.LOWER_CASE_LETTERS]):
            enclose = True
        elif found > 1:
            enclose = True

        if enclose:
            self._re.appendleft('[')
            self._re.append(']')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

    def _escape_special_characters(self, individual_chars):
        meta_chars = meta_characters[self._target_lang]
        return ''.join([meta_chars[c] if c in meta_chars else c for c in individual_chars])
