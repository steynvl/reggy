from collections import deque
from regy.common_use_cases.currency.currency_to_code import currency_to_code
from regy.common_use_cases.models.currency_info import CurrencyInfo


class Currency:

    def __init__(self, info: CurrencyInfo, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        codes = [currency_to_code[curr] for curr in self._info.currencies]

        if len(codes) == 0:
            return
        elif len(codes) == 1:
            self._re.append(codes[0])
        else:
            self._re.append('(?:{})'.format('|'.join(codes)))

