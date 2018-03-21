from collections import deque
from regy.samples_and_semantics.mapper.meta_characters import meta_characters
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens import RepeatInfo, Token


class MapMarkedText:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        marked_strings = self._info[Token.MARKED_TEXT_STRINGS]
        escaped_strings = self._escape_special_characters(marked_strings)
        self._info[Token.ESCAPED_STRINGS] = escaped_strings

        if len(escaped_strings) == 1:
            esc_string = escaped_strings[0]
            if len(esc_string) > 1 and esc_string[0] != '\\' and self._info[Token.REPEAT_INFO] != RepeatInfo.ONE:
                self._re.extend(['(', esc_string, ')'])
            else:
                self._re.append(esc_string)
        else:
            self._re.append('({})'.format('|'.join(escaped_strings)))

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

    def _escape_special_characters(self, marked_strings):
        meta_chars = meta_characters[self._target_lang]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]
