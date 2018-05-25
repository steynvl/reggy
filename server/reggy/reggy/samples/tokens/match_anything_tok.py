from enum import Enum


class MatchAnythingTok(Enum):
    SPECIFIC_CHARACTERS     = 1
    SPECIFIC_CHARACTER      = 2
    BASIC_CHARACTERS        = 3
    NOTHING                 = 4
    CAN_SPAN_ACROSS_LINES   = 5
    CASE_INSENSITIVE        = 6

    LOWER_CASE_LETTERS      = 7
    UPPER_CASE_LETTERS      = 8
    DIGITS                  = 9
    PUNCTUATION_AND_SYMBOLS = 10
    WHITESPACE              = 11
    LINE_BREAKS             = 12
