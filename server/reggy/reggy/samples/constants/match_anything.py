from reggy.samples.tokens import Target
from reggy.samples.tokens.match_anything_tok import MatchAnythingTok

basic_char_to_tok = {
    'lowerCaseLetters'     : MatchAnythingTok.LOWER_CASE_LETTERS,
    'upperCaseLetters'     : MatchAnythingTok.UPPER_CASE_LETTERS,
    'digits'               : MatchAnythingTok.DIGITS,
    'punctuationAndSymbols': MatchAnythingTok.PUNCTUATION_AND_SYMBOLS,
    'whiteSpace'           : MatchAnythingTok.WHITESPACE,
    'lineBreaks'           : MatchAnythingTok.LINE_BREAKS
}

basic_char_to_re = {

    Target.JAVA: {
        MatchAnythingTok.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnythingTok.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnythingTok.DIGITS                 : '\\\\d',
        MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\\\p{Punct}',
        MatchAnythingTok.WHITESPACE             : '\\\\s',
        MatchAnythingTok.LINE_BREAKS            : '\\\\r\\\\n'
    },

    Target.PERL: {
        MatchAnythingTok.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnythingTok.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnythingTok.DIGITS                 : '\\d',
        MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\p{PosixPunct}',
        MatchAnythingTok.WHITESPACE             : '\\s',
        MatchAnythingTok.LINE_BREAKS            : '\\r\\n'
    },

    Target.POSIX: {
        MatchAnythingTok.LOWER_CASE_LETTERS     : 'a-z',
        MatchAnythingTok.UPPER_CASE_LETTERS     : 'A-Z',
        MatchAnythingTok.DIGITS                 : '\\d',
        MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\p{PosixPunct}',
        MatchAnythingTok.WHITESPACE             : '\\s',
        MatchAnythingTok.LINE_BREAKS            : '\\r\\n'
    },

    Target.PYTHON: {
        MatchAnythingTok.LOWER_CASE_LETTERS: 'a-z',
        MatchAnythingTok.UPPER_CASE_LETTERS: 'A-Z',
        MatchAnythingTok.DIGITS: '\\d',
        MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\p{P}',
        MatchAnythingTok.WHITESPACE: '\\s',
        MatchAnythingTok.LINE_BREAKS: '\\r\\n'
    },

    Target.JAVASCRIPT: {
        MatchAnythingTok.LOWER_CASE_LETTERS: 'a-z',
        MatchAnythingTok.UPPER_CASE_LETTERS: 'A-Z',
        MatchAnythingTok.DIGITS: '\\d',
        MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '[!"\#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]',
        MatchAnythingTok.WHITESPACE: '\\s',
        MatchAnythingTok.LINE_BREAKS: '\\r\\n'
    },

    Target.PHP: {
      MatchAnythingTok.LOWER_CASE_LETTERS: 'a-z',
      MatchAnythingTok.UPPER_CASE_LETTERS: 'A-Z',
      MatchAnythingTok.DIGITS: '\\d',
      MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\p{P}',
      MatchAnythingTok.WHITESPACE: '\\s',
      MatchAnythingTok.LINE_BREAKS: '\\r\\n'
    },

    Target.GOLANG: {
      MatchAnythingTok.LOWER_CASE_LETTERS: 'a-z',
      MatchAnythingTok.UPPER_CASE_LETTERS: 'A-Z',
      MatchAnythingTok.DIGITS: '\\\\d',
      MatchAnythingTok.PUNCTUATION_AND_SYMBOLS: '\\\\p{P}',
      MatchAnythingTok.WHITESPACE: '\\\\s',
      MatchAnythingTok.LINE_BREAKS: '\\\\r\\\\n'
    }

}

can_span_across_lines = {
    Target.JAVA : '\\\\r\\\\n',
    Target.PERL : '\\r\\n',
    Target.POSIX: '\\r\\n'
}
