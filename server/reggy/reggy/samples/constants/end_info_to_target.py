from reggy.samples.tokens import Target, RegexExtraInfo

end_info_to_target = {

    Target.JAVA: {
        RegexExtraInfo.ANYWHERE   : '',
        RegexExtraInfo.END_OF_TEXT: '\\\\z',
        RegexExtraInfo.END_OF_LINE: '$',
        RegexExtraInfo.END_OF_WORD: '\\\\b'
    },

    Target.PERL: {
        RegexExtraInfo.ANYWHERE   : '',
        RegexExtraInfo.END_OF_TEXT: '\\z',
        RegexExtraInfo.END_OF_LINE: '$',
        RegexExtraInfo.END_OF_WORD: '\\b'
    },

    Target.POSIX: {
        RegexExtraInfo.ANYWHERE   : '',
        RegexExtraInfo.END_OF_TEXT: '\\z',
        RegexExtraInfo.END_OF_LINE: '$',
        RegexExtraInfo.END_OF_WORD: '\\b'
    }

}
