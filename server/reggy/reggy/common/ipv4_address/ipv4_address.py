from collections import deque

from reggy.common.ipv4_address.options_to_re import ip_to_re
from reggy.common.models.ipv4_info import Ipv4Info


class Ipv4Address:

    def __init__(self, info: Ipv4Info, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = ip_to_re[self._target]
        checked_options = self._info.get_checked_options()

        if len(checked_options) == 0:
            return
        elif len(checked_options) == 1:
            self._re.append(target[checked_options[0]])
        else:
            self._re.append('(?:{})'.format('|'.join([target[i] for i in checked_options])))
