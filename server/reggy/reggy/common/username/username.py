from collections import deque

from reggy.common.models.username_info import UsernameInfo
from reggy.common.username.options_to_re import opt_to_re


class Username:

    def __init__(self, info: UsernameInfo, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = opt_to_re[self._target]

        self._re.append(target[self._info.should_start_with])
        self._re.extend(['(?=.*{})'.format(target[should_contain]) for should_contain in self._info.should_contain])

        min_len = int(self._info.min_length)

        if self._info.max_length == 'No maximum length required':
            if self._info.should_start_with != 'Anything':
                min_len -= 1
            self._re.append('.{%d,}' % min_len)
        else:
            max_len = int(self._info.max_length)

            if self._info.should_start_with != 'Anything':
                min_len -= 1
                max_len -= 1
            self._re.append('.{%d,%d}' % (min_len, max_len))
