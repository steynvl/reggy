from enum import Enum


class RegexExtraInfo(Enum):
    ANYWHERE         = 1
    START_OF_TEXT    = 2
    START_OF_LINE    = 3
    START_OF_WORD    = 4
    START_OF_ATTEMPT = 5
    END_OF_TEXT      = 6
    END_OF_LINE      = 7
    END_OF_WORD      = 8
