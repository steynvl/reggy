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
    # samples = deserialize_samples('{"sampleStringsInfo":[{"markerType":"Marked text","markedStrings":["d"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1"}},{"markerType":"Control characters","markedStrings":["aaaaa"],"markerInfo":{"nul":true,"startOfHeading":true,"startOfText":false,"endOfText":false,"endOfTransmission":false,"enquiry":false,"acknowledge":false,"bell":false,"backspace":false,"horizontalTab":false,"newLine":false,"verticalTab":false,"formFeed":false,"carriageReturn":false,"shiftOut":false,"shiftIn":false,"dataLinkEscape":false,"deviceControlOne":false,"deviceControlTwo":false,"deviceControlThree":false,"deviceControlFour":false,"negativeAcknowledge":false,"synchronousIdle":false,"endOfTransBlock":false,"cancel":false,"endOfMedium":false,"substitute":false,"escape":false,"fileSeparator":false,"groupSeparator":false,"recordSeparator":false,"unitSeparator":false,"matchAllExceptSelectedOnes":true},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"},"generateMethod":"samplesAndSemantics"}')

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
