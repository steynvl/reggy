from collections import deque
import re
from reggy.samples.constants.meta_characters import meta_characters
from reggy.samples.mapper.repeat_helper import repeat_info_to_regex
from reggy.samples.models.list_of_literal_text_info import ListOfLiteralTextInfo
from reggy.samples.tokens.case_state import CaseSensitive
from reggy.samples.tokens.repetition import Repetition
from reggy.samples.utils.factorizer import Factorizer


class MapListOfLiteralText:

    def __init__(self, info: ListOfLiteralTextInfo, target_lang, state_info):
        self._info = info
        self._target_lang = target_lang
        self._state_info = state_info
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        match_anything_except = self._info.match_anything_except_specified
        escaped_literals = self._escape_special_characters(self._info.literal_text)
        grouped = False

        self._re.append(Factorizer(escaped_literals).get_re())

        if match_anything_except:
            self._re.appendleft('(?!')
            self._re.append(').')
        else:
            repeat_info = self._info.repetition_info.repeat_info
            llt = self._info.literal_text
                
            if len(llt) == 1 and repeat_info != Repetition.ONE:
                if not (len(llt) == 1 and len(llt[0]) == 1):
                    grouped = True
                    self._re.appendleft('(')
                    if not self._state_info['isBackReferenced']:
                        self._re.append('?:')
                    self._re.append(')')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

        self._add_case_state(escaped_literals)

        if self._state_info['isBackReferenced']:
            if not grouped:
                self._re.appendleft('(')
                self._re.append(')')
            self._state_info['currBackReferenceNum'] += 1
            self._state_info['markerToReference'][self._info.marker_id] = self._state_info['currBackReferenceNum']

    def _add_case_state(self, escaped_literals):
        case_insensitive = self._info.case_insensitive

        if case_insensitive:
            if not self._state_info['case'] == CaseSensitive.OFF:
                self._re.appendleft('(?i)')
                self._state_info['case'] = CaseSensitive.OFF
                self._state_info['hasChanged'] = True
        else:
            if self._state_info['hasChanged']:
                self._re.appendleft('(?-i)')
                self._state_info['case'] = CaseSensitive.ON

            if self._does_contain_letters(escaped_literals):
                self._state_info['canUseCaseInsensitiveFlag'] = False

    def _escape_special_characters(self, marked_strings):
        meta_chars = meta_characters[self._target_lang]

        return [''.join([meta_chars[c] if c in meta_chars else c for c in string]) for string in marked_strings]

    @staticmethod
    def _does_contain_letters(escaped_literals):
        letters_re = re.compile(r'[A-Za-z]')
        return any([letters_re.match(i) for i in escaped_literals])
