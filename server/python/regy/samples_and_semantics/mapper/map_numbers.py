from collections import deque
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens import Token


class MapNumbers:

    def __init__(self, info):
        self._info = info
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        marker_info = self._info[Token.NUMBERS]
        if len(marker_info) == 10:
            self._re.append('\\d')
        else:
            self._re.append(self._calculate_character_class(marker_info))

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

    @staticmethod
    def _calculate_character_class(marker_info):
        nums = sorted([i.value for i in marker_info])

        ranges = []
        for i in range(len(nums)):
            if i == 0:
                ranges.append([nums[i], nums[i]])
            else:
                if nums[i] - ranges[-1][1] == 1:
                    ranges[-1][1] = nums[i]
                else:
                    ranges.append([nums[i], nums[i]])

        char_class = []
        for i in ranges:
            if i[0] == i[1]:
                char_class.append(str(i[0]))
            elif i[1] - i[0] == 1:
                char_class.append(str(i[0]))
                char_class.append(str(i[1]))
            else:
                char_class.append('{}-{}'.format(str(i[0]), str(i[1])))

        return '[{}]'.format(''.join(char_class))
