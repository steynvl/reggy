#!/usr/bin/env python3

import sys
import regy


def main():
    samples = sys.argv[1]

    re = regy.Regy(samples=samples).get_re()

    print(re)
    sys.stdout.flush()

if __name__ == '__main__':
    main()
