from regy.samples_and_semantics.tokens import Target

opt_to_re = {

    Target.JAVA: {
        'Letter'           : '[A-Za-z]',
        'Uppercase letter' : '[A-Z]',
        'Lowercase letter' : '[a-z]',
        'Letter or number' : '[A-Za-z0-9]',
        'Special character': '[!\\"#$%&\'()*+,-.:;<=>?@\\\\[\\\\]^_`{|}~]',
        'Number'           : '\\\\d'
    },

    Target.PERL: {
        'Letter'           : '[A-Za-z]',
        'Uppercase letter' : '[A-Z]',
        'Lowercase letter' : '[a-z]',
        'Letter or number' : '[A-Za-z0-9]',
        'Special character': '[!"#$%&\'()*+,-.:;<=>?@[]^_`{|}~]',
        'Number'           : '\\d'
    },

    Target.POSIX: {

    }


}
