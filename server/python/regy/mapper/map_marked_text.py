from regy.mapper.map_repeat_info import repeat_info_map
from regy.tokens import RepeatInfo


class MapMarkedText:

    def __init__(self, info):
        self._info = info
        self.re = None
        self._map_info()

    def get_re(self):
        return self.re

    def _map_info(self):
        marked_strings = self._info['strings']
        alternation = '({})'.format('|'.join(marked_strings))
        if self._info['repeatInfo'] == RepeatInfo.CUSTOM_RANGE:
            repeat_range = self._info['repeatRange']
            s = repeat_range['start']
            e = repeat_range['end']
            self.re = alternation + repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
        else:
            self.re = alternation + repeat_info_map[self._info['repeatInfo']]
