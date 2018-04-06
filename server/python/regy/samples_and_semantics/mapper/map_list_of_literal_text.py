from collections import deque
from regy.samples_and_semantics.mapper.meta_characters import meta_characters
from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens.list_of_literal_text import ListOfLiteralText


class MapListOfLiteralText:


    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        match_anything_except = self._info[ListOfLiteralText.MATCH_ANYTHING_EXCEPT_SPECFIED]

        self._re.append('|'.join(self._info[ListOfLiteralText.LITERAL_TEXT]))

        if match_anything_except:
            self._re.appendleft('(?!')
            self._re.append(').')


        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)


    def _escape_special_characters(self, marked_strings):
        meta_chars = meta_characters[self._target_lang]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]
