from collections import deque

from regy.common_use_cases.url.options_to_re import opt_to_re


class Url:

    def __init__(self, info, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = opt_to_re[self._target]
