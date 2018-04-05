from enum import Enum

from regy.samples_and_semantics.tokens import Target


class MatchAnything(Enum):

    SPECIFIC_CHARACTERS     = 1
    SPECIFIC_CHARACTER      = 2
    BASIC_CHARACTERS        = 3
    NOTHING                 = 4
    CAN_SPAN_ACROSS_LINES   = 5

    LOWER_CASE_LETTERS      = 6
    UPPER_CASE_LETTERS      = 7
    DIGITS                  = 8
    PUNCTUATION_AND_SYMBOLS = 9
    WHITESPACE              = 10
    LINE_BREAKS             = 11

basic_char_to_tok = {
    'lowerCaseLetters'     : MatchAnything.LOWER_CASE_LETTERS,
    'upperCaseLetters'     : MatchAnything.UPPER_CASE_LETTERS,
    'digits'               : MatchAnything.DIGITS,
    'punctuationAndSymbols': MatchAnything.PUNCTUATION_AND_SYMBOLS,
    'whiteSpace'           : MatchAnything.WHITESPACE,
    'lineBreaks'           : MatchAnything.LINE_BREAKS
}

basic_char_to_re = {

    Target.JAVA: {
        MatchAnything.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnything.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnything.DIGITS                 : '\\\\d',
        MatchAnything.PUNCTUATION_AND_SYMBOLS: '\\\\p{Punct}',
        MatchAnything.WHITESPACE             : '\\\\s',
        MatchAnything.LINE_BREAKS            : '\\\\r\\\\n'
    },

    Target.PERL: {
        MatchAnything.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnything.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnything.DIGITS                 : '\\d',
        MatchAnything.PUNCTUATION_AND_SYMBOLS: '\\p{PosixPunct}',
        MatchAnything.WHITESPACE             : '\\s',
        MatchAnything.LINE_BREAKS            : '\\r\\n'
    },

    Target.POSIX: {
        MatchAnything.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnything.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnything.DIGITS                 : '\\d',
        MatchAnything.PUNCTUATION_AND_SYMBOLS: '\\p{PosixPunct}',
        MatchAnything.WHITESPACE             : '\\s',
        MatchAnything.LINE_BREAKS            : '\\r\\n'
    }

}

can_span_across_lines = {
    Target.JAVA : '\\\\r\\\\n',
    Target.PERL : '\\r\\n',
    Target.POSIX: '\\r\\n'
}
