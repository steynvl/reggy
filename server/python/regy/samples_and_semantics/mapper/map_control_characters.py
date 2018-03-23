from collections import deque

from regy.samples_and_semantics.tokens import Token
from regy.samples_and_semantics.tokens.control_characters_info import control_char_to_re


class MapControlCharacters:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        char_to_re = control_char_to_re[self._target_lang]
        control_chars = self._info[Token.CONTROL_CHARACTERS]

        if len(control_chars) == 0:
            return
        elif len(control_chars) == 1:
            self._re.append(char_to_re[control_chars[0]])
        else:
            # TODO find ranges (i.e \x09-\x1c)
            self._re.extend([char_to_re[i] for i in control_chars])
            self._re.append(']')
            self._re.appendleft('[')
