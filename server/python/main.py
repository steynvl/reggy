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

    # samples = deserialize_samples('{"sampleStringsInfo":[{"markerType":"Unicode characters","markedStrings":["sdas"],"markerInfo":{"lowercaseLetters":false,"uppercaseLetters":false,"titleCaseLetters":false,"casedLetters":true,"modifierLetters":true,"otherLetters":true,"nonSpacingMarks":false,"spacingCombiningMarks":false,"enclosingMarks":false,"spaceSeparators":false,"lineSeparators":false,"paragraphSeparators":false,"mathSymbols":true,"currencySymbols":false,"modifierSymbols":false,"otherSymbols":false,"decimalDigitNumbers":false,"letterNumbers":false,"otherNumbers":false,"dashPunctuation":false,"openPunctuation":false,"closePunctuation":false,"initialPunctuation":false,"finalPunctuation":false,"connectorPunctuation":false,"otherPunctuation":false,"controlCharacters":false,"formatCharacters":false,"privateUseCharacters":false,"surrogateCharacters":false,"unassignedCharacters":false,"matchAllExceptSelectedOnes":false,"individualCharacters":""},"repeatInfo":{"repeat":"1"}}],"generalRegexInfo":{"startRegexMatchAt":"Anywhere","endRegexMatchAt":"Anywhere","regexTarget":"Java"},"generateMethod":"samplesAndSemantics"}')

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
