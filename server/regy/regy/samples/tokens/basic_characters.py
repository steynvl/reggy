from enum import Enum
from regy.samples.tokens import Target


class BasicCharacters(Enum):
    CASE_INSENSITIVE           = 1
    LOWER_CASE_LETTERS         = 2
    UPPER_CASE_LETTERS         = 3
    DIGITS                     = 4
    PUNCTUATION_AND_SYMBOLS    = 5
    MATCH_ALL_EXCEPT_SPECIFIED = 6
    WHITE_SPACE                = 7
    LINE_BREAKS                = 8
    INDIVIDUAL_CHARACTERS      = 9

basic_characters_to_re = {

    Target.JAVA: {
        BasicCharacters.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharacters.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharacters.DIGITS                     : '\\\\d',
        BasicCharacters.PUNCTUATION_AND_SYMBOLS    : '\\\\p{Punct}',
        BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharacters.WHITE_SPACE                : '\\\\s',
        BasicCharacters.LINE_BREAKS                : '\\\\r\\\\n',
    },

    Target.PERL: {
        BasicCharacters.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharacters.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharacters.DIGITS                     : '\\d',
        BasicCharacters.PUNCTUATION_AND_SYMBOLS    : '\\p{PosixPunct}',
        BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharacters.WHITE_SPACE                : '\\s',
        BasicCharacters.LINE_BREAKS                : '\\r\\n',
    },

    Target.POSIX: {
        BasicCharacters.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharacters.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharacters.DIGITS                     : '\\d',
        BasicCharacters.PUNCTUATION_AND_SYMBOLS    : '\\p{P}',
        BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharacters.WHITE_SPACE                : '\\s',
        BasicCharacters.LINE_BREAKS                : '\\r\\n',
    }

}
