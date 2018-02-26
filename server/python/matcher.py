#!/usr/bin/env python3

import os
import sys
import json


def alternation_regex(sample_strings):
    alternation = '|'.join(sample_strings)
    return '({})'.format(alternation)


def get_common_prefix(sample_strings):
    return os.path.commonprefix(sample_strings)


def get_common_suffix(list_of_strings):
    reverse = [s[::-1] for s in list_of_strings]
    return get_common_prefix(reverse)[::-1]


def main():
    sample_strings = list(map(str.strip, sys.argv[1:]))

    prefix = get_common_prefix(sample_strings)

    suffix_sample_strings = [i[len(prefix):] for i in sample_strings]
    suffix = get_common_suffix(suffix_sample_strings)

    if prefix != '' or suffix != '':
        original_size = len(sample_strings)
        sample_strings = list(filter(lambda s: len(s) > len(prefix) and len(s) > len(suffix), sample_strings))
        body = [i[len(prefix):len(i)-len(suffix)] for i in sample_strings]
        optional = '?' if original_size > len(sample_strings) else ''
        regex = '{0}({1}){2}{3}'.format(prefix, '|'.join(body), optional, suffix).replace('()?', '')
    else:
        regex = alternation_regex(sample_strings)

    print(json.dumps(regex))
    sys.stderr.flush()


if __name__ == '__main__':
    main()
