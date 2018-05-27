from reggy.samples.tokens import Target
from reggy.samples.tokens.regex_extra_info import RegexExtraInfo

regex_info_to_tok = {

    'Java'         : Target.JAVA,
    'Perl'         : Target.PERL,
    'POSIX'        : Target.POSIX,

    'Anywhere'     : RegexExtraInfo.ANYWHERE,
    'Start of text': RegexExtraInfo.START_OF_TEXT,
    'Start of line': RegexExtraInfo.START_OF_LINE,
    'Start of word': RegexExtraInfo.START_OF_WORD,

    'End of text'  : RegexExtraInfo.END_OF_TEXT,
    'End of line'  : RegexExtraInfo.END_OF_LINE,
    'End of word'  : RegexExtraInfo.END_OF_WORD

}