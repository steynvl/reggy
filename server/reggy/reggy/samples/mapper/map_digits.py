from collections import deque
from reggy.samples.mapper.repeat_helper import repeat_info_to_regex
from reggy.samples.models.digits_info import DigitsInfo
from reggy.samples.tokens import Target


class MapDigits:

    def __init__(self, info: DigitsInfo, target_lang, state_info):
        self._info = info
        self._target_lang = target_lang
        self._state_info = state_info
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        marker_info = self._info.digits
        if len(marker_info) == 10:
            if self._target_lang == Target.JAVA:
                self._re.append('\\\\d')
            else:
                self._re.append('\\d')
        else:
            self._re.append(self._calculate_character_class(marker_info))

        if self._info.include_minus:
            self._re.appendleft('-')
        elif self._info.include_optional_minus:
            self._re.appendleft('-?')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        if self._state_info['isBackReferenced']:
            self._re.appendleft('(')
            self._re.append(')')

            self._state_info['currBackReferenceNum'] += 1
            self._state_info['markerToReference'][self._info.marker_id] = self._state_info['currBackReferenceNum']

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

        if len(char_class) == 1 and len(char_class[0]) == 1:
            return ''.join(char_class)
        else:
            return '[{}]'.format(''.join(char_class))
