from enum import Enum


class MarkerType(Enum):
    LITERAL_TEXT       = 1
    BASIC_CHARACTERS   = 2
    DIGITS             = 3
    CONTROL_CHARACTERS = 4
    UNICODE_CHARACTERS = 5
