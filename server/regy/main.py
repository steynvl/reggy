#!/usr/bin/env python3

import sys
import regy
import json


def deserialize_samples(samples):
    return json.loads(samples)


def serialize_re(re):
    return json.dumps(re)


def main():
    samples = deserialize_samples(sys.argv[1])

    re = regy.Regy(samples=samples).get_re()

    serialized_re = serialize_re(re)

    sys.stdout.write(serialized_re)
    sys.stdout.flush()


if __name__ == '__main__':
    main()
