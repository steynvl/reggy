from regy.samples.tokens import Target

const_to_re = {

    Target.JAVA: {

        'thousandSeparator': {
            'Any'  : '[,\' ]',
            'Comma': ',',
            'Quote': '\'',
            'Space': ' '
        },

        'decimalSeparator': {
            'Any'   : '[,.]',
            'Period': '\\\\.',
            'Comma' : ','
        },

        'currencySign': {
            'Any'      : '[$€¥£]',
            'Dollar'   : '\\\\$',
            'Euro'     : '€',
            'Yen'      : '¥',
            'Pound'    : '£'
        },

        'allowExponent': '(?:[eE][+-]?[0-9]++)',
        'number': '\\\\d',
        'plusSign': '\\\\+'

    },

    Target.PERL: {

        'thousandSeparator': {
            'Any': '[,\' ]',
            'Comma': ',',
            'Quote': '\'',
            'Space': ' '
        },

        'decimalSeparator': {
            'Any': '[,.]',
            'Period': '\\.',
            'Comma': ','
        },

        'currencySign': {
            'Any': '[$€¥£]',
            'Dollar': '\\$',
            'Euro': '€',
            'Yen': '¥',
            'Pound': '£'
        },

        'allowExponent': '(?:[eE][+-]?[0-9]++)',
        'number': '\\d',
        'plusSign': '\\+'

    },

    Target.POSIX: {

        'thousandSeparator': {
            'Any': '[,\' ]',
            'Comma': ',',
            'Quote': '\'',
            'Space': ' '
        },

        'decimalSeparator': {
            'Any': '[,.]',
            'Period': '\\.',
            'Comma': ','
        },

        'currencySign': {
            'Any': '[$€¥£]',
            'Dollar': '\\$',
            'Euro': '€',
            'Yen': '¥',
            'Pound': '£'
        },

        'allowExponent': '(?:[eE][+-]?[0-9]++)',
        'number': '\\d',
        'plusSign': '\\+'

    }

}