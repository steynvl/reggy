from reggy.samples.tokens import Target

braces_to_re = {

    Target.JAVA: {
        'Required'   : '\\\\{%s}',
        'Optional'   : '%s|\\\\{%s}'
    },

    Target.PERL: {
        'Required'   : '\\{%s}',
        'Optional'   : '%s|\\{%s}'
    },

    Target.POSIX: {
        'Required'   : '\\{%s}',
        'Optional'   : '%s|\\{%s}'
    },

    Target.PYTHON: {
        'Required'   : '\\{%s}',
        'Optional'   : '%s|\\{%s}'
    },

    Target.JAVASCRIPT: {
        'Required': '\\{%s}',
        'Optional': '%s|\\{%s}'
    },

    Target.PHP: {
      'Required': '\\{%s}',
      'Optional': '%s|\\{%s}'
    },

    Target.GOLANG: {
        'Required': '\\\\{%s}',
        'Optional': '%s|\\\\{%s}'
    },

    Target.RUST: {
        'Required': '\\{%s}',
        'Optional': '%s|\\{%s}'
    },

    Target.CSHARP: {
        'Required': '\\{%s}',
        'Optional': '%s|\\{%s}'
    },

    Target.SCALA: {
        'Required': '\\\\{%s}',
        'Optional': '%s|\\\\{%s}'
    },

    Target.KOTLIN: {
        'Required': '\\\\{%s}',
        'Optional': '%s|\\\\{%s}'
    }

}

case_to_re = {

    Target.JAVA: {
        'Case insensitive': '[\\\\dA-Fa-f]',
        'Uppercase'       : '[\\\\dA-F]',
        'Lowercase'       : '[\\\\da-f]'
    },

    Target.PERL: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase'       : '[\\dA-F]',
        'Lowercase'       : '[\\da-f]'
    },

    Target.POSIX: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase'       : '[\\dA-F]',
        'Lowercase'       : '[\\da-f]'
    },

    Target.PYTHON: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase': '[\\dA-F]',
        'Lowercase': '[\\da-f]'
    },

    Target.JAVASCRIPT: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase': '[\\dA-F]',
        'Lowercase': '[\\da-f]'
    },

    Target.PHP: {
      'Case insensitive': '[\\dA-Fa-f]',
      'Uppercase': '[\\dA-F]',
      'Lowercase': '[\\da-f]'
    },

    Target.GOLANG: {
        'Case insensitive': '[\\\\dA-Fa-f]',
        'Uppercase': '[\\\\dA-F]',
        'Lowercase': '[\\\\da-f]'
    },

    Target.RUST: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase': '[\\dA-F]',
        'Lowercase': '[\\da-f]'
    },

    Target.CSHARP: {
        'Case insensitive': '[\\dA-Fa-f]',
        'Uppercase': '[\\dA-F]',
        'Lowercase': '[\\da-f]'
    },

    Target.SCALA: {
        'Case insensitive': '[\\\\dA-Fa-f]',
        'Uppercase': '[\\\\dA-F]',
        'Lowercase': '[\\\\da-f]'
    },

    Target.KOTLIN: {
        'Case insensitive': '[\\\\dA-Fa-f]',
        'Uppercase': '[\\\\dA-F]',
        'Lowercase': '[\\\\da-f]'
    }

}
