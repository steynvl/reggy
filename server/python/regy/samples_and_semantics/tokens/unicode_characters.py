from enum import Enum
from regy.samples_and_semantics.tokens import TargetLanguage


class UnicodeCharacters(Enum):

    UPPERCASE_LETTERS = 1
    LOWERCASE_LETTERS = 2
    MODIFIER_LETTERS  = 3
    NON_SPACING_MARKS = 4
    ENCLOSING_MARKS   = 5


unicode_char_to_re = {

    TargetLanguage.JAVA: {
        UnicodeCharacters.UPPERCASE_LETTERS: '\\\\u0041-\\\\u005A',
        UnicodeCharacters.LOWERCASE_LETTERS: '\\\\u0061-\\\\u007A',
        UnicodeCharacters.MODIFIER_LETTERS : '\\\\u02B0-\\\\uFF9F',
        UnicodeCharacters.NON_SPACING_MARKS: '\\\\u0300-\\\\uFE2F',
        UnicodeCharacters.ENCLOSING_MARKS:   '\\\\u0488-\\\\uA672'
    },

    TargetLanguage.PERL: {
        UnicodeCharacters.UPPERCASE_LETTERS: '\\x{0041}-\\x{005A}',
        UnicodeCharacters.LOWERCASE_LETTERS: '\\x{0061}-\\x{007A}',
        UnicodeCharacters.MODIFIER_LETTERS : '\\x{02B0}-\\x{FF9F}',
        UnicodeCharacters.NON_SPACING_MARKS: '\\x{0300}-\\x{FE2F}',
        UnicodeCharacters.ENCLOSING_MARKS:   '\\x{0488}-\\x{A672}'
    },

    TargetLanguage.POSIX: {

    }


}