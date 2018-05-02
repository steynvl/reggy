from regy.samples_and_semantics.tokens import Target

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
    }


}
