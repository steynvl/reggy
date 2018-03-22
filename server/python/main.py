#!/usr/bin/env python3

import sys
import regy


def main():
    samples = sys.argv[1]
    # with open('awe.txt', 'w') as f:
    #     f.write(sys.argv[1])
    # samples = '{"sampleStringsInfo":[{"markerType":"Basic characters","markedStrings":["sdasd"],"markerInfo":{"caseInsensitive":false,"lowerCaseLetters":true,"upperCaseLetters":false,"digits":false,"punctuationAndSymbols":false,"matchAllExceptSpecified":false,"whiteSpace":false,"lineBreaks":false,"individualCharacters":""},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"}}'
    # samples = '{"sampleStringsInfo":[{"markerType":"Marked text","markedStrings":["aaaa"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Numbers","markedStrings":["aaaaaaa"],"markerInfo":{"zero":true,"one":true,"two":true,"three":true,"four":true,"five":true,"six":true,"seven":true,"eight":true,"nine":true,"minus":{"minus":false,"optional":true}},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"}}'

    re = regy.Regy(samples=samples).get_re()

    print(re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
