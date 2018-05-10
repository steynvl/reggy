from enum import Enum


class RegexEndInfo(Enum):
    ANYWHERE    = 1
    END_OF_TEXT = 2
    END_OF_LINE = 3
    END_OF_WORD = 4
