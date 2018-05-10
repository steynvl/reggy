from collections import deque
import re

from regy.samples.mapper.repeat_helper import repeat_info_to_regex
from regy.samples.models.numbers_info import NumbersInfo
from regy.samples.tokens.numbers import Numbers
from regy.samples.utils.numbers_helper import const_to_re
from regy.samples.utils.numeric_range_generator import NumericRangeGenerator


class MapNumbers:

    def __init__(self, info, target_lang):
        self._currency_codes = re.compile(r'^[A-Z]{3}(?:;[A-Z]{3})*$')
        self._info = info
        self._target_lang = target_lang
        self._const_to_re = const_to_re[target_lang]
        self._re = deque()
        self._map_info()

    def get_re(self):
        return self._re

    def _map_info(self):
        numbers = self._info[Numbers.MODEL]
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

        if numbers.min_nr_of_decimals != '' and numbers.max_nr_of_decimals != '':
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
        regex = []
        if start >= 0 and end >= 0:
            regex.append(NumericRangeGenerator(start, end, insert_minus=False).get_regex())

        elif start < 0 and end >= 0:
            regex.append(NumericRangeGenerator(1, abs(start), insert_minus=True).get_regex())
            if end == 0:
                regex.append('0')
            else:
                regex.append(NumericRangeGenerator(0, end, insert_minus=False).get_regex())

        else:
            regex.append(NumericRangeGenerator(abs(end), abs(start), insert_minus=True).get_regex())

        if len(regex) == 1:
            self._re.append('|'.join(regex))
        else:
            self._re.append('(?:{})'.format('|'.join(regex)))

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
