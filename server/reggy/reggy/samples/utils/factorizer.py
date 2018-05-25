import os


class Factorizer:

    def __init__(self, strings: list):
        self._re = None
        self._calculate_regex(strings)

    def get_re(self):
        return self._re

    def _calculate_regex(self, strings: list):
        prefix = self._get_common_prefix(strings)

        suffix_sample_strings = [i[len(prefix):] for i in strings]
        suffix = self._get_common_suffix(suffix_sample_strings)

        if prefix != '' or suffix != '':
            p_length = len(prefix)
            s_length = len(suffix)

            original_size = len(strings)
            strings = list(filter(lambda s: len(s) > len(prefix) and len(s) > len(suffix), strings))

            body = [
                self._slice_str(i, p_length, s_length) for i in strings if self._slice_str(i, p_length, s_length) != ''
            ]
            optional_item = original_size > len(strings) or original_size > len(body)

            if optional_item:
                self._re = '{0}(?:{1})?{2}'.format(prefix, '|'.join(body), suffix).replace('(?:)?', '')
            else:
                self._re = '{0}(?:{1}){2}'.format(prefix, '|'.join(body), suffix)
        else:
            self._re = self._alternation_regex(strings)

    @staticmethod
    def _alternation_regex(sample_strings):
        alternation = '|'.join(sample_strings)
        return '(?:{})'.format(alternation)

    @staticmethod
    def _get_common_prefix(sample_strings):
        return os.path.commonprefix(sample_strings)

    @staticmethod
    def _get_common_suffix(list_of_strings):
        reverse = [s[::-1] for s in list_of_strings]
        return Factorizer._get_common_prefix(reverse[::-1])

    @staticmethod
    def _slice_str(string, prefix_length, suffix_length):
        return string[prefix_length:len(string) - suffix_length]
