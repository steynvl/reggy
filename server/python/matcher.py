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


def slice_str(string, prefix_length, suffix_length):
    return string[prefix_length:len(string) - suffix_length]


def main():
    with open('awe.txt', 'w') as f:
        f.write(sys.argv[1])

    sample_strings = list(map(str.strip, sys.argv[1:]))

    prefix = get_common_prefix(sample_strings)

    suffix_sample_strings = [i[len(prefix):] for i in sample_strings]
    suffix = get_common_suffix(suffix_sample_strings)

    if prefix != '' or suffix != '':
        p_length = len(prefix)
        s_length = len(suffix)

        original_size = len(sample_strings)
        sample_strings = list(filter(lambda s: len(s) > len(prefix) and len(s) > len(suffix), sample_strings))

        body = [slice_str(i, p_length, s_length) for i in sample_strings if slice_str(i, p_length, s_length) != '']
        optional_item = original_size > len(sample_strings) or original_size > len(body)

        if optional_item:
            regex = '{0}({1})?{2}'.format(prefix, '|'.join(body), suffix).replace('()?', '')
        else:
            regex = '{0}({1}){2}'.format(prefix, '|'.join(body), suffix)
    else:
        regex = alternation_regex(sample_strings)

    print(json.dumps(regex))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
