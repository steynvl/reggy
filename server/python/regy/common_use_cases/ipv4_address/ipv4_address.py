from collections import deque

from regy.common_use_cases.ipv4_address.options_to_re import ip_to_re, field_to_key


class Ipv4Address:

    def __init__(self, info, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = ip_to_re[self._target]
        checked_options = self._get_checked_options()

        if len(checked_options) == 0:
            return
        elif len(checked_options) == 1:
            self._re.append(target[checked_options[0]])
        else:
            self._re.append('(?:{})'.format('|'.join([target[i] for i in checked_options])))

    def _get_checked_options(self):
        return [field_to_key[option] for option in field_to_key.keys() if self._info[option]]
