import regy
from regy.samples_and_semantics import mapper
from regy.samples_and_semantics.tokens.marker_type import MarkerType


class Regy:

    def __init__(self, samples):
        self._samples = samples
        self._re_list = []
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re_list)

    def _calculate_regex(self):
        scanner = regy.Scanner(self._samples)
        scanned_samples = scanner.get_scanned_samples()

        for scanned_sample in scanned_samples:

            marker_type = scanned_sample['markerType']
            if marker_type == MarkerType.MARKED_TEXT:
                self._re_list.append(''.join(mapper.MapMarkedText(scanned_sample).get_re_list()))
            elif marker_type == MarkerType.NUMBERS:
                self._re_list.append(''.join(mapper.MapNumbers(scanned_sample).get_re_list()))
