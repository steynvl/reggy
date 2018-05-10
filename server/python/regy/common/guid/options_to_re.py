from regy.samples.tokens import Target

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
    }

}
