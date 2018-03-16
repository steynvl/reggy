from regy.mapper.map_repeat_info import repeat_info_map
from regy.tokens import RepeatInfo


class MapNumbers:

    def __init__(self, info):
        self._info = info
        self.re = None
        self._map_info()

    def get_re(self):
        return self.re

    def _map_info(self):
        marker_info = self._info['numbers']
        if len(marker_info) == 10:
            nums = '\\d'
        else:
            nums = self._calculate_character_class(marker_info)

        if self._info['repeatInfo'] == RepeatInfo.CUSTOM_RANGE:
            repeat_range = self._info['repeatRange']
            s = repeat_range['start']
            e = repeat_range['end']
            self.re = nums + repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
        else:
            self.re = nums + repeat_info_map[self._info['repeatInfo']]


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
