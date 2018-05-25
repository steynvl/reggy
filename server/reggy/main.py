#!/usr/bin/env python3

import sys
import reggy
import json


def deserialize_samples(samples):
    return json.loads(samples)


def serialize_re(re):
    return json.dumps(re)


def main():
    samples = deserialize_samples(sys.argv[1])

    # samples = deserialize_samples('{"sampleStringsInfo":[{"markerType":"Basic characters","markedStrings":["aad"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false,"lowerCaseLetters":true,"punctuationAndSymbols":true,"individualCharacters":"qqqq"},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"},"generateMethod":"samplesAndSemantics"}')



    re = reggy.Reggy(samples=samples).get_re()

    serialized_re = serialize_re(re)

    sys.stdout.write(serialized_re)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
