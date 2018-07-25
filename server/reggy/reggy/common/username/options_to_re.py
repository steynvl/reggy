from reggy.samples.tokens import Target

opt_to_re = {

    Target.JAVA: {
        'Anything'         : '',
        'Letter'           : '[A-Za-z]',
        'Uppercase letter' : '[A-Z]',
        'Lowercase letter' : '[a-z]',
        'Letter or number' : '[A-Za-z0-9]',
        'Special character': '[!\\"#$%&\'()*+,-.:;<=>?@\\\\[\\\\]^_`{|}~]',
        'Number'           : '\\\\d'
    },

    Target.PERL: {
        'Anything'         : '',
        'Letter'           : '[A-Za-z]',
        'Uppercase letter' : '[A-Z]',
        'Lowercase letter' : '[a-z]',
        'Letter or number' : '[A-Za-z0-9]',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\[\]^_`{|}~]',
        'Number'           : '\\d'
    },

    Target.POSIX: {
        'Anything'         : '',
        'Letter'           : '[A-Za-z]',
        'Uppercase letter' : '[A-Z]',
        'Lowercase letter' : '[a-z]',
        'Letter or number' : '[A-Za-z0-9]',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\[\]^_`{|}~]',
        'Number'           : '\\d'
    },

    Target.PYTHON: {
        'Anything': '',
        'Letter': '[A-Za-z]',
        'Uppercase letter': '[A-Z]',
        'Lowercase letter': '[a-z]',
        'Letter or number': '[A-Za-z0-9]',
        'Special character': '[!"#$%&\\\'()*+,-.:;<=>?@\[\]^_`{|}~]',
        'Number': '\\d'
    },

    Target.JAVASCRIPT: {
        'Anything': '',
        'Letter': '[A-Za-z]',
        'Uppercase letter': '[A-Z]',
        'Lowercase letter': '[a-z]',
        'Letter or number': '[A-Za-z0-9]',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@\[\]^_`{|}~]',
        'Number': '\\d'
    },

    Target.PHP: {
      'Anything': '',
      'Letter': '[A-Za-z]',
      'Uppercase letter': '[A-Z]',
      'Lowercase letter': '[a-z]',
      'Letter or number': '[A-Za-z0-9]',
      'Special character': '[!"#$%&\'()*+,-.:;<=>?@\[\]^_`{|}~]',
      'Number': '\\d'
    }

}
