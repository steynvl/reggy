from regy.common_use_cases.credt_card_number.options_to_re import credit_card_to_re


class CreditCardNumber:

    def __init__(self, info, target):
        self._info = info
        self._target = target
        self._re = []
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        credit_cards = self._get_checked_credit_cards()

        card_format_info = self._info['spacesAndDashes']
        target = credit_card_to_re[self._target]

        for credit_card in credit_cards:
            self._re.append(target[credit_card][card_format_info])

        if len(credit_cards) > 1:
            self._re = ['|'.join(self._re)]

    def _get_checked_credit_cards(self):
        return [
            k for k in self._info.keys() if k != 'spacesAndDashes' and self._info[k]
        ]
