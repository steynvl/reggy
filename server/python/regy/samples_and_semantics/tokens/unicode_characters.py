from enum import Enum
from regy.samples_and_semantics.tokens import Target


class UnicodeCharacters(Enum):

    LOWERCASE_LETTERS       = 1
    UPPERCASE_LETTERS       = 2
    TITLE_CASE_LETTERS      = 3
    CASED_LETTERS           = 4
    MODIFIER_LETTERS        = 5
    OTHER_LETTERS           = 6

    NON_SPACING_MARKS       = 7
    SPACING_COMBINING_MARKS = 8
    ENCLOSING_MARKS         = 9

    SPACE_SEPARATORS        = 10
    LINE_SEPARATORS         = 11
    PARAGRAPH_SEPARATORS    = 12

    MATH_SYMBOLS            = 13
    CURRENCY_SYMBOLS        = 14
    MODIFIER_SYMBOLS        = 15
    OTHER_SYMBOLS           = 16

    DECIMAL_DIGIT_NUMBERS   = 17
    LETTER_NUMBERS          = 18
    OTHER_NUMBERS           = 19

    DASH_PUNCTUATION        = 20
    OPEN_PUNCTUATION        = 21
    CLOSE_PUNCTUATION       = 22
    INITIAL_PUNCTUATION     = 23
    FINAL_PUNCTUATION       = 24
    CONNECTOR_PUNCTUATION   = 25
    OTHER_PUNCTUATION       = 26

    CONTROL_CHARACTERS      = 27
    FORMAT_CHARACTERS       = 28
    PRIVATE_USE_CHARACTERS  = 29
    SURROGATE_CHARACTERS    = 30
    UNASSIGNED_CHARACTERS   = 31


unicode_chars = [
    'lowercaseLetters', 'uppercaseLetters', 'titleCaseLetters',
    'casedLetters', 'modifierLetters', 'otherLetters',
    'nonSpacingMarks', 'spacingCombiningMarks', 'enclosingMarks',
    'spaceSeparators', 'lineSeparators', 'paragraphSeparators',
    'mathSymbols', 'currencySymbols', 'modifierSymbols',
    'otherSymbols', 'decimalDigitNumbers', 'letterNumbers',
    'otherNumbers', 'dashPunctuation', 'openPunctuation',
    'closePunctuation', 'initialPunctuation', 'finalPunctuation',
    'connectorPunctuation', 'otherPunctuation', 'controlCharacters',
    'formatCharacters', 'privateUseCharacters', 'surrogateCharacters',
    'unassignedCharacters'
]

unicode_char_to_token = {
    'lowercaseLetters'     : UnicodeCharacters.LOWERCASE_LETTERS,
    'uppercaseLetters'     : UnicodeCharacters.UPPERCASE_LETTERS,
    'titleCaseLetters'     : UnicodeCharacters.TITLE_CASE_LETTERS,
    'casedLetters'         : UnicodeCharacters.CASED_LETTERS,
    'modifierLetters'      : UnicodeCharacters.MODIFIER_LETTERS,
    'otherLetters'         : UnicodeCharacters.OTHER_LETTERS,
    'nonSpacingMarks'      : UnicodeCharacters.NON_SPACING_MARKS,
    'spacingCombiningMarks': UnicodeCharacters.SPACING_COMBINING_MARKS,
    'enclosingMarks'       : UnicodeCharacters.ENCLOSING_MARKS,
    'spaceSeparators'      : UnicodeCharacters.SPACE_SEPARATORS,
    'lineSeparators'       : UnicodeCharacters.LINE_SEPARATORS,
    'paragraphSeparators'  : UnicodeCharacters.PARAGRAPH_SEPARATORS,
    'mathSymbols'          : UnicodeCharacters.MATH_SYMBOLS,
    'currencySymbols'      : UnicodeCharacters.CURRENCY_SYMBOLS,
    'modifierSymbols'      : UnicodeCharacters.MODIFIER_SYMBOLS,
    'otherSymbols'         : UnicodeCharacters.OTHER_SYMBOLS,
    'decimalDigitNumbers'  : UnicodeCharacters.DECIMAL_DIGIT_NUMBERS,
    'letterNumbers'        : UnicodeCharacters.LETTER_NUMBERS,
    'otherNumbers'         : UnicodeCharacters.OTHER_NUMBERS,
    'dashPunctuation'      : UnicodeCharacters.DASH_PUNCTUATION,
    'openPunctuation'      : UnicodeCharacters.OPEN_PUNCTUATION,
    'closePunctuation'     : UnicodeCharacters.CLOSE_PUNCTUATION,
    'initialPunctuation'   : UnicodeCharacters.INITIAL_PUNCTUATION,
    'finalPunctuation'     : UnicodeCharacters.FINAL_PUNCTUATION,
    'connectorPunctuation' : UnicodeCharacters.CONNECTOR_PUNCTUATION,
    'otherPunctuation'     : UnicodeCharacters.OPEN_PUNCTUATION,
    'controlCharacters'    : UnicodeCharacters.CONTROL_CHARACTERS,
    'formatCharacters'     : UnicodeCharacters.FORMAT_CHARACTERS,
    'privateUseCharacters' : UnicodeCharacters.PRIVATE_USE_CHARACTERS,
    'surrogateCharacters'  : UnicodeCharacters.SURROGATE_CHARACTERS,
    'unassignedCharacters' : UnicodeCharacters.UNASSIGNED_CHARACTERS
}

unicode_char_to_re = {

    Target.JAVA: {
        UnicodeCharacters.LOWERCASE_LETTERS      : '\\\\p{Ll}',
        UnicodeCharacters.UPPERCASE_LETTERS      : '\\\\p{Lu}',
        UnicodeCharacters.TITLE_CASE_LETTERS     : '\\\\p{Lt}',
        UnicodeCharacters.CASED_LETTERS          : '\\\\p{L}',
        UnicodeCharacters.MODIFIER_LETTERS       : '\\\\p{Lm}',
        UnicodeCharacters.OTHER_LETTERS          : '\\\\p{Lo}',
        UnicodeCharacters.NON_SPACING_MARKS      : '\\\\p{Mn}',
        UnicodeCharacters.SPACING_COMBINING_MARKS: '\\\\p{Mc}',
        UnicodeCharacters.ENCLOSING_MARKS        : '\\\\p{Me}',
        UnicodeCharacters.SPACE_SEPARATORS       : '\\\\p{Zs}',
        UnicodeCharacters.LINE_SEPARATORS        : '\\\\p{Zl}',
        UnicodeCharacters.PARAGRAPH_SEPARATORS   : '\\\\p{Zp}',
        UnicodeCharacters.MATH_SYMBOLS           : '\\\\p{Sm}',
        UnicodeCharacters.CURRENCY_SYMBOLS       : '\\\\p{Sc}',
        UnicodeCharacters.MODIFIER_SYMBOLS       : '\\\\p{Sk}',
        UnicodeCharacters.OTHER_SYMBOLS          : '\\\\p{So}',
        UnicodeCharacters.DECIMAL_DIGIT_NUMBERS  : '\\\\p{Nd}',
        UnicodeCharacters.LETTER_NUMBERS         : '\\\\p{Nl}',
        UnicodeCharacters.OTHER_NUMBERS          : '\\\\p{No}',
        UnicodeCharacters.DASH_PUNCTUATION       : '\\\\p{Pd}',
        UnicodeCharacters.OPEN_PUNCTUATION       : '\\\\p{Ps}',
        UnicodeCharacters.CLOSE_PUNCTUATION      : '\\\\p{Pe}',
        UnicodeCharacters.INITIAL_PUNCTUATION    : '\\\\p{Pi}',
        UnicodeCharacters.FINAL_PUNCTUATION      : '\\\\p{Pf}',
        UnicodeCharacters.CONNECTOR_PUNCTUATION  : '\\\\p{Pc}',
        UnicodeCharacters.OTHER_PUNCTUATION      : '\\\\p{Po}',
        UnicodeCharacters.CONTROL_CHARACTERS     : '\\\\p{Cc}',
        UnicodeCharacters.FORMAT_CHARACTERS      : '\\\\p{Cf}',
        UnicodeCharacters.PRIVATE_USE_CHARACTERS : '\\\\p{Co}',
        UnicodeCharacters.SURROGATE_CHARACTERS   : '\\\\p{Cs}',
        UnicodeCharacters.UNASSIGNED_CHARACTERS  : '\\\\p{Cn}'
    },

    Target.PERL: {
        UnicodeCharacters.LOWERCASE_LETTERS      : '\\p{Ll}',
        UnicodeCharacters.UPPERCASE_LETTERS      : '\\p{Lu}',
        UnicodeCharacters.TITLE_CASE_LETTERS     : '\\p{Lt}',
        UnicodeCharacters.CASED_LETTERS          : '\\p{L}',
        UnicodeCharacters.MODIFIER_LETTERS       : '\\p{Lm}',
        UnicodeCharacters.OTHER_LETTERS          : '\\p{Lo}',
        UnicodeCharacters.NON_SPACING_MARKS      : '\\p{Mn}',
        UnicodeCharacters.SPACING_COMBINING_MARKS: '\\p{Mc}',
        UnicodeCharacters.ENCLOSING_MARKS        : '\\p{Me}',
        UnicodeCharacters.SPACE_SEPARATORS       : '\\p{Zs}',
        UnicodeCharacters.LINE_SEPARATORS        : '\\p{Zl}',
        UnicodeCharacters.PARAGRAPH_SEPARATORS   : '\\p{Zp}',
        UnicodeCharacters.MATH_SYMBOLS           : '\\p{Sm}',
        UnicodeCharacters.CURRENCY_SYMBOLS       : '\\p{Sc}',
        UnicodeCharacters.MODIFIER_SYMBOLS       : '\\p{Sk}',
        UnicodeCharacters.OTHER_SYMBOLS          : '\\p{So}',
        UnicodeCharacters.DECIMAL_DIGIT_NUMBERS  : '\\p{Nd}',
        UnicodeCharacters.LETTER_NUMBERS         : '\\p{Nl}',
        UnicodeCharacters.OTHER_NUMBERS          : '\\p{No}',
        UnicodeCharacters.DASH_PUNCTUATION       : '\\p{Pd}',
        UnicodeCharacters.OPEN_PUNCTUATION       : '\\p{Ps}',
        UnicodeCharacters.CLOSE_PUNCTUATION      : '\\p{Pe}',
        UnicodeCharacters.INITIAL_PUNCTUATION    : '\\p{Pi}',
        UnicodeCharacters.FINAL_PUNCTUATION      : '\\p{Pf}',
        UnicodeCharacters.CONNECTOR_PUNCTUATION  : '\\p{Pc}',
        UnicodeCharacters.OTHER_PUNCTUATION      : '\\p{Po}',
        UnicodeCharacters.CONTROL_CHARACTERS     : '\\p{Cc}',
        UnicodeCharacters.FORMAT_CHARACTERS      : '\\p{Cf}',
        UnicodeCharacters.PRIVATE_USE_CHARACTERS : '\\p{Co}',
        UnicodeCharacters.SURROGATE_CHARACTERS   : '\\p{Cs}',
        UnicodeCharacters.UNASSIGNED_CHARACTERS  : '\\p{Cn}'
    },

    Target.POSIX: {
        UnicodeCharacters.LOWERCASE_LETTERS      : '\\p{Ll}',
        UnicodeCharacters.UPPERCASE_LETTERS      : '\\p{Lu}',
        UnicodeCharacters.TITLE_CASE_LETTERS     : '\\p{Lt}',
        UnicodeCharacters.CASED_LETTERS          : '\\p{L}',
        UnicodeCharacters.MODIFIER_LETTERS       : '\\p{Lm}',
        UnicodeCharacters.OTHER_LETTERS          : '\\p{Lo}',
        UnicodeCharacters.NON_SPACING_MARKS      : '\\p{Mn}',
        UnicodeCharacters.SPACING_COMBINING_MARKS: '\\p{Mc}',
        UnicodeCharacters.ENCLOSING_MARKS        : '\\p{Me}',
        UnicodeCharacters.SPACE_SEPARATORS       : '\\p{Zs}',
        UnicodeCharacters.LINE_SEPARATORS        : '\\p{Zl}',
        UnicodeCharacters.PARAGRAPH_SEPARATORS   : '\\p{Zp}',
        UnicodeCharacters.MATH_SYMBOLS           : '\\p{Sm}',
        UnicodeCharacters.CURRENCY_SYMBOLS       : '\\p{Sc}',
        UnicodeCharacters.MODIFIER_SYMBOLS       : '\\p{Sk}',
        UnicodeCharacters.OTHER_SYMBOLS          : '\\p{So}',
        UnicodeCharacters.DECIMAL_DIGIT_NUMBERS  : '\\p{Nd}',
        UnicodeCharacters.LETTER_NUMBERS         : '\\p{Nl}',
        UnicodeCharacters.OTHER_NUMBERS          : '\\p{No}',
        UnicodeCharacters.DASH_PUNCTUATION       : '\\p{Pd}',
        UnicodeCharacters.OPEN_PUNCTUATION       : '\\p{Ps}',
        UnicodeCharacters.CLOSE_PUNCTUATION      : '\\p{Pe}',
        UnicodeCharacters.INITIAL_PUNCTUATION    : '\\p{Pi}',
        UnicodeCharacters.FINAL_PUNCTUATION      : '\\p{Pf}',
        UnicodeCharacters.CONNECTOR_PUNCTUATION  : '\\p{Pc}',
        UnicodeCharacters.OTHER_PUNCTUATION      : '\\p{Po}',
        UnicodeCharacters.CONTROL_CHARACTERS     : '\\p{Cc}',
        UnicodeCharacters.FORMAT_CHARACTERS      : '\\p{Cf}',
        UnicodeCharacters.PRIVATE_USE_CHARACTERS : '\\p{Co}',
        UnicodeCharacters.SURROGATE_CHARACTERS   : '\\p{Cs}',
        UnicodeCharacters.UNASSIGNED_CHARACTERS  : '\\p{Cn}'
    }

}
