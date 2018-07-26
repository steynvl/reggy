from reggy.samples.tokens import Target

vat_to_re = {

    Target.JAVA: {

        'austria'      : {
            'code'   : 'AT',
            'noGroup': 'U\\\\d{8}',
            'group'  : '{}*U(?>{}*\\\\d){{8}}'
        },
        'belgium'      : {
            'code'   : 'BE',
            'noGroup': '0\\\\d{9}',
            'group'  : '0(?>{}*\\\\d){{9}}'
        },
        'bulgaria'     : {
            'code'   : 'BG',
            'noGroup': '\\\\d{9,10}',
            'group'  : '(?>{}*\\\\d){{9,10}}'
        },
        'cyprus'       : {
            'code'   : 'CY',
            'noGroup': '\\\\d{8}[A-Z]',
            'group'  : '(?>{}*\\\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code'   : 'CZ',
            'noGroup': '\\\\d{8,10}',
            'group'  : '(?>{}*\\\\d){{8,10}}'
        },
        'germany'      : {
            'code'   : 'DE',
            'noGroup': '\\\\d{9}',
            'group'  : '(?>{}*\\\\d){{9}}'
        },
        'denmark'      : {
            'code': 'DK',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'slovakia'     : {
            'code'   : 'SK',
            'noGroup': '\\\\d{10}',
            'group'  : '(?>{}*\\\\d){{10}}'
        },
        'estonia'      : {
            'code'   : 'EE',
            'noGroup': '\\\\d{9}',
            'group'  : '(?>{}*\\\\d){{9}}'
        },
        'greece'       : {
            'code'   : '(?:EL|GR)',
            'noGroup': '\\\\d{9}',
            'group'  : '(?>{}*\\\\d){{9}}'
        },
        'ireland'      : {
            'code'   : 'IE',
            'noGroup': '(?:\\\\d[\\\\d*+A-Z]\\\\d{5}[A-Z]|\\\\d{7}[A-Z]{2})',
            'group'  : '(?:\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland'       : {
            'code'   : 'PL',
            'noGroup': '\\\\d{10}',
            'group'  : '(?>{}*\\\\d){{10}}'
        },
        'spain'        : {
            'code'   : 'ES',
            'noGroup': '[\\\\dA-Z]\\\\d{7}[\\\\dA-Z]',
            'group'  : '[\\\\dA-Z](?>{}*\\\\d){{7}}{}*[\\\\dA-Z]'
        },
        'italy'        : {
            'code'   : 'IT',
            'noGroup': '\\\\d{11}',
            'group'  : '(?>{}*\\\\d){{11}}'
        },
        'portugal'     : {
            'code'   : 'PT',
            'noGroup': '\\\\d{9}',
            'group'  : '(?>{}*\\\\d){{9}}'
        },
        'finland'      : {
            'code'   : 'FI',
            'noGroup': '\\\\d{8}',
            'group'  : '(?>{}*\\\\d){{8}}'
        },
        'lithuania'    : {
            'code'   : 'LT',
            'noGroup': '(?:\\\\d{9}|\\\\d{12})',
            'group'  : '(?:(?>{}*\\\\d){{9}}|(?>{}*\\\\d){{12}})'
        },
        'romania'      : {
            'code'   : 'RO',
            'noGroup': '\\\\d{2,10}',
            'group'  : '(?>{}*\\\\d){{2,10}}'
        },
        'france'       : {
            'code'   : 'FR',
            'noGroup': '[\\\\dA-Z]{2}\\\\d{9}',
            'group'  : '(?>{}*[\\\\dA-Z]){{2}}(?>{}*\\\\d){{9}}'
        },
        'luxembourg'   : {
            'code'   : 'LU',
            'noGroup': '\\\\d{8}',
            'group'  : '(?>{}*\\\\d){{8}}'
        },
        'unitedKingdom': {
            'code'      : 'GB',
            'noGroup'   : '(?:\\\\d{9}(?:\\\\d{3})?|GD[0-4]\\\\d{2}|HA[5-9]\\\\d{2})',
            'group'     : '(?:(?>{}*\\\\d){{9}}(?:(?>{}*\\\\d){{3}})?|GD[0-4](?>{}*\\\\d){{2}}|HA[5-9](?>{}*\\\\d){{2}})',
        },
        'latvia'       : {
            'code'   : 'LV',
            'noGroup': '\\\\d{11}',
            'group'  : '(?>{}*\\\\d){{11}}'
        },
        'sweden'       : {
            'code'   : 'SE',
            'noGroup': '\\\\d{12}',
            'group'  : '(?>{}*\\\\d){{12}}'
        },
        'croatia'      : {
            'code'   : 'HR',
            'noGroup': '\\\\d{11}',
            'group'  : '(?>{}*\\\\d){{11}}'
        },
        'malta'        : {
            'code'   : 'MT',
            'noGroup': '\\\\d{8}',
            'group'  : '(?>{}*\\\\d){{8}}'
        },

        'slovenia'     : {
            'code'   : 'SI',
            'noGroup': '\\\\d{8}',
            'group'  : '(?>{}*\\\\d){{8}}'
        },
        'hungary'      : {
            'code'   : 'HU',
            'noGroup': '\\\\d{8}',
            'group'  : '(?>{}*\\\\d){{8}}'
        },
        'netherlands'  : {
            'code'   : 'NL',
            'noGroup': '\\\\d{9}B\\\\d{2}',
            'group'  : '(?>{}*\\\\d){{9}}{}*B(?>{}*\\\\d){{2}}'
        }

    },

    Target.PERL: {

        'austria'      : {
            'code'   : 'AT',
            'noGroup': 'U\\d{8}',
            'group'  : '{}*U(?>{}*\\d){{8}}'
        },
        'belgium'      : {
            'code'   : 'BE',
            'noGroup': '0\\d{9}',
            'group'  : '0(?>{}*\\d){{9}}'
        },
        'bulgaria'     : {
            'code'   : 'BG',
            'noGroup': '\\d{9,10}',
            'group'  : '(?>{}*\\d){{9,10}}'
        },
        'cyprus'       : {
            'code'   : 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group'  : '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code'   : 'CZ',
            'noGroup': '\\d{8,10}',
            'group'  : '(?>{}*\\d){{8,10}}'
        },
        'germany'      : {
            'code'   : 'DE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'denmark'      : {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia'     : {
            'code'   : 'SK',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'estonia'      : {
            'code'   : 'EE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'greece'       : {
            'code'   : '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'ireland'      : {
            'code'   : 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group'  : '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland'       : {
            'code'   : 'PL',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'spain'        : {
            'code'   : 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group'  : '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy'        : {
            'code'   : 'IT',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'portugal'     : {
            'code'   : 'PT',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'finland'      : {
            'code'   : 'FI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'lithuania'    : {
            'code'   : 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group'  : '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania'      : {
            'code'   : 'RO',
            'noGroup': '\\d{2,10}',
            'group'  : '(?>{}*\\d){{2,10}}'
        },
        'france'       : {
            'code'   : 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group'  : '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg'   : {
            'code'   : 'LU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code'      : 'GB',
            'noGroup'   : '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group'     : '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia'       : {
            'code'   : 'LV',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'sweden'       : {
            'code'   : 'SE',
            'noGroup': '\\d{12}',
            'group'  : '(?>{}*\\d){{12}}'
        },
        'croatia'      : {
            'code'   : 'HR',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'malta'        : {
            'code'   : 'MT',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },

        'slovenia'     : {
            'code'   : 'SI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'hungary'      : {
            'code'   : 'HU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'netherlands'  : {
            'code'   : 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group'  : '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.POSIX: {

        'austria'      : {
            'code'   : 'AT',
            'noGroup': 'U\\d{8}',
            'group'  : '{}*U(?>{}*\\d){{8}}'
        },
        'belgium'      : {
            'code'   : 'BE',
            'noGroup': '0\\d{9}',
            'group'  : '0(?>{}*\\d){{9}}'
        },
        'bulgaria'     : {
            'code'   : 'BG',
            'noGroup': '\\d{9,10}',
            'group'  : '(?>{}*\\d){{9,10}}'
        },
        'cyprus'       : {
            'code'   : 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group'  : '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code'   : 'CZ',
            'noGroup': '\\d{8,10}',
            'group'  : '(?>{}*\\d){{8,10}}'
        },
        'germany'      : {
            'code'   : 'DE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'denmark'      : {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia'     : {
            'code'   : 'SK',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'estonia'      : {
            'code'   : 'EE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'greece'       : {
            'code'   : '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'ireland'      : {
            'code'   : 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group'  : '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland'       : {
            'code'   : 'PL',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'spain'        : {
            'code'   : 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group'  : '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy'        : {
            'code'   : 'IT',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'portugal'     : {
            'code'   : 'PT',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'finland'      : {
            'code'   : 'FI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'lithuania'    : {
            'code'   : 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group'  : '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania'      : {
            'code'   : 'RO',
            'noGroup': '\\d{2,10}',
            'group'  : '(?>{}*\\d){{2,10}}'
        },
        'france'       : {
            'code'   : 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group'  : '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg'   : {
            'code'   : 'LU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code'      : 'GB',
            'noGroup'   : '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group'     : '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia'       : {
            'code'   : 'LV',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'sweden'       : {
            'code'   : 'SE',
            'noGroup': '\\d{12}',
            'group'  : '(?>{}*\\d){{12}}'
        },
        'croatia'      : {
            'code'   : 'HR',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'malta'        : {
            'code'   : 'MT',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },

        'slovenia'     : {
            'code'   : 'SI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'hungary'      : {
            'code'   : 'HU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'netherlands'  : {
            'code'   : 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group'  : '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.PYTHON: {

        'austria'      : {
            'code'   : 'AT',
            'noGroup': 'U\\d{8}',
            'group'  : '{}*U(?>{}*\\d){{8}}'
        },
        'belgium'      : {
            'code'   : 'BE',
            'noGroup': '0\\d{9}',
            'group'  : '0(?>{}*\\d){{9}}'
        },
        'bulgaria'     : {
            'code'   : 'BG',
            'noGroup': '\\d{9,10}',
            'group'  : '(?>{}*\\d){{9,10}}'
        },
        'cyprus'       : {
            'code'   : 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group'  : '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code'   : 'CZ',
            'noGroup': '\\d{8,10}',
            'group'  : '(?>{}*\\d){{8,10}}'
        },
        'germany'      : {
            'code'   : 'DE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'denmark'      : {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia'     : {
            'code'   : 'SK',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'estonia'      : {
            'code'   : 'EE',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'greece'       : {
            'code'   : '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'ireland'      : {
            'code'   : 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group'  : '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland'       : {
            'code'   : 'PL',
            'noGroup': '\\d{10}',
            'group'  : '(?>{}*\\d){{10}}'
        },
        'spain'        : {
            'code'   : 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group'  : '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy'        : {
            'code'   : 'IT',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'portugal'     : {
            'code'   : 'PT',
            'noGroup': '\\d{9}',
            'group'  : '(?>{}*\\d){{9}}'
        },
        'finland'      : {
            'code'   : 'FI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'lithuania'    : {
            'code'   : 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group'  : '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania'      : {
            'code'   : 'RO',
            'noGroup': '\\d{2,10}',
            'group'  : '(?>{}*\\d){{2,10}}'
        },
        'france'       : {
            'code'   : 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group'  : '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg'   : {
            'code'   : 'LU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code'      : 'GB',
            'noGroup'   : '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group'     : '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia'       : {
            'code'   : 'LV',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'sweden'       : {
            'code'   : 'SE',
            'noGroup': '\\d{12}',
            'group'  : '(?>{}*\\d){{12}}'
        },
        'croatia'      : {
            'code'   : 'HR',
            'noGroup': '\\d{11}',
            'group'  : '(?>{}*\\d){{11}}'
        },
        'malta'        : {
            'code'   : 'MT',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },

        'slovenia'     : {
            'code'   : 'SI',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'hungary'      : {
            'code'   : 'HU',
            'noGroup': '\\d{8}',
            'group'  : '(?>{}*\\d){{8}}'
        },
        'netherlands'  : {
            'code'   : 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group'  : '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.JAVASCRIPT: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\d{8}',
            'group': '{}*U(?>{}*\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\d{9}',
            'group': '0(?>{}*\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\d{9,10}',
            'group': '(?>{}*\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group': '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\d{8,10}',
            'group': '(?>{}*\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group': '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group': '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group': '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\d{2,10}',
            'group': '(?>{}*\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group': '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group': '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\d{12}',
            'group': '(?>{}*\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group': '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.PHP: {

      'austria': {
        'code': 'AT',
        'noGroup': 'U\\d{8}',
        'group': '{}*U(?>{}*\\d){{8}}'
      },
      'belgium': {
        'code': 'BE',
        'noGroup': '0\\d{9}',
        'group': '0(?>{}*\\d){{9}}'
      },
      'bulgaria': {
        'code': 'BG',
        'noGroup': '\\d{9,10}',
        'group': '(?>{}*\\d){{9,10}}'
      },
      'cyprus': {
        'code': 'CY',
        'noGroup': '\\d{8}[A-Z]',
        'group': '(?>{}*\\d){{8}}{}*[A-Z]'
      },
      'czechRepublic': {
        'code': 'CZ',
        'noGroup': '\\d{8,10}',
        'group': '(?>{}*\\d){{8,10}}'
      },
      'germany': {
        'code': 'DE',
        'noGroup': '\\d{9}',
        'group': '(?>{}*\\d){{9}}'
      },
      'denmark': {
        'code': 'DK',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },
      'slovakia': {
        'code': 'SK',
        'noGroup': '\\d{10}',
        'group': '(?>{}*\\d){{10}}'
      },
      'estonia': {
        'code': 'EE',
        'noGroup': '\\d{9}',
        'group': '(?>{}*\\d){{9}}'
      },
      'greece': {
        'code': '(?:EL|GR)',
        'noGroup': '\\d{9}',
        'group': '(?>{}*\\d){{9}}'
      },
      'ireland': {
        'code': 'IE',
        'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
        'group': '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
        'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
        'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
      },
      'poland': {
        'code': 'PL',
        'noGroup': '\\d{10}',
        'group': '(?>{}*\\d){{10}}'
      },
      'spain': {
        'code': 'ES',
        'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
        'group': '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
      },
      'italy': {
        'code': 'IT',
        'noGroup': '\\d{11}',
        'group': '(?>{}*\\d){{11}}'
      },
      'portugal': {
        'code': 'PT',
        'noGroup': '\\d{9}',
        'group': '(?>{}*\\d){{9}}'
      },
      'finland': {
        'code': 'FI',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },
      'lithuania': {
        'code': 'LT',
        'noGroup': '(?:\\d{9}|\\d{12})',
        'group': '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
      },
      'romania': {
        'code': 'RO',
        'noGroup': '\\d{2,10}',
        'group': '(?>{}*\\d){{2,10}}'
      },
      'france': {
        'code': 'FR',
        'noGroup': '[\\dA-Z]{2}\\d{9}',
        'group': '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
      },
      'luxembourg': {
        'code': 'LU',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },
      'unitedKingdom': {
        'code': 'GB',
        'noGroup': '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
        'group': '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
      },
      'latvia': {
        'code': 'LV',
        'noGroup': '\\d{11}',
        'group': '(?>{}*\\d){{11}}'
      },
      'sweden': {
        'code': 'SE',
        'noGroup': '\\d{12}',
        'group': '(?>{}*\\d){{12}}'
      },
      'croatia': {
        'code': 'HR',
        'noGroup': '\\d{11}',
        'group': '(?>{}*\\d){{11}}'
      },
      'malta': {
        'code': 'MT',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },

      'slovenia': {
        'code': 'SI',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },
      'hungary': {
        'code': 'HU',
        'noGroup': '\\d{8}',
        'group': '(?>{}*\\d){{8}}'
      },
      'netherlands': {
        'code': 'NL',
        'noGroup': '\\d{9}B\\d{2}',
        'group': '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
      }

    },

    Target.GOLANG: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\\\d{8}',
            'group': '{}*U(?>{}*\\\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\\\d{9}',
            'group': '0(?>{}*\\\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\\\d{9,10}',
            'group': '(?>{}*\\\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\\\d{8}[A-Z]',
            'group': '(?>{}*\\\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\\\d{8,10}',
            'group': '(?>{}*\\\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\\\d[\\\\d*+A-Z]\\\\d{5}[A-Z]|\\\\d{7}[A-Z]{2})',
            'group': '(?:\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\\\dA-Z]\\\\d{7}[\\\\dA-Z]',
            'group': '[\\\\dA-Z](?>{}*\\\\d){{7}}{}*[\\\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\\\d{9}|\\\\d{12})',
            'group': '(?:(?>{}*\\\\d){{9}}|(?>{}*\\\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\\\d{2,10}',
            'group': '(?>{}*\\\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\\\dA-Z]{2}\\\\d{9}',
            'group': '(?>{}*[\\\\dA-Z]){{2}}(?>{}*\\\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\\\d{9}(?:\\\\d{3})?|GD[0-4]\\\\d{2}|HA[5-9]\\\\d{2})',
            'group': '(?:(?>{}*\\\\d){{9}}(?:(?>{}*\\\\d){{3}})?|GD[0-4](?>{}*\\\\d){{2}}|HA[5-9](?>{}*\\\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\\\d{12}',
            'group': '(?>{}*\\\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\\\d{9}B\\\\d{2}',
            'group': '(?>{}*\\\\d){{9}}{}*B(?>{}*\\\\d){{2}}'
        }

    },

    Target.RUST: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\d{8}',
            'group': '{}*U(?>{}*\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\d{9}',
            'group': '0(?>{}*\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\d{9,10}',
            'group': '(?>{}*\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group': '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\d{8,10}',
            'group': '(?>{}*\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group': '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group': '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group': '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\d{2,10}',
            'group': '(?>{}*\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group': '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group': '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\d{12}',
            'group': '(?>{}*\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group': '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.CSHARP: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\d{8}',
            'group': '{}*U(?>{}*\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\d{9}',
            'group': '0(?>{}*\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\d{9,10}',
            'group': '(?>{}*\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\d{8}[A-Z]',
            'group': '(?>{}*\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\d{8,10}',
            'group': '(?>{}*\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\d[\\d*+A-Z]\\d{5}[A-Z]|\\d{7}[A-Z]{2})',
            'group': '(?:\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\d{}*[\\d*+A-Z](?>{}*\\d){{5}}{}*[A-Z]|(?>{}*\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\d{10}',
            'group': '(?>{}*\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\dA-Z]\\\\d{7}[\\dA-Z]',
            'group': '[\\dA-Z](?>{}*\\d){{7}}{}*[\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\d{9}',
            'group': '(?>{}*\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\d{9}|\\d{12})',
            'group': '(?:(?>{}*\\d){{9}}|(?>{}*\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\d{2,10}',
            'group': '(?>{}*\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\dA-Z]{2}\\d{9}',
            'group': '(?>{}*[\\dA-Z]){{2}}(?>{}*\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\d{9}(?:\\d{3})?|GD[0-4]\\d{2}|HA[5-9]\\d{2})',
            'group': '(?:(?>{}*\\d){{9}}(?:(?>{}*\\d){{3}})?|GD[0-4](?>{}*\\d){{2}}|HA[5-9](?>{}*\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\d{12}',
            'group': '(?>{}*\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\d{11}',
            'group': '(?>{}*\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\d{8}',
            'group': '(?>{}*\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\d{9}B\\d{2}',
            'group': '(?>{}*\\d){{9}}{}*B(?>{}*\\\d){{2}}'
        }

    },

    Target.SCALA: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\\\d{8}',
            'group': '{}*U(?>{}*\\\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\\\d{9}',
            'group': '0(?>{}*\\\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\\\d{9,10}',
            'group': '(?>{}*\\\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\\\d{8}[A-Z]',
            'group': '(?>{}*\\\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\\\d{8,10}',
            'group': '(?>{}*\\\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\\\d[\\\\d*+A-Z]\\\\d{5}[A-Z]|\\\\d{7}[A-Z]{2})',
            'group': '(?:\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\\\dA-Z]\\\\d{7}[\\\\dA-Z]',
            'group': '[\\\\dA-Z](?>{}*\\\\d){{7}}{}*[\\\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\\\d{9}|\\\\d{12})',
            'group': '(?:(?>{}*\\\\d){{9}}|(?>{}*\\\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\\\d{2,10}',
            'group': '(?>{}*\\\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\\\dA-Z]{2}\\\\d{9}',
            'group': '(?>{}*[\\\\dA-Z]){{2}}(?>{}*\\\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\\\d{9}(?:\\\\d{3})?|GD[0-4]\\\\d{2}|HA[5-9]\\\\d{2})',
            'group': '(?:(?>{}*\\\\d){{9}}(?:(?>{}*\\\\d){{3}})?|GD[0-4](?>{}*\\\\d){{2}}|HA[5-9](?>{}*\\\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\\\d{12}',
            'group': '(?>{}*\\\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\\\d{9}B\\\\d{2}',
            'group': '(?>{}*\\\\d){{9}}{}*B(?>{}*\\\\d){{2}}'
        }

    },

    Target.KOTLIN: {

        'austria': {
            'code': 'AT',
            'noGroup': 'U\\\\d{8}',
            'group': '{}*U(?>{}*\\\\d){{8}}'
        },
        'belgium': {
            'code': 'BE',
            'noGroup': '0\\\\d{9}',
            'group': '0(?>{}*\\\\d){{9}}'
        },
        'bulgaria': {
            'code': 'BG',
            'noGroup': '\\\\d{9,10}',
            'group': '(?>{}*\\\\d){{9,10}}'
        },
        'cyprus': {
            'code': 'CY',
            'noGroup': '\\\\d{8}[A-Z]',
            'group': '(?>{}*\\\\d){{8}}{}*[A-Z]'
        },
        'czechRepublic': {
            'code': 'CZ',
            'noGroup': '\\\\d{8,10}',
            'group': '(?>{}*\\\\d){{8,10}}'
        },
        'germany': {
            'code': 'DE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'denmark': {
            'code': 'DK',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'slovakia': {
            'code': 'SK',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'estonia': {
            'code': 'EE',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'greece': {
            'code': '(?:EL|GR)',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'ireland': {
            'code': 'IE',
            'noGroup': '(?:\\\\d[\\\\d*+A-Z]\\\\d{5}[A-Z]|\\\\d{7}[A-Z]{2})',
            'group': '(?:\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'optionalCode': '(?:IE)?(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})',
            'requireCode': 'IE(?:{}*\\\\d{}*[\\\\d*+A-Z](?>{}*\\\\d){{5}}{}*[A-Z]|(?>{}*\\\\d){{7}}(?>{}*[A-Z]){{2}})'
        },
        'poland': {
            'code': 'PL',
            'noGroup': '\\\\d{10}',
            'group': '(?>{}*\\\\d){{10}}'
        },
        'spain': {
            'code': 'ES',
            'noGroup': '[\\\\dA-Z]\\\\d{7}[\\\\dA-Z]',
            'group': '[\\\\dA-Z](?>{}*\\\\d){{7}}{}*[\\\\dA-Z]'
        },
        'italy': {
            'code': 'IT',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'portugal': {
            'code': 'PT',
            'noGroup': '\\\\d{9}',
            'group': '(?>{}*\\\\d){{9}}'
        },
        'finland': {
            'code': 'FI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'lithuania': {
            'code': 'LT',
            'noGroup': '(?:\\\\d{9}|\\\\d{12})',
            'group': '(?:(?>{}*\\\\d){{9}}|(?>{}*\\\\d){{12}})'
        },
        'romania': {
            'code': 'RO',
            'noGroup': '\\\\d{2,10}',
            'group': '(?>{}*\\\\d){{2,10}}'
        },
        'france': {
            'code': 'FR',
            'noGroup': '[\\\\dA-Z]{2}\\\\d{9}',
            'group': '(?>{}*[\\\\dA-Z]){{2}}(?>{}*\\\\d){{9}}'
        },
        'luxembourg': {
            'code': 'LU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'unitedKingdom': {
            'code': 'GB',
            'noGroup': '(?:\\\\d{9}(?:\\\\d{3})?|GD[0-4]\\\\d{2}|HA[5-9]\\\\d{2})',
            'group': '(?:(?>{}*\\\\d){{9}}(?:(?>{}*\\\\d){{3}})?|GD[0-4](?>{}*\\\\d){{2}}|HA[5-9](?>{}*\\\\d){{2}})',
        },
        'latvia': {
            'code': 'LV',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'sweden': {
            'code': 'SE',
            'noGroup': '\\\\d{12}',
            'group': '(?>{}*\\\\d){{12}}'
        },
        'croatia': {
            'code': 'HR',
            'noGroup': '\\\\d{11}',
            'group': '(?>{}*\\\\d){{11}}'
        },
        'malta': {
            'code': 'MT',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },

        'slovenia': {
            'code': 'SI',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'hungary': {
            'code': 'HU',
            'noGroup': '\\\\d{8}',
            'group': '(?>{}*\\\\d){{8}}'
        },
        'netherlands': {
            'code': 'NL',
            'noGroup': '\\\\d{9}B\\\\d{2}',
            'group': '(?>{}*\\\\d){{9}}{}*B(?>{}*\\\\d){{2}}'
        }

    }

}

group_chars_to_re = {

    Target.JAVA: {
        'None'                 : '',
        'Space'                : ' ',
        'Dot'                  : '\\\\.',
        'Hyphen'               : '-',
        'Space and dot'        : '[ .]',
        'Space and hyphen'     : '[ -]',
        'Dot and hyphen'       : '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.PERL: {
        'None'                 : '',
        'Space'                : ' ',
        'Dot'                  : '\\.',
        'Hyphen'               : '-',
        'Space and dot'        : '[ .]',
        'Space and hyphen'     : '[ -]',
        'Dot and hyphen'       : '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.POSIX: {
        'None'                 : '',
        'Space'                : ' ',
        'Dot'                  : '\\.',
        'Hyphen'               : '-',
        'Space and dot'        : '[ .]',
        'Space and hyphen'     : '[ -]',
        'Dot and hyphen'       : '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.PYTHON: {
        'None': '',
        'Space': ' ',
        'Dot': '\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.JAVASCRIPT: {
        'None': '',
        'Space': ' ',
        'Dot': '\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.PHP: {
      'None': '',
      'Space': ' ',
      'Dot': '\\.',
      'Hyphen': '-',
      'Space and dot': '[ .]',
      'Space and hyphen': '[ -]',
      'Dot and hyphen': '[.-]',
      'Space, dot and hyphen': '[ .-]'
    },

    Target.GOLANG: {
        'None': '',
        'Space': ' ',
        'Dot': '\\\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.RUST: {
        'None': '',
        'Space': ' ',
        'Dot': '\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.CSHARP: {
        'None': '',
        'Space': ' ',
        'Dot': '\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.SCALA: {
        'None': '',
        'Space': ' ',
        'Dot': '\\\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    },

    Target.KOTLIN: {
        'None': '',
        'Space': ' ',
        'Dot': '\\\\.',
        'Hyphen': '-',
        'Space and dot': '[ .]',
        'Space and hyphen': '[ -]',
        'Dot and hyphen': '[.-]',
        'Space, dot and hyphen': '[ .-]'
    }

}

countries_with_two_groupings = {
    'austria',
    'cyprus',
    'lithuania',
    'france'
}
