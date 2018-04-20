from collections import deque

from regy.common_use_cases.date_and_time.options_to_re import identifiers_to_re, options_to_re
from regy.common_use_cases.models.date_and_time_info import DateAndTimeInfo


class DateAndTime:

    def __init__(self, info: DateAndTimeInfo, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        opt_to_re = options_to_re[self._target]

        date_sep  = opt_to_re['dateSeparators'][self._info.date_separator]
        time_sep  = opt_to_re['timeSeparators'][self._info.time_separator]
        am_pm_inc = opt_to_re['amPmIndicators'][self._info.am_pm_indicator]

        formats = self._get_formats()

        for char in formats:

            if char in identifiers_to_re.keys():
                pass
            elif char == '/':
                pass
            elif char == 'a':
                pass
            elif char == ':':
                pass


    def _get_formats(self):
        return map(str.strip, self._info.date_formats.split('\n'))
