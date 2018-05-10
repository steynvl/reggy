from collections import deque
import re
from regy.samples.mapper.meta_characters import meta_characters
from regy.samples.mapper.repeat_helper import repeat_info_to_regex
from regy.samples.tokens import Token
from regy.samples.tokens.case_state import CaseSensitive
from regy.samples.tokens.repeat_info import RepeatInfo
from regy.samples.tokens.list_of_literal_text import ListOfLiteralText


class MapListOfLiteralText:


    def __init__(self, info, target_lang, case_state):
        self._info = info
        self._target_lang = target_lang
        self._case_state = case_state
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        match_anything_except = self._info[ListOfLiteralText.MATCH_ANYTHING_EXCEPT_SPECFIED]

        escaped_literals = self._escape_special_characters(self._info[ListOfLiteralText.LITERAL_TEXT])
        self._re.append('|'.join(escaped_literals))

        if match_anything_except:
            self._re.appendleft('(?!')
            self._re.append(').')
        else:
            repeat_info = self._info[Token.REPEAT_INFO]
            llt = self._info[ListOfLiteralText.LITERAL_TEXT]
                
            if len(llt) > 1 or repeat_info != RepeatInfo.ONE:
                if not (len(llt) == 1 and len(llt[0]) == 1):
                    self._re.appendleft('(?:')
                    self._re.append(')')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        self._add_case_state(escaped_literals)

    def _add_case_state(self, escaped_literals):
        case_insensitive = self._info[ListOfLiteralText.CASE_INSENSITIVE]

        if case_insensitive:
            if not self._case_state['case'] == CaseSensitive.OFF:
                self._re.appendleft('(?i)')
                self._case_state['case'] = CaseSensitive.OFF
                self._case_state['hasChanged'] = True
        else:
            if self._case_state['hasChanged']:
                self._re.appendleft('(?-i)')
                self._case_state['case'] = CaseSensitive.ON

            if self._does_contain_letters(escaped_literals):
                self._case_state['canUseCaseInsensitiveFlag'] = False

    def _escape_special_characters(self, marked_strings):
        meta_chars = meta_characters[self._target_lang]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]

    @staticmethod
    def _does_contain_letters(escaped_literals):
        letters_re = re.compile(r'[A-Za-z]')
        return any([letters_re.match(i) for i in escaped_literals])
