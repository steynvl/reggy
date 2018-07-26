from reggy.samples.tokens import Target, RegexExtraInfo

start_info_to_target = {

    Target.JAVA: {
        RegexExtraInfo.ANYWHERE        : '',
        RegexExtraInfo.START_OF_TEXT   : '\\\\b',
        RegexExtraInfo.START_OF_LINE   : '^',
        RegexExtraInfo.START_OF_WORD   : '\\\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\\\G'
    },

    Target.PERL: {
        RegexExtraInfo.ANYWHERE        : '',
        RegexExtraInfo.START_OF_TEXT   : '\\b',
        RegexExtraInfo.START_OF_LINE   : '^',
        RegexExtraInfo.START_OF_WORD   : '\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.POSIX: {
        RegexExtraInfo.ANYWHERE        : '',
        RegexExtraInfo.START_OF_TEXT   : '\\b',
        RegexExtraInfo.START_OF_LINE   : '^',
        RegexExtraInfo.START_OF_WORD   : '\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.PYTHON: {
        RegexExtraInfo.ANYWHERE: '',
        RegexExtraInfo.START_OF_TEXT: '\\b',
        RegexExtraInfo.START_OF_LINE: '^',
        RegexExtraInfo.START_OF_WORD: '\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.JAVASCRIPT: {
        RegexExtraInfo.ANYWHERE: '',
        RegexExtraInfo.START_OF_TEXT: '\\b',
        RegexExtraInfo.START_OF_LINE: '^',
        RegexExtraInfo.START_OF_WORD: '\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.PHP: {
      RegexExtraInfo.ANYWHERE: '',
      RegexExtraInfo.START_OF_TEXT: '\\b',
      RegexExtraInfo.START_OF_LINE: '^',
      RegexExtraInfo.START_OF_WORD: '\\b',
      RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    },

    Target.GOLANG: {
      RegexExtraInfo.ANYWHERE: '',
      RegexExtraInfo.START_OF_TEXT: '\\\\b',
      RegexExtraInfo.START_OF_LINE: '^',
      RegexExtraInfo.START_OF_WORD: '\\\\b',
      RegexExtraInfo.START_OF_ATTEMPT: '\\\\G'
    },

    Target.RUST: {
        RegexExtraInfo.ANYWHERE: '',
        RegexExtraInfo.START_OF_TEXT: '\\b',
        RegexExtraInfo.START_OF_LINE: '^',
        RegexExtraInfo.START_OF_WORD: '\\b',
        RegexExtraInfo.START_OF_ATTEMPT: '\\G'
    }

}
