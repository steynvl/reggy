#!/usr/bin/env python3

import sys
import regy


def main():
    samples = sys.argv[1]
    # with open('awe.txt', 'w') as f:
    #     f.write(sys.argv[1])
    # samples = '{"sampleStringsInfo":[{"markerType":"Marked text","markedStrings":["v","version"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Marked text","markedStrings":["."],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"0 or 1"}},{"markerType":"Numbers","markedStrings":["1"],"markerInfo":{"zero":true,"one":true,"two":true,"three":true,"four":true,"five":true,"six":true,"seven":true,"eight":true,"nine":true,"minus":{"minus":false,"optional":false}},"repeatInfo":{"repeat":"n or more times","start":"2"}}],"generalRegexInfo":{"startRegexMatchAt":"Start of word","endRegexMatchAt":"Anywhere","regexTarget":"Java"}}'

    re = regy.Regy(samples=samples).get_re()

    print(re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
