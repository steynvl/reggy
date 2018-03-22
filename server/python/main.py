#!/usr/bin/env python3

import sys
import regy
import json
from regy.generate_method import GenerateMethod


def deserialize_samples(samples):
    return json.loads(samples)

def main():
    samples = deserialize_samples(sys.argv[1])
    # with open('awe.txt', 'w') as f:
    #     f.write(sys.argv[1])
    # samples = deserialize_samples('{"sampleStringsInfo":[{"markerType":"Marked text","markedStrings":["version","v"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Marked text","markedStrings":["."],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"0 or 1"}},{"markerType":"Numbers","markedStrings":["1"],"markerInfo":{"zero":true,"one":true,"two":true,"three":true,"four":true,"five":true,"six":true,"seven":true,"eight":true,"nine":true,"minus":{"minus":false,"optional":false}},"repeatInfo":{"repeat":"Custom range","start":"1","end":"3"}}],"generalRegexInfo":{"startRegexMatchAt":"Start of line","endRegexMatchAt":"End of line","regexTarget":"Perl"}}')

    if samples['generateMethod'] == 'samplesAndSemantics':
        gen_method = GenerateMethod.SAMPLES_AND_SEMANTICS
    elif samples['generateMethod'] == 'commonUseCases':
        gen_method = GenerateMethod.COMMON_USE_CASES
    elif samples['generateMethod'] == 'induction':
        gen_method = GenerateMethod.COMMON_USE_CASES
    else:
        sys.exit(2)

    re = regy.Regy(samples=samples, gen_method=gen_method).get_re()

    print(re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
