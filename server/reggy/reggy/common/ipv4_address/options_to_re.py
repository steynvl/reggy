from reggy.samples.tokens import Target

ip_to_re = {

    Target.JAVA: {
        'Dotted 192.168.0.1'    : '[0-9]{1,3}\\\\.[0-9]{1,3}\\\\.[0-9]{1,3}\\\\.[0-9]{1,3}',
        'Decimal 3232235521'    : '429496729[0-5]|42949672[0-8][0-9]|4294967[01][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[01][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]',
        'Hexadecimal C0A8000'   : '[0-9a-f]{8}',
        'Hexadecimal C0A80001h' : '[0-9a-f]{8}h',
        'Hexadecimal 0xC0A80001': '0x[0-9a-f]{8}'
    },

    Target.PERL: {
        'Dotted 192.168.0.1': '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}',
        'Decimal 3232235521': '429496729[0-5]|42949672[0-8][0-9]|4294967[01][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[01][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]',
        'Hexadecimal C0A8000': '[0-9a-f]{8}',
        'Hexadecimal C0A80001h': '[0-9a-f]{8}h',
        'Hexadecimal 0xC0A80001': '0x[0-9a-f]{8}'
    },

    Target.POSIX: {
        'Dotted 192.168.0.1': '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}',
        'Decimal 3232235521': '429496729[0-5]|42949672[0-8][0-9]|4294967[01][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[01][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]',
        'Hexadecimal C0A8000': '[0-9a-f]{8}',
        'Hexadecimal C0A80001h': '[0-9a-f]{8}h',
        'Hexadecimal 0xC0A80001': '0x[0-9a-f]{8}'
    },

    Target.PYTHON: {
        'Dotted 192.168.0.1': '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}',
        'Decimal 3232235521': '429496729[0-5]|42949672[0-8][0-9]|4294967[01][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[01][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]',
        'Hexadecimal C0A8000': '[0-9a-f]{8}',
        'Hexadecimal C0A80001h': '[0-9a-f]{8}h',
        'Hexadecimal 0xC0A80001': '0x[0-9a-f]{8}'
    },

    Target.JAVASCRIPT: {
        'Dotted 192.168.0.1': '[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}',
        'Decimal 3232235521': '429496729[0-5]|42949672[0-8][0-9]|4294967[01][0-9]{2}|429496[0-6][0-9]{3}|42949[0-5][0-9]{4}|4294[0-8][0-9]{5}|429[0-3][0-9]{6}|42[0-8][0-9]{7}|4[01][0-9]{8}|[1-3][0-9]{9}|[1-9][0-9]{1,8}|[0-9]',
        'Hexadecimal C0A8000': '[0-9a-f]{8}',
        'Hexadecimal C0A80001h': '[0-9a-f]{8}h',
        'Hexadecimal 0xC0A80001': '0x[0-9a-f]{8}'
    }

}

