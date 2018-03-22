from regy.samples_and_semantics.tokens import TargetLanguage, RegexStartInfo

start_info_to_lang = {

    TargetLanguage.JAVA: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\\\G'
    },

    TargetLanguage.PERL: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\G'
    },

    TargetLanguage.POSIX: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\G'
    }

}
