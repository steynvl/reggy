from collections import deque

from regy.common_use_cases.credt_card_number.credit_card_number import CreditCardNumber
from regy.common_use_cases.email.email import Email
from regy.common_use_cases.guid.guid import Guid
from regy.common_use_cases.national_id.national_id import NationalId
from regy.common_use_cases.password.password import Password
from regy.common_use_cases.url.url import Url
from regy.common_use_cases.username import Username
from regy.samples_and_semantics.mapper.end_info_to_target import end_info_to_target
from regy.samples_and_semantics.mapper.start_info_to_target import start_info_to_target
from regy.samples_and_semantics.tokens import Token
from regy.samples_and_semantics.utils.language_to_tok import language_to_tok
from regy.samples_and_semantics.utils.regex_end_info_to_tok import regex_end_info_to_tok
from regy.samples_and_semantics.utils.regex_start_info_to_tok import regex_start_info_to_tok


class CommonUseCases:

    def __init__(self, samples):
        self._samples = samples
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re).strip()

    def _parse_general_regex_info(self):
        general_info = self._samples['generalRegexInfo']

        self._lang_info = {
            Token.TARGET           : language_to_tok[general_info['regexTarget']],
            Token.REGEX_START_INFO : regex_start_info_to_tok[general_info['startRegexMatchAt']],
            Token.REGEX_END_INFO   : regex_end_info_to_tok[general_info['endRegexMatchAt']]
        }

    def _calculate_regex(self):
        self._parse_general_regex_info()

        if self._samples['type'] == 'Username':
            self._re.append(Username(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'Password':
            self._re.append(Password(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'Email address':
            self._re.append(Email(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'URL':
            self._re.append(Url(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'GUID':
            self._re.append(Guid(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'Credit card number':
            self._re.append(CreditCardNumber(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'National ID':
            self._re.append(NationalId(self._samples['information'], self._lang_info[Token.TARGET]).get_re())
        elif self._samples['type'] == 'VAT number':
            self._re.append(VatNumber(self._samples['information'], self._lang_info[Token.TARGET]).get_re())

        self._add_general_info()

    def _add_general_info(self):
        start_info_to_re = start_info_to_target[self._lang_info[Token.TARGET]]
        end_info_to_re = end_info_to_target[self._lang_info[Token.TARGET]]

        self._re.appendleft(start_info_to_re[self._lang_info[Token.REGEX_START_INFO]])
        self._re.append(end_info_to_re[self._lang_info[Token.REGEX_END_INFO]])
