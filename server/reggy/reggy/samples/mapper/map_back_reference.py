from collections import deque
from reggy.samples.models.back_reference_info import BackReferenceInfo


class MapBackReference:

    def __init__(self, info: BackReferenceInfo, target_lang, state_info):
        self._info = info
        self._target_lang = target_lang
        self._state_info = state_info
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        self._re.append('\\{}'.format(self._state_info['markerToReference'][self._info.marker['id']]))

        if self._state_info['isBackReferenced']:
            self._re.appendleft('(')
            self._re.append(')')

            self._state_info['currBackReferenceNum'] += 1
            self._state_info['markerToReference'][self._info.marker_id] = self._state_info['currBackReferenceNum']
