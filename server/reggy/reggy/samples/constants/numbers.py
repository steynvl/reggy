from reggy.samples.tokens import Target


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

    },

    Target.PYTHON: {
        'thousandSeparator': {
            'Any': '[,\\\' ]',
            'Comma': ',',
            'Quote': '\\\'',
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

    Target.JAVASCRIPT: {

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

    Target.PHP: {

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

    Target.GOLANG: {

      'thousandSeparator': {
        'Any': '[,\' ]',
        'Comma': ',',
        'Quote': '\'',
        'Space': ' '
      },

      'decimalSeparator': {
        'Any': '[,.]',
        'Period': '\\\\.',
        'Comma': ','
      },

      'currencySign': {
        'Any': '[$€¥£]',
        'Dollar': '\\\\$',
        'Euro': '€',
        'Yen': '¥',
        'Pound': '£'
      },

      'allowExponent': '(?:[eE][+-]?[0-9]++)',
      'number': '\\\\d',
      'plusSign': '\\\\+'

    },

    Target.RUST: {
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

    Target.CSHARP: {
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

    Target.SCALA: {

        'thousandSeparator': {
            'Any': '[,\' ]',
            'Comma': ',',
            'Quote': '\'',
            'Space': ' '
        },

        'decimalSeparator': {
            'Any': '[,.]',
            'Period': '\\\\.',
            'Comma': ','
        },

        'currencySign': {
            'Any': '[$€¥£]',
            'Dollar': '\\\\$',
            'Euro': '€',
            'Yen': '¥',
            'Pound': '£'
        },

        'allowExponent': '(?:[eE][+-]?[0-9]++)',
        'number': '\\\\d',
        'plusSign': '\\\\+'

    },

    Target.KOTLIN: {

        'thousandSeparator': {
            'Any': '[,\' ]',
            'Comma': ',',
            'Quote': '\'',
            'Space': ' '
        },

        'decimalSeparator': {
            'Any': '[,.]',
            'Period': '\\\\.',
            'Comma': ','
        },

        'currencySign': {
            'Any': '[$€¥£]',
            'Dollar': '\\\\$',
            'Euro': '€',
            'Yen': '¥',
            'Pound': '£'
        },

        'allowExponent': '(?:[eE][+-]?[0-9]++)',
        'number': '\\\\d',
        'plusSign': '\\\\+'

    }

}
