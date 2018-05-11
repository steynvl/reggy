from enum import Enum


class MarkerType(Enum):
    LITERAL_TEXT         = 1
    BASIC_CHARACTERS     = 2
    DIGITS               = 3
    CONTROL_CHARACTERS   = 4
    UNICODE_CHARACTERS   = 5
    MATCH_ANYTHING       = 6
    LIST_OF_LITERAL_TEXT = 7
    NUMBERS              = 8
