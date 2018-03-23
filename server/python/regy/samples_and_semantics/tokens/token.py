from enum import Enum


class Token(Enum):
    GENERAL_REGEX_INFO         = 1
    TARGET_LANGUAGE            = 2
    REGEX_START_INFO           = 3
    REGEX_END_INFO             = 4

    SAMPLE_STRINGS_INFO        = 5
    MARKER_TYPE                = 6

    MARKED_TEXT_STRINGS        = 7

    MARKER_INFO                = 8

    LOWERCASE_LETTERS          = 9
    UPPERCASE_LETTERS          = 10
    CONTAINS_DIGIT             = 11
    MATCH_ALL_EXCEPT_SPECIFIED = 12

    DIGITS                    = 13
    MINUS_INFO                 = 14
    INCLUDE_MINUS              = 15
    INCLUDE_OPTIONAL_MINUS     = 16

    REPEAT_INFO                = 17
    REPEAT_RANGE               = 18
    REPEAT_START               = 19
    REPEAT_END                 = 20

    ESCAPED_STRINGS            = 21

    CONTROL_CHARACTERS         = 22
