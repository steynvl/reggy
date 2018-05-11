class CreditCardInfo:

    def __init__(self, info):
        self._info             = info
        self.visa              = info['visa']
        self.diners_club       = info['dinersClub']
        self.master_card       = info['masterCard']
        self.discover          = info['discover']
        self.american_express  = info['americanExpress']
        self.jcb               = info['jcb']
        self.spaces_and_dashes = info['spacesAndDashes']

    def get_checked_credit_cards(self):
        return [
            k for k in self._info.keys() if k != 'spacesAndDashes' and self._info[k]
        ]
