#!/usr/bin/env python3

import sys
import regy


def main():
    # samples = sys.argv[1]
    samples = '[{"markerType":"Marked text","markedStrings":["v"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Marked text","markedStrings":["."],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"0 or 1"}},{"markerType":"Numbers","markedStrings":["1"],"markerInfo":{"zero":true,"one":true,"two":true,"three":true,"four":true,"five":true,"six":true,"seven":true,"eight":true,"nine":true,"minus":{"minus":false,"optional":false}},"repeatInfo":{"repeat":"Custom range","start":"1","end":"3"}}]'

    scanner = regy.Scan(samples)
    scanned_samples = scanner.get_scanned_samples()

    for i in scanned_samples:
        print(i)
        print('')



if __name__ == '__main__':
    main()