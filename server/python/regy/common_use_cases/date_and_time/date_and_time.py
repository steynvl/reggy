from collections import deque
from regy.common_use_cases.date_and_time.options_to_re import identifiers_to_re, options_to_re
from regy.common_use_cases.models.date_and_time_info import DateAndTimeInfo


class DateAndTime:

    def __init__(self, info: DateAndTimeInfo, target):
        self._info = info
        self._target = target
        self._re = []
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        opt_to_re = options_to_re[self._target]

        date_sep  = opt_to_re['dateSeparators'][self._info.date_separator]
        time_sep  = opt_to_re['timeSeparators'][self._info.time_separator]
        am_pm_inc = opt_to_re['amPmIndicators'][self._info.am_pm_indicator]

        formats = self._get_formats()

        for _format in formats:

            tmp = []
            for char in _format:
                
                curr = deque()
                if char in identifiers_to_re.keys():
                    if char == 'y' or char == 'Y':
                        curr.append(identifiers_to_re[char])
                    else:
                        curr.append(identifiers_to_re[char][self._info.leading_zeros])          
                        if len(_format) > 1:
                            curr.appendleft('(?:')
                            curr.append(')')

                elif char == '/':
                    curr.append(date_sep)
                elif char == 'a':
                    curr.append(am_pm_inc)
                elif char == ':':
                    curr.append(time_sep)
                elif char == ' ':
                    curr.append(' ')
                
                tmp.append(''.join(curr))
            
            self._re.append(''.join(tmp))

        if len(self._re) > 1:
            self._re = ['(?:{})'.format('|'.join(self._re))]

    def _get_formats(self):
        return map(str.strip, self._info.date_formats.split('\n'))
