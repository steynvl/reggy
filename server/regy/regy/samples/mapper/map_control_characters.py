from collections import deque

from regy.samples.constants.control_characters import control_char_to_re
from regy.samples.mapper.repeat_helper import repeat_info_to_regex
from regy.samples.models.control_characters_info import ControlCharactersInfo


class MapControlCharacters:

    def __init__(self, info: ControlCharactersInfo, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        char_to_re = control_char_to_re[self._target_lang]
        control_chars = self._info.wanted_control_chars

        if len(control_chars) == 0:
            return
        elif len(control_chars) == 1:
            self._re.append(char_to_re[control_chars[0]])
        else:
            ranges = []
            for i in range(len(control_chars)):
                if i == 0:
                    ranges.append([control_chars[0], None])
                else:
                    index = 0 if ranges[-1][1] is None else 1
                    if control_chars[i].value - ranges[-1][index].value == 1:
                        ranges[-1][1] = control_chars[i]
                    else:
                        ranges.append([control_chars[i], None])

            for r in ranges:

                if r[1] is None:
                    self._re.append(char_to_re[r[0]])
                elif r[1].value - r[0].value == 1:
                    self._re.append(char_to_re[r[0]])
                    self._re.append(char_to_re[r[1]])
                else:
                    self._re.append(char_to_re[r[0]])
                    self._re.append('-')
                    self._re.append(char_to_re[r[1]])

            self._re.append(']')
            self._re.appendleft('[')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)
