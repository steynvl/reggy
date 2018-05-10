from regy.samples.tokens import Target, RegexStartInfo

start_info_to_target = {

    Target.JAVA: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\\\G'
    },

    Target.PERL: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.POSIX: {
        RegexStartInfo.ANYWHERE        : '',
        RegexStartInfo.START_OF_TEXT   : '\\b',
        RegexStartInfo.START_OF_LINE   : '^',
        RegexStartInfo.START_OF_WORD   : '\\b',
        RegexStartInfo.START_OF_ATTEMPT: '\\G'
    }

}
