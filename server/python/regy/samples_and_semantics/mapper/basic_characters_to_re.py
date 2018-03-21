from regy.samples_and_semantics.tokens import TargetLanguage
from regy.samples_and_semantics.tokens.basic_characters_info import BasicCharactersInfo

basic_characters_to_re = {

    TargetLanguage.JAVA: {
        BasicCharactersInfo.LOWER_CASE_LETTERS         : 'a-z',
        BasicCharactersInfo.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersInfo.DIGITS                     : '\\\\d',
        BasicCharactersInfo.PUNCTUATION_AND_SYMBOLS    : '\\\\p{Punct}',
        BasicCharactersInfo.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersInfo.WHITE_SPACE                : '\\\\s',
        BasicCharactersInfo.LINE_BREAKS                : '\\\\r\\\\n',
    },

    TargetLanguage.PERL: {
        BasicCharactersInfo.LOWER_CASE_LETTERS         : '[a-z]',
        BasicCharactersInfo.UPPER_CASE_LETTERS         : 'A-Z',
        BasicCharactersInfo.DIGITS                     : '\\d',
        BasicCharactersInfo.PUNCTUATION_AND_SYMBOLS    : '\\p{PosixPunct}',
        BasicCharactersInfo.MATCH_ALL_EXCEPT_SPECIFIED : '^',
        BasicCharactersInfo.WHITE_SPACE                : '\\s',
        BasicCharactersInfo.LINE_BREAKS                : '\\r\\n',
    },

    TargetLanguage.POSIX: {

    }

}
