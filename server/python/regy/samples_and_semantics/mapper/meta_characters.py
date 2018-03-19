from regy.samples_and_semantics.tokens import TargetLanguage

meta_characters = {

    TargetLanguage.JAVA: {
        '{': '\{',
        '}': '\}',
        '[': '\[',
        ']': '\]',
        '(': '\(',
        ')': '\)',
        '^': '\^',
        '$': '\$',
        '.': '\.',
        '|': '\|',
        '*': '\*',
        '+': '\+',
        '?': '\?',
        '\\': '\\\\'
    },

    TargetLanguage.PERL: {

    },

    TargetLanguage.POSIX: {

    }

}
