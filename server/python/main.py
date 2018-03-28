#!/usr/bin/env python3

import sys
import regy
import json
from regy.generate_method import GenerateMethod


def deserialize_samples(samples):
    return json.loads(samples)

def main():
    # samples = deserialize_samples(sys.argv[1])
    samples = deserialize_samples('{"type":"Username","information":{"shouldStartWith":"Letter","shouldContain":["Lowercase letter","Number"],"minimumLength":"3","maximumLength":"7"},"generalRegexInfo":{"startRegexMatchAt":"Start of text","endRegexMatchAt":"End of line","regexTarget":"Java"},"generateMethod":"commonUseCases"}')

    gen_method_map = {
        'samplesAndSemantics': GenerateMethod.SAMPLES_AND_SEMANTICS,
        'commonUseCases'     : GenerateMethod.COMMON_USE_CASES,
        'induction'          : GenerateMethod.INDUCTION
    }

    gen_method = gen_method_map[samples['generateMethod']]
    re = regy.Regy(samples=samples, gen_method=gen_method).get_re()

    print(re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()

