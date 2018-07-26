from reggy.samples.tokens import Target

identifiers_to_re = {
    'd': {
        'No leading zeros allowed': '[12][0-9]|[1-9]|30|[12][0-9]|[1-9]|3[01]|[12][0-9]|[1-9]',
        'Optional leading zeros'  : '[12][0-9]|0?[1-9]|30|[12][0-9]|0?[1-9]|3[01]|[12][0-9]|0?[1-9]',
        'Leading zeros required'  : '[12][0-9]|0[1-9]|30|[12][0-9]|0[1-9]|3[01]|[12][0-9]|0[1-9]',
    },
    'm': {
        'No leading zeros allowed': '1[0-2]|[1-9]',
        'Optional leading zeros'  : '1[0-2]|0?[1-9]',
        'Leading zeros required'  : '1[0-2]|0[1-9]',
    },
    'y': '[0-9]{2}',
    'Y': '[0-9]{4}',
    'h': {
        'No leading zeros allowed': '1[0-2]|[1-9]',
        'Optional leading zeros'  : '1[0-2]|0?[1-9]',
        'Leading zeros required'  : '1[0-2]|0[1-9]',
    },
    'H': {
        'No leading zeros allowed': '2[0-3]|1?[0-9]',
        'Optional leading zeros'  : '2[0-3]|[01]?[0-9]',
        'Leading zeros required'  : '2[0-3]|[01][0-9]',
    },
    'n': {
        'No leading zeros allowed': '[1-5]?[0-9]',
        'Optional leading zeros'  : '[0-5]?[0-9]',
        'Leading zeros required'  : '[0-5][0-9]',
    },
    's': {
        'No leading zeros allowed': '[1-5]?[0-9]',
        'Optional leading zeros'  : '[0-5]?[0-9]',
        'Leading zeros required'  : '[0-5][0-9]',
    }
}

options_to_re = {

    Target.JAVA: {
        'dateSeparators': {
          'Forward slash'       : '/',
          'Hyphen'              : '-',
          'Dot'                 : '\\\\.',
          'Slash, hyphen or dot': '[-/.]'
        },
        'timeSeparators': {
            'Colon'       : ':',
            'Dot'         : '\\\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM'   : 'AM',
            'PM'   : 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.PERL: {
        'dateSeparators': {
            'Forward slash'       : '\/',
            'Hyphen'              : '-',
            'Dot'                 : '\\.',
            'Slash, hyphen or dot': '[-\/.]'
        },
        'timeSeparators': {
            'Colon'       : ':',
            'Dot'         : '\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM'   : 'AM',
            'PM'   : 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.POSIX: {
        'dateSeparators': {
            'Forward slash'       : '/',
            'Hyphen'              : '-',
            'Dot'                 : '\\.',
            'Slash, hyphen or dot': '[-/.]'
        },
        'timeSeparators': {
            'Colon'       : ':',
            'Dot'         : '\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM'   : 'AM',
            'PM'   : 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.PYTHON: {
        'dateSeparators': {
            'Forward slash'       : '/',
            'Hyphen'              : '-',
            'Dot'                 : '\\.',
            'Slash, hyphen or dot': '[-\/.]'
        },
        'timeSeparators': {
            'Colon'       : ':',
            'Dot'         : '\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM'   : 'AM',
            'PM'   : 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.JAVASCRIPT: {
        'dateSeparators': {
            'Forward slash': '\/',
            'Hyphen': '-',
            'Dot': '\\.',
            'Slash, hyphen or dot': '[-\/.]'
        },
        'timeSeparators': {
            'Colon': ':',
            'Dot': '\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM': 'AM',
            'PM': 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.PHP: {
      'dateSeparators': {
        'Forward slash': '\/',
        'Hyphen': '-',
        'Dot': '\\.',
        'Slash, hyphen or dot': '[-\/.]'
      },
      'timeSeparators': {
        'Colon': ':',
        'Dot': '\\.',
        'Colon or dot': '[:.]'

      },
      'amPmIndicators': {
        'AM': 'AM',
        'PM': 'PM',
        'AM/PM': '(?:AM|PM)'
      }
    },

    Target.GOLANG: {
        'dateSeparators': {
            'Forward slash': '/',
            'Hyphen': '-',
            'Dot': '\\\\.',
            'Slash, hyphen or dot': '[-/.]'
        },
        'timeSeparators': {
            'Colon': ':',
            'Dot': '\\\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM': 'AM',
            'PM': 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    },

    Target.RUST: {
        'dateSeparators': {
            'Forward slash': '/',
            'Hyphen': '-',
            'Dot': '\\.',
            'Slash, hyphen or dot': '[-\/.]'
        },
        'timeSeparators': {
            'Colon': ':',
            'Dot': '\\.',
            'Colon or dot': '[:.]'

        },
        'amPmIndicators': {
            'AM': 'AM',
            'PM': 'PM',
            'AM/PM': '(?:AM|PM)'
        }
    }

}
