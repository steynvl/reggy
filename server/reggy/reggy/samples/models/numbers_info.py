from reggy.samples.parser.repetition_info import RepetitionInfo


class NumbersInfo:

    def __init__(self, marker_id, info):
        self.marker_id = marker_id
        self.min_val_of_int_part              = info['minValOfIntPart']
        self.max_val_of_int_part              = info['maxValOfIntPart']
        self.decimal_separator                = info['decimalSeparator']
        self.min_nr_of_decimals               = info['minNrOfDecimals']
        self.max_nr_of_decimals               = info['maxNrOfDecimals']
        self.thousand_separator               = info['thousandSeparator']
        self.code_position                    = info['codePosition']
        self.currency_sign                    = info['currencySign']
        self.currency_codes                   = info['currencyCodes']
        self.limit_integer_part               = info['limitIntegerPart']
        self.allow_plus_sign                  = info['allowPlusSign']
        self.allow_minus_sign                 = info['allowMinusSign']
        self.sign_is_required                 = info['signIsRequired']
        self.whitespace_allowed_after_sign    = info['whitespaceAllowedAfterSign']
        self.thousand_separators_are_required = info['thousandSeparatorsAreRequired']
        self.allow_leading_zeros              = info['allowLeadingZeros']
        self.require_integer_part             = info['requireIntegerPart']
        self.allow_exponent                   = info['allowExponent']
        self.currency_sign_or_code_required   = info['currencySignOrCodeRequired']

        self.repetition_info = RepetitionInfo()
