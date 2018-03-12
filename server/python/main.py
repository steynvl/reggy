#!/usr/bin/env python3

import sys
import regy
import regy.mapper as mapper
from regy.tokens import MarkerType


def main():
    samples = sys.argv[1]
    # samples = '[{"markerType":"Marked text","markedStrings":["v"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Marked text","markedStrings":["."],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"0 or 1"}},{"markerType":"Numbers","markedStrings":["1"],"markerInfo":{"zero":false,"one":true,"two":true,"three":true,"four":true,"five":true,"six":true,"seven":true,"eight":true,"nine":true,"minus":{"minus":false,"optional":false}},"repeatInfo":{"repeat":"Custom range","start":"1","end":"3"}}]'

    scanner = regy.Scanner(samples)
    scanned_samples = scanner.get_scanned_samples()

    re_list = []
    for scanned_sample in scanned_samples:

        marker_type = scanned_sample['markerType']
        if marker_type == MarkerType.MARKED_TEXT:
            re_list.append(mapper.MapMarkedText(scanned_sample).get_re())
        elif marker_type == MarkerType.NUMBERS:
            re_list.append(mapper.MapNumbers(scanned_sample).get_re())

    re = ''.join(re_list)

    print(re)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
