from enum import Enum


class ListOfLiteralTextTok(Enum):
    LITERAL_TEXT                    = 1
    MATCH_ANYTHING_EXCEPT_SPECIFIED = 2
    CASE_INSENSITIVE                = 3
