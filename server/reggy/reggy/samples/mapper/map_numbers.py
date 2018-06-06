from collections import deque
import re

from reggy.samples.mapper.repeat_helper import repeat_info_to_regex
from reggy.samples.models.numbers_info import NumbersInfo
from reggy.samples.constants.numbers import const_to_re
from reggy.samples.utils.numeric_range import NumericRange


class MapNumbers:

    def __init__(self, info: NumbersInfo, target_lang):
        self._currency_codes = re.compile(r'^[A-Z]{3}(?:;[A-Z]{3})*$')
        self._info = info
        self._target_lang = target_lang
        self._const_to_re = const_to_re[target_lang]
        self._re = deque()
        self._map_info()

    def get_re(self):
        return ''.join(self._re)

    def _map_info(self):
        numbers = self._info
        contains_currency = False

        if numbers.currency_sign != 'None' \
                or self._currency_codes.match(numbers.currency_codes) is not None:
            contains_currency = True
            curr_str = self._build_currency(numbers)

        if contains_currency and 'Before' in numbers.code_position:
            if numbers.currency_sign_or_code_required:
                self._re.append('{} *'.format(curr_str))
            else:
                self._re.append('{}? *'.format(curr_str))

        if (numbers.allow_plus_sign or numbers.allow_minus_sign) and not numbers.limit_integer_part:
            if numbers.allow_plus_sign and numbers.allow_minus_sign:
                self._re.append('[{}-]'.format(self._const_to_re['plusSign']))
            if numbers.allow_plus_sign:
                self._re.append(self._const_to_re['plusSign'])
            elif numbers.allow_minus_sign:
                self._re.append('-')

            if not numbers.sign_is_required:
                self._re.append('?')

            if numbers.whitespace_allowed_after_sign:
                self._re.append(' *')

        if numbers.allow_leading_zeros:
            self._re.append('0*')

        if numbers.limit_integer_part:
            self._build_limited_integer_part(numbers.min_val_of_int_part, numbers.max_val_of_int_part)
        elif numbers.thousand_separators_are_required:
            self._re.append('[0-9]{1,3}(?:,[0-9]{3})*')
        else:
            self._re.append(self._const_to_re['number'])
            self._re.append('+' if numbers.require_integer_part else '*')

        if numbers.min_nr_of_decimals != 0 or numbers.max_nr_of_decimals != 0:
            self._build_decimal_part(numbers)

        if numbers.allow_exponent:
            self._re.append(self._const_to_re['allowExponent'])

        if contains_currency and 'After' in numbers.code_position:
            if numbers.currency_sign_or_code_required:
                self._re.append(' *{}'.format(curr_str))
            else:
                self._re.append(' *{}?'.format(curr_str))

        repeat_info = repeat_info_to_regex(self._info)
        self._re.append(repeat_info)

    def _build_limited_integer_part(self, start, end):
        self._re.append(NumericRange(start, end).get_re())

    def _build_currency(self, numbers_info: NumbersInfo):
        currs = deque()
        if self._currency_codes.match(numbers_info.currency_codes) is not None:
            currs.extend(self._parse_currency_codes(numbers_info.currency_codes))

        if numbers_info.currency_sign != 'None':
            currs.appendleft(self._const_to_re['currencySign'][numbers_info.currency_sign])

        return '(?:{})'.format(currs[0] if len(currs) == 1 else '|'.join(currs))

    def _build_decimal_part(self, numbers_info: NumbersInfo):
        decimal_separator_to_re = self._const_to_re['decimalSeparator']

        if numbers_info.min_nr_of_decimals == numbers_info.max_nr_of_decimals:
            self._re.append('(?:%s%s{%s})?' % (decimal_separator_to_re[numbers_info.decimal_separator],
                                               self._const_to_re['number'],
                                               numbers_info.min_nr_of_decimals))
        else:
            self._re.append('(%s%s{%s,%s})?' % (decimal_separator_to_re[numbers_info.decimal_separator],
                                                self._const_to_re['number'],
                                                numbers_info.min_nr_of_decimals,
                                                numbers_info.max_nr_of_decimals))

    @staticmethod
    def _parse_currency_codes(values):
        semicolons = re.compile(r'(?<![\\]);')
        field = filter(lambda u: u != '', re.split(semicolons, values))
        return [i.replace('\\;', ';') for i in field]
