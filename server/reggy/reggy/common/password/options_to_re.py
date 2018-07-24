from reggy.samples.tokens import Target

opt_to_re = {

    Target.JAVA: {
        'Anything'         : '',
        'Digit'            : '\\\\d',
        'Lowercase letter' : '[a-z]',
        'Minus'            : '-',
        'Whitespace'       : '\\\\s',
        'Special character': '[!\\"#$%&\'()*+,-.:;<=>?@\\\\[\\\\]^_`{|}~]',
        'Letter'           : '[A-Za-z]',
        'Underline'        : '_',
        'Uppercase letter' : '[A-Z]',
        'Letter or digit' : '[A-Za-z0-9]'
    },

    Target.PERL: {
        'Anything'         : '',
        'Digit'            : '\\d',
        'Lowercase letter' : '[a-z]',
        'Minus'            : '-',
        'Whitespace'       : '\\s',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\\[\\]^_`{|}~]',
        'Letter'           : '[A-Za-z]',
        'Underline'        : '_',
        'Uppercase letter' : '[A-Z]',
        'Letter or digit' : '[A-Za-z0-9]'
    },

    Target.POSIX: {
        'Anything'         : '',
        'Digit'            : '\\d',
        'Lowercase letter' : '[a-z]',
        'Minus'            : '-',
        'Whitespace'       : '\\s',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\\[\\]^_`{|}~]',
        'Letter'           : '[A-Za-z]',
        'Underline'        : '_',
        'Uppercase letter' : '[A-Z]',
        'Letter or digit' : '[A-Za-z0-9]'
    },

    Target.PYTHON: {
        'Anything': '',
        'Digit': '\\d',
        'Lowercase letter': '[a-z]',
        'Minus': '-',
        'Whitespace': '\\s',
        'Special character': '[!"#$%&\\\'()*+,-.:;<=>?@\\[\\]^_`{|}~]',
        'Letter': '[A-Za-z]',
        'Underline': '_',
        'Uppercase letter': '[A-Z]',
        'Letter or digit': '[A-Za-z0-9]'
    },

    Target.JAVASCRIPT: {
        'Anything': '',
        'Digit': '\\d',
        'Lowercase letter': '[a-z]',
        'Minus': '-',
        'Whitespace': '\\s',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\\[\\]^_`{|}~]',
        'Letter': '[A-Za-z]',
        'Underline': '_',
        'Uppercase letter': '[A-Z]',
        'Letter or digit': '[A-Za-z0-9]'
    }

}


