from enum import Enum


class UnicodeCharactersTok(Enum):
    LOWERCASE_LETTERS       = 1
    UPPERCASE_LETTERS       = 2
    TITLE_CASE_LETTERS      = 3
    CASED_LETTERS           = 4
    MODIFIER_LETTERS        = 5
    OTHER_LETTERS           = 6

    NON_SPACING_MARKS       = 7
    SPACING_COMBINING_MARKS = 8
    ENCLOSING_MARKS         = 9

    SPACE_SEPARATORS        = 10
    LINE_SEPARATORS         = 11
    PARAGRAPH_SEPARATORS    = 12

    MATH_SYMBOLS            = 13
    CURRENCY_SYMBOLS        = 14
    MODIFIER_SYMBOLS        = 15
    OTHER_SYMBOLS           = 16

    DECIMAL_DIGIT_NUMBERS   = 17
    LETTER_NUMBERS          = 18
    OTHER_NUMBERS           = 19

    DASH_PUNCTUATION        = 20
    OPEN_PUNCTUATION        = 21
    CLOSE_PUNCTUATION       = 22
    INITIAL_PUNCTUATION     = 23
    FINAL_PUNCTUATION       = 24
    CONNECTOR_PUNCTUATION   = 25
    OTHER_PUNCTUATION       = 26

    CONTROL_CHARACTERS      = 27
    FORMAT_CHARACTERS       = 28
    PRIVATE_USE_CHARACTERS  = 29
    SURROGATE_CHARACTERS    = 30
    UNASSIGNED_CHARACTERS   = 31