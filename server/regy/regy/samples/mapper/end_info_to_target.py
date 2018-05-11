from regy.samples.tokens import Target, RegexEndInfo

end_info_to_target = {

    Target.JAVA: {
        RegexEndInfo.ANYWHERE   : '',
        RegexEndInfo.END_OF_TEXT: '\\\\z',
        RegexEndInfo.END_OF_LINE: '$',
        RegexEndInfo.END_OF_WORD: '\\\\b'
    },

    Target.PERL: {
        RegexEndInfo.ANYWHERE   : '',
        RegexEndInfo.END_OF_TEXT: '\\z',
        RegexEndInfo.END_OF_LINE: '$',
        RegexEndInfo.END_OF_WORD: '\\b'
    },

    Target.POSIX: {
        RegexEndInfo.ANYWHERE   : '',
        RegexEndInfo.END_OF_TEXT: '\\z',
        RegexEndInfo.END_OF_LINE: '$',
        RegexEndInfo.END_OF_WORD: '\\b'
    }

}
