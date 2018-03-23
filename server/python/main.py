#!/usr/bin/env python3

import sys
import regy
import json
from regy.generate_method import GenerateMethod


def deserialize_samples(samples):
    return json.loads(samples)

def main():
    # samples = deserialize_samples(sys.argv[1])
    # with open('awe.txt', 'w') as f:
    #     f.write(sys.argv[1])
    samples = deserialize_samples('{"sampleStringsInfo":[{"markerType":"Marked text","markedStrings":["lk"],"markerInfo":{"caseInsensitive":false,"matchAllExceptSpecified":false},"repeatInfo":{"repeat":"1 or more"}},{"markerType":"Control characters","markedStrings":["jlk"],"markerInfo":{"nul":false,"startOfHeading":true,"startOfText":true,"endOfText":true,"endOfTransmission":true,"enquiry":true,"acknowledge":false,"bell":false,"backspace":false,"horizontalTab":false,"newLine":false,"verticalTab":true,"formFeed":true,"carriageReturn":true,"shiftOut":false,"shiftIn":false,"dataLinkEscape":false,"deviceControlOne":false,"deviceControlTwo":true,"deviceControlThree":true,"deviceControlFour":true,"negativeAcknowledge":false,"synchronousIdle":false,"endOfTransBlock":false,"cancel":false,"endOfMedium":false,"substitute":true,"escape":true,"fileSeparator":true,"groupSeparator":false,"recordSeparator":false,"unitSeparator":false,"matchAllExceptSelectedOnes":false},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"},"generateMethod":"samplesAndSemantics"}')
    #
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
