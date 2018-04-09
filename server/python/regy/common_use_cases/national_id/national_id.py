from collections import deque

from regy.common_use_cases.models.national_id_info import NationalIdInfo
from regy.common_use_cases.national_id.options_to_re import national_id_to_re


class NationalId:

    def __init__(self, info: NationalIdInfo, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        id_to_re = national_id_to_re[self._target]
        self._re.append(id_to_re[self._info.kind])
