from regy.mapper.map_repeat_info import repeat_info_map
from regy.mapper.meta_characters import meta_characters
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
        escaped_strings = self._escape_special_characters(marked_strings)

        if len(escaped_strings) == 1:
            alternation = escaped_strings[0]
        else:
            alternation = '({})'.format('|'.join(escaped_strings))

        if self._info['repeatInfo'] == RepeatInfo.CUSTOM_RANGE:
            repeat_range = self._info['repeatRange']
            s = repeat_range['start']
            e = repeat_range['end']
            self.re = alternation + repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
        else:
            self.re = alternation + repeat_info_map[self._info['repeatInfo']]

    @staticmethod
    def _escape_special_characters(marked_strings, target='java'):
        meta_chars = meta_characters[target]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]
