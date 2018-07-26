from reggy.samples.tokens import Target

national_id_to_re = {

    Target.JAVA: {

        'Austrian social security number'            : '\\\\d{4}(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}',
        'Bulgarian Uniform Civil Number'             : '\\\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\\\d|3[01])[+-]?\\\\d{4}',
        'Canadian Social Insurance Number'           : '[1-9]\\\\d{2}[ -]?\d{3}[ -]?\\\\d{3}',
        'Chinese National Identification Card Number': '\\\\d{6}(?:19|20)\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])\\\\d{4}',
        'Croatian Master Citizen Number'             : '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])(?:9\\\\d{2}|0[01]\\\\d)\\\\d{6}',
        'Danish Civil Registration Number'           : '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}[+-]?\\\\d{4}',
        'Finnish Social Security Number'             : '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}[a+-]?\\\\d{3}[\\\\da-z]',
        'Indian Permanent Account Number'            : '[a-z]{3}[abcfghjlpt][a-z]\\\\d{4}[a-z]',
        'Indian Vehicle License Plate Number'        : '(?:dl ?[1-9]?\\\\d ?[cprstvy]|[a-z]{2} ?\\\\d{1,2}) ?[a-z]{0,2} ?\\\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)'       : '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\\\d|[37][01])(?:\\\\d[a-z]{3}|z\\\\d{3})[a-z]',
        'Norwegian Social Security Number'           : '(?:0[1-9]|[12]\\\\d|3[01])(?:[04][1-9]|[15][012])\\\\d{7}',
        'Romanian Personal Numeric Code'             : '[1-8]\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|[1-4]\\\\d|5[012]|99)\\\\d{4}',
        'South African ID number'                    : '\\\\d{2}[0-1][0-9][0-3]\\\\d\\\\d{4}[0-1]\\\\d{2}',
        'South Korean Resident Registration Number'  : '\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])-[12349]\\\\d{6}',
        'Swedish Personal Identification Number'     : '(?:19|20)?\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])[+-]\\\\d{4}',
        'Taiwanese National Identification Number'   : '[a-z][12]\\\\d{8}',
        'UK National Insurance Number'               : '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\\\d{2} ?\\\\d{2} ?\\\\d{2} ?[abcdfm]?',
        'US social security number'                  : '(?!000|666)[0-8]\\\\d{2}-(?!00)\\\\d{2}-(?!0000)\\\\d{4}'

    },

    Target.PERL: {

        'Austrian social security number'            : '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
        'Bulgarian Uniform Civil Number'             : '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
        'Canadian Social Insurance Number'           : '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
        'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
        'Croatian Master Citizen Number'             : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
        'Danish Civil Registration Number'           : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
        'Finnish Social Security Number'             : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
        'Indian Permanent Account Number'            : '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
        'Indian Vehicle License Plate Number'        : '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)'       : '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
        'Norwegian Social Security Number'           : '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
        'Romanian Personal Numeric Code'             : '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
        'South African ID number'                    : '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
        'South Korean Resident Registration Number'  : '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
        'Swedish Personal Identification Number'     : '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
        'Taiwanese National Identification Number'   : '[a-z][12]\\d{8}',
        'UK National Insurance Number'               : '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
        'US social security number'                  : '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    },

    Target.POSIX: {

        'Austrian social security number'            : '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
        'Bulgarian Uniform Civil Number'             : '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
        'Canadian Social Insurance Number'           : '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
        'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
        'Croatian Master Citizen Number'             : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
        'Danish Civil Registration Number'           : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
        'Finnish Social Security Number'             : '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
        'Indian Permanent Account Number'            : '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
        'Indian Vehicle License Plate Number'        : '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)'       : '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
        'Norwegian Social Security Number'           : '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
        'Romanian Personal Numeric Code'             : '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
        'South African ID number'                    : '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
        'South Korean Resident Registration Number'  : '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
        'Swedish Personal Identification Number'     : '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
        'Taiwanese National Identification Number'   : '[a-z][12]\\d{8}',
        'UK National Insurance Number'               : '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
        'US social security number'                  : '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    },

    Target.PYTHON: {

        'Austrian social security number': '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
        'Bulgarian Uniform Civil Number': '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
        'Canadian Social Insurance Number': '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
        'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
        'Croatian Master Citizen Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
        'Danish Civil Registration Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
        'Finnish Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
        'Indian Permanent Account Number': '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
        'Indian Vehicle License Plate Number': '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)': '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
        'Norwegian Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
        'Romanian Personal Numeric Code': '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
        'South African ID number': '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
        'South Korean Resident Registration Number': '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
        'Swedish Personal Identification Number': '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
        'Taiwanese National Identification Number': '[a-z][12]\\d{8}',
        'UK National Insurance Number': '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
        'US social security number': '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    },

    Target.JAVASCRIPT: {

        'Austrian social security number': '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
        'Bulgarian Uniform Civil Number': '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
        'Canadian Social Insurance Number': '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
        'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
        'Croatian Master Citizen Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
        'Danish Civil Registration Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
        'Finnish Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
        'Indian Permanent Account Number': '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
        'Indian Vehicle License Plate Number': '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)': '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
        'Norwegian Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
        'Romanian Personal Numeric Code': '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
        'South African ID number': '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
        'South Korean Resident Registration Number': '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
        'Swedish Personal Identification Number': '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
        'Taiwanese National Identification Number': '[a-z][12]\\d{8}',
        'UK National Insurance Number': '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
        'US social security number': '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    },

    Target.PHP: {

      'Austrian social security number': '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
      'Bulgarian Uniform Civil Number': '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
      'Canadian Social Insurance Number': '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
      'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
      'Croatian Master Citizen Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
      'Danish Civil Registration Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
      'Finnish Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
      'Indian Permanent Account Number': '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
      'Indian Vehicle License Plate Number': '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
      'Italian Fiscal Code (Codice fiscale)': '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
      'Norwegian Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
      'Romanian Personal Numeric Code': '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
      'South African ID number': '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
      'South Korean Resident Registration Number': '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
      'Swedish Personal Identification Number': '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
      'Taiwanese National Identification Number': '[a-z][12]\\d{8}',
      'UK National Insurance Number': '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
      'US social security number': '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    },

    Target.GOLANG: {

        'Austrian social security number': '\\\\d{4}(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}',
        'Bulgarian Uniform Civil Number': '\\\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\\\d|3[01])[+-]?\\\\d{4}',
        'Canadian Social Insurance Number': '[1-9]\\\\d{2}[ -]?\d{3}[ -]?\\\\d{3}',
        'Chinese National Identification Card Number': '\\\\d{6}(?:19|20)\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])\\\\d{4}',
        'Croatian Master Citizen Number': '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])(?:9\\\\d{2}|0[01]\\\\d)\\\\d{6}',
        'Danish Civil Registration Number': '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}[+-]?\\\\d{4}',
        'Finnish Social Security Number': '(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|1[012])\\\\d{2}[a+-]?\\\\d{3}[\\\\da-z]',
        'Indian Permanent Account Number': '[a-z]{3}[abcfghjlpt][a-z]\\\\d{4}[a-z]',
        'Indian Vehicle License Plate Number': '(?:dl ?[1-9]?\\\\d ?[cprstvy]|[a-z]{2} ?\\\\d{1,2}) ?[a-z]{0,2} ?\\\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)': '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\\\d|[37][01])(?:\\\\d[a-z]{3}|z\\\\d{3})[a-z]',
        'Norwegian Social Security Number': '(?:0[1-9]|[12]\\\\d|3[01])(?:[04][1-9]|[15][012])\\\\d{7}',
        'Romanian Personal Numeric Code': '[1-8]\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])(?:0[1-9]|[1-4]\\\\d|5[012]|99)\\\\d{4}',
        'South African ID number': '\\\\d{2}[0-1][0-9][0-3]\\\\d\\\\d{4}[0-1]\\\\d{2}',
        'South Korean Resident Registration Number': '\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])-[12349]\\\\d{6}',
        'Swedish Personal Identification Number': '(?:19|20)?\\\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\\\d|3[01])[+-]\\\\d{4}',
        'Taiwanese National Identification Number': '[a-z][12]\\\\d{8}',
        'UK National Insurance Number': '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\\\d{2} ?\\\\d{2} ?\\\\d{2} ?[abcdfm]?',
        'US social security number': '(?!000|666)[0-8]\\\\d{2}-(?!00)\\\\d{2}-(?!0000)\\\\d{4}'

    },

    Target.RUST: {

        'Austrian social security number': '\\d{4}(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}',
        'Bulgarian Uniform Civil Number': '\\d{2}(?:[024][1-9]|[135][012])(?:0[1-9]|[12]\\d|3[01])[+-]?\\d{4}',
        'Canadian Social Insurance Number': '[1-9]\\d{2}[ -]?\\d{3}[ -]?\\d{3}',
        'Chinese National Identification Card Number': '\\d{6}(?:19|20)\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])\\d{4}',
        'Croatian Master Citizen Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])(?:9\\d{2}|0[01]\\d)\\d{6}',
        'Danish Civil Registration Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[+-]?\\d{4}',
        'Finnish Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|1[012])\\d{2}[a+-]?\\d{3}[\\da-z]',
        'Indian Permanent Account Number': '[a-z]{3}[abcfghjlpt][a-z]\\d{4}[a-z]',
        'Indian Vehicle License Plate Number': '(?:dl ?[1-9]?\\d ?[cprstvy]|[a-z]{2} ?\\d{1,2}) ?[a-z]{0,2} ?\\d{1,4}',
        'Italian Fiscal Code (Codice fiscale)': '(?:[bcdfghjklmnpqrstvwxyz][a-z]{2}){2}\\d{2}[abcdehlmprst](?:[04][1-9]|[1256]\\d|[37][01])(?:\\d[a-z]{3}|z\\d{3})[a-z]',
        'Norwegian Social Security Number': '(?:0[1-9]|[12]\\d|3[01])(?:[04][1-9]|[15][012])\\d{7}',
        'Romanian Personal Numeric Code': '[1-8]\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])(?:0[1-9]|[1-4]\\d|5[012]|99)\\d{4}',
        'South African ID number': '\d{2}[0-1][0-9][0-3]\d\d{4}[0-1]\d{2}',
        'South Korean Resident Registration Number': '\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])-[12349]\\d{6}',
        'Swedish Personal Identification Number': '(?:19|20)?\\d{2}(?:0[1-9]|1[012])(?:0[1-9]|[12]\\d|3[01])[+-]\\d{4}',
        'Taiwanese National Identification Number': '[a-z][12]\\d{8}',
        'UK National Insurance Number': '[abceghjklmnoprstwxyz][abceghjklmnprstwxyz] ?\\d{2} ?\\d{2} ?\\d{2} ?[abcdfm]?',
        'US social security number': '(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}'

    }

}
