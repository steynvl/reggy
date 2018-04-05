from collections import deque

from regy.samples_and_semantics.mapper.repeat_helper import repeat_info_to_regex
from regy.samples_and_semantics.tokens.match_anything import MatchAnything, basic_char_to_re, can_span_across_lines


class MapMatchAnything:

    def __init__(self, info, target_lang):
        self._info = info
        self._target_lang = target_lang
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        enclose_in_brackets = True

        if MatchAnything.SPECIFIC_CHARACTERS in self._info:
            self._re.append(self._info[MatchAnything.SPECIFIC_CHARACTERS])
            if self._info[MatchAnything.CAN_SPAN_ACROSS_LINES]:
                self._re.appendleft(can_span_across_lines[self._target_lang])
        elif MatchAnything.SPECIFIC_CHARACTER in self._info:
            self._re.append(self._info[MatchAnything.SPECIFIC_CHARACTER])
            if self._info[MatchAnything.CAN_SPAN_ACROSS_LINES]:
                self._re.appendleft(can_span_across_lines[self._target_lang])
        elif MatchAnything.NOTHING in self._info:
            if self._info[MatchAnything.CAN_SPAN_ACROSS_LINES]:
                self._re.append(can_span_across_lines[self._target_lang])
            else:
                self._re.append('.')
                enclose_in_brackets = False
        elif MatchAnything.BASIC_CHARACTERS in self._info:
            if len(self._info[MatchAnything.BASIC_CHARACTERS]) == 0 and not self._info[MatchAnything.CAN_SPAN_ACROSS_LINES]:
                self._re.append('.')
                enclose_in_brackets = False

            basic_to_re = basic_char_to_re[self._target_lang]
            self._re.append(''.join([basic_to_re[i] for i in self._info[MatchAnything.BASIC_CHARACTERS]]))
            if self._info[MatchAnything.CAN_SPAN_ACROSS_LINES] and MatchAnything.LINE_BREAKS not in self._info[MatchAnything.BASIC_CHARACTERS]:
                self._re.append(can_span_across_lines[self._target_lang])

        if enclose_in_brackets:
            self._re.append(']')
            self._re.appendleft('[^')

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)
