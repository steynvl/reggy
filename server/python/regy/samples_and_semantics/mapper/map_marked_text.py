from regy.samples_and_semantics.mapper.meta_characters import meta_characters
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens import RepeatInfo


class MapMarkedText:

    def __init__(self, info):
        self._info = info
        self._re_list = []
        self._map_info()

    def get_re_list(self):
        return self._re_list

    def _map_info(self):
        marked_strings = self._info['strings']
        escaped_strings = self._escape_special_characters(marked_strings)
        self._info['escapedStrings'] = escaped_strings

        if len(escaped_strings) == 1:
            esc_string = escaped_strings[0]
            if len(esc_string) > 1 and esc_string[0] != '\\' and self._info['repeatInfo'] != RepeatInfo.ONE:
                self._re_list.extend(['(', esc_string, ')'])
            else:
                self._re_list.append(esc_string)
        else:
            self._re_list.append('({})'.format('|'.join(escaped_strings)))

        repeat_info = repeat_info_to_regex(self._info)
        self._re_list.append(repeat_info)

    @staticmethod
    def _escape_special_characters(marked_strings, target='java'):
        meta_chars = meta_characters[target]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]
