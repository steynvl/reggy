#!/usr/bin/env python3

import sys
import regy
import json


def deserialize_samples(samples):
    return json.loads(samples)

def main():
    samples = deserialize_samples(sys.argv[1])

    re = regy.Regy(samples=samples).get_re()

    serialized_re = json.dumps(re)

    sys.stdout.write(serialized_re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
