from collections import deque
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens import Token
from regy.samples_and_semantics.tokens.unicode_characters import unicode_char_to_re


class MapUnicodeCharacters:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        char_to_re = unicode_char_to_re[self._target_lang]
        unicode_chars = self._info[Token.UNICODE_CHARACTERS]
        individual = self._info[Token.INDIVIDUAL_UNICODE_CHARS]

        if len(unicode_chars) + len(individual) == 0:
            return
        elif len(unicode_chars) == 1 and len(individual) == 0:
            self._re.append(char_to_re[unicode_chars[0]])
        else:
            self._re.extend([char_to_re[unicode_char] for unicode_char in unicode_chars])
            self._re.extend(individual)
            self._re.append(']')
            self._re.appendleft('[')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)
