from reggy.samples.tokens import Target
from reggy.samples.tokens.basic_characters_tok import BasicCharactersTok

basic_characters_to_re = {

    Target.JAVA: {
        BasicCharactersTok.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersTok.DIGITS                     : '\\\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS    : '\\\\p{Punct}',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersTok.WHITE_SPACE                : '\\\\s',
        BasicCharactersTok.LINE_BREAKS                : '\\\\r\\\\n',
    },

    Target.PERL: {
        BasicCharactersTok.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersTok.DIGITS                     : '\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS    : '\\p{PosixPunct}',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersTok.WHITE_SPACE                : '\\s',
        BasicCharactersTok.LINE_BREAKS                : '\\r\\n',
    },

    Target.POSIX: {
        BasicCharactersTok.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersTok.DIGITS                     : '\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS    : '\\p{P}',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersTok.WHITE_SPACE                : '\\s',
        BasicCharactersTok.LINE_BREAKS                : '\\r\\n',
    },

    Target.PYTHON: {
        BasicCharactersTok.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersTok.DIGITS                     : '\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS    : '\\p{P}',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersTok.WHITE_SPACE                : '\\s',
        BasicCharactersTok.LINE_BREAKS                : '\\r\\n',
    },

    Target.JAVASCRIPT: {
        BasicCharactersTok.LOWER_CASE_LETTERS: 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS: 'A-Z',
        BasicCharactersTok.DIGITS: '\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS: '[!"\#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~]',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED: '^',
        BasicCharactersTok.WHITE_SPACE: '\\s',
        BasicCharactersTok.LINE_BREAKS: '\\r\\n',
    },

    Target.PHP: {
      BasicCharactersTok.LOWER_CASE_LETTERS: 'a-z',
      BasicCharactersTok.UPPER_CASE_LETTERS: 'A-Z',
      BasicCharactersTok.DIGITS: '\\d',
      BasicCharactersTok.PUNCTUATION_AND_SYMBOLS: '\\p{P}',
      BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED: '^',
      BasicCharactersTok.WHITE_SPACE: '\\s',
      BasicCharactersTok.LINE_BREAKS: '\\r\\n',
    },

    Target.GOLANG: {
      BasicCharactersTok.LOWER_CASE_LETTERS: 'a-z',
      BasicCharactersTok.UPPER_CASE_LETTERS: 'A-Z',
      BasicCharactersTok.DIGITS: '\\\\d',
      BasicCharactersTok.PUNCTUATION_AND_SYMBOLS: '\\\\p{P}',
      BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED: '^',
      BasicCharactersTok.WHITE_SPACE: '\\\\s',
      BasicCharactersTok.LINE_BREAKS: '\\\\r\\\\n',
    },

    Target.RUST: {
        BasicCharactersTok.LOWER_CASE_LETTERS: 'a-z',
        BasicCharactersTok.UPPER_CASE_LETTERS: 'A-Z',
        BasicCharactersTok.DIGITS: '\\d',
        BasicCharactersTok.PUNCTUATION_AND_SYMBOLS: '\\p{P}',
        BasicCharactersTok.MATCH_ALL_EXCEPT_SPECIFIED: '^',
        BasicCharactersTok.WHITE_SPACE: '\\s',
        BasicCharactersTok.LINE_BREAKS: '\\r\\n',
    }

}
