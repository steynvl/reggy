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
            nums = '[{}]'.format(''.join([i.value for i in marker_info]))

        if self._info['repeatInfo'] == RepeatInfo.CUSTOM_RANGE:
            repeat_range = self._info['repeatRange']
            s = repeat_range['start']
            e = repeat_range['end']
            self.re = nums + repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
        else:
            self.re = nums + repeat_info_map[self._info['repeatInfo']]
