class Ipv4Info:

    def __init__(self, info):
        self._info        = info
        self.dotted       = info['dotted']
        self.decimal      = info['decimal']
        self.hexadecimal1 = info['hexadecimal1']
        self.hexadecimal2 = info['hexadecimal2']
        self.hexadecimal3 = info['hexadecimal3']

        self._field_to_key = {
            'dotted'      : 'Dotted 192.168.0.1',
            'decimal'     : 'Decimal 3232235521',
            'hexadecimal1': 'Hexadecimal C0A8000',
            'hexadecimal2': 'Hexadecimal C0A80001h',
            'hexadecimal3': 'Hexadecimal 0xC0A80001'
        }

    def get_checked_options(self):
        return [self._field_to_key[option] for option in self._field_to_key.keys() if self._info[option]]
