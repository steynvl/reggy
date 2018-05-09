from collections import deque

from regy.common_use_cases.credt_card_number.credit_card_number import CreditCardNumber
from regy.common_use_cases.currency.currency import Currency
from regy.common_use_cases.date_and_time.date_and_time import DateAndTime
from regy.common_use_cases.email.email import Email
from regy.common_use_cases.guid.guid import Guid
from regy.common_use_cases.ipv4_address.ipv4_address import Ipv4Address
from regy.common_use_cases.models.credit_card_info import CreditCardInfo
from regy.common_use_cases.models.currency_info import CurrencyInfo
from regy.common_use_cases.models.date_and_time_info import DateAndTimeInfo
from regy.common_use_cases.models.email_info import EmailInfo
from regy.common_use_cases.models.guid_info import GuidInfo
from regy.common_use_cases.models.ipv4_info import Ipv4Info
from regy.common_use_cases.models.national_id_info import NationalIdInfo
from regy.common_use_cases.models.password_info import PasswordInfo
from regy.common_use_cases.models.url_info import UrlInfo
from regy.common_use_cases.models.username_info import UsernameInfo
from regy.common_use_cases.models.vat_number_info import VatNumberInfo
from regy.common_use_cases.national_id.national_id import NationalId
from regy.common_use_cases.password.password import Password
from regy.common_use_cases.url.url import Url
from regy.common_use_cases.username import Username
from regy.common_use_cases.vat_number.vat_number import VatNumber
from regy.samples_and_semantics.mapper.end_info_to_target import end_info_to_target
from regy.samples_and_semantics.mapper.start_info_to_target import start_info_to_target
from regy.samples_and_semantics.tokens import Token, Target
from regy.samples_and_semantics.utils.language_to_tok import language_to_tok
from regy.samples_and_semantics.utils.regex_end_info_to_tok import regex_end_info_to_tok
from regy.samples_and_semantics.utils.regex_start_info_to_tok import regex_start_info_to_tok


class CommonUseCases:

    def __init__(self, samples):
        self._samples = samples
        self._re = None
        self._calculate_regex()

    def get_re(self):
        return self._re

    def _parse_general_regex_info(self):
        general_info = self._samples['generalRegexInfo']

        self._lang_info = {
            Token.TARGET           : language_to_tok[general_info['regexTarget']],
            Token.REGEX_START_INFO : regex_start_info_to_tok[general_info['startRegexMatchAt']],
            Token.REGEX_END_INFO   : regex_end_info_to_tok[general_info['endRegexMatchAt']]
        }

    def _calculate_regex(self):
        self._parse_general_regex_info()

        sample_type = self._samples['type']
        info = self._samples['information']
        regex = deque()

        if sample_type == 'Username':
            username_info = UsernameInfo(info)
            regex.append(Username(username_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'Password':
            password_info = PasswordInfo(info)
            regex.append(Password(password_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'Email address':
            email_info = EmailInfo(info)
            regex.append(Email(email_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'URL':
            url_info = UrlInfo(info)
            regex.append(Url(url_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'GUID':
            guid_info = GuidInfo(info)
            regex.append(Guid(guid_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'Credit card number':
            credit_card_info = CreditCardInfo(info)
            regex.append(CreditCardNumber(credit_card_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'National ID':
            national_id_info = NationalIdInfo(info)
            regex.append(NationalId(national_id_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'VAT number':
            vat_number_info = VatNumberInfo(info)
            regex.append(VatNumber(vat_number_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'IPv4 address':
            ipv4_info = Ipv4Info(info)
            regex.append(Ipv4Address(ipv4_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'Currency':
            currency_info = CurrencyInfo(info)
            regex.append(Currency(currency_info, self._lang_info[Token.TARGET]).get_re())
        elif sample_type == 'Date and time':
            date_and_time_info = DateAndTimeInfo(info)
            regex.append(DateAndTime(date_and_time_info, self._lang_info[Token.TARGET]).get_re())

        self._add_general_info(regex)

        regex = ''.join(regex).strip()
        self._map_re_to_target(regex, self._lang_info[Token.TARGET])

    def _map_re_to_target(self, regex, target):
        self._re = { 'regex': regex }

        compiled_re = None
        if target == Target.JAVA:
            compiled_re = 'Pattern regex = Pattern.compile("{}");'.format(regex)
        elif target == Target.PERL:
            compiled_re = '/{}/'.format(regex)
        elif target == Target.POSIX:
            compiled_re = regex[:]

        self._re['compiledRegex'] = compiled_re

    def _add_general_info(self, regex):
        start_info_to_re = start_info_to_target[self._lang_info[Token.TARGET]]
        end_info_to_re = end_info_to_target[self._lang_info[Token.TARGET]]

        regex.appendleft(start_info_to_re[self._lang_info[Token.REGEX_START_INFO]])
        regex.append(end_info_to_re[self._lang_info[Token.REGEX_END_INFO]])
