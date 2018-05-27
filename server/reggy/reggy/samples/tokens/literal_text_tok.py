from enum import Enum


class LiteralTextTok(Enum):
    CASE_SENSITIVE             = 1
    CASE_INSENSITIVE           = 2
    MATCH_ALL_EXCEPT_SPECIFIED = 3
