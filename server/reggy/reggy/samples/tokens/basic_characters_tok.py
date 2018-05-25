from enum import Enum


class BasicCharactersTok(Enum):
    CASE_INSENSITIVE           = 1
    LOWER_CASE_LETTERS         = 2
    UPPER_CASE_LETTERS         = 3
    DIGITS                     = 4
    PUNCTUATION_AND_SYMBOLS    = 5
    MATCH_ALL_EXCEPT_SPECIFIED = 6
    WHITE_SPACE                = 7
    LINE_BREAKS                = 8
    INDIVIDUAL_CHARACTERS      = 9
