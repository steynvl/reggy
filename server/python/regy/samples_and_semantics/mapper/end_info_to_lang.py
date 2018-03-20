from regy.samples_and_semantics.tokens import TargetLanguage, RegexEndInfo

end_info_to_lang = {

    TargetLanguage.JAVA: {
        RegexEndInfo.ANYWHERE   : '',
        RegexEndInfo.END_OF_TEXT: '\\z',
        RegexEndInfo.END_OF_LINE: '$',
        RegexEndInfo.END_OF_WORD: '\\b'
    },

    TargetLanguage.PERL: {

    },

    TargetLanguage.POSIX: {

    }

}
