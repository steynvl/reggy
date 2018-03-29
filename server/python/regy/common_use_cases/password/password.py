from collections import deque

from regy.common_use_cases.password.options_to_re import opt_to_re


class Password:

    def __init__(self, info, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = opt_to_re[self._target]

        self._re.append(target[self._info['shouldStartWith']])
        self._re.extend(['(?=.*{})'.format(target[should_contain]) for should_contain in self._info['shouldContain']])

        min_len = int(self._info['minimumLength'])

        if self._info['maximumLength'] == 'No maximum length required':
            if self._info['shouldStartWith'] != 'Anything':
                min_len -= 1
            self._re.append('.{%d,}' % min_len)
        else:
            max_len = int(self._info['maximumLength'])

            if self._info['shouldStartWith'] != 'Anything':
                min_len -= 1
                max_len -= 1
            self._re.append('.{%d,%d}' % (min_len, max_len))
