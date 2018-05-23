from collections import deque

from regy.common.credt_card_number.credit_card_number import CreditCardNumber
from regy.common.currency.currency import Currency
from regy.common.date_and_time.date_and_time import DateAndTime
from regy.common.email.email import Email
from regy.common.guid.guid import Guid
from regy.common.ipv4_address.ipv4_address import Ipv4Address
from regy.common.models.credit_card_info import CreditCardInfo
from regy.common.models.currency_info import CurrencyInfo
from regy.common.models.date_and_time_info import DateAndTimeInfo
from regy.common.models.email_info import EmailInfo
from regy.common.models.guid_info import GuidInfo
from regy.common.models.ipv4_info import Ipv4Info
from regy.common.models.national_id_info import NationalIdInfo
from regy.common.models.password_info import PasswordInfo
from regy.common.models.url_info import UrlInfo
from regy.common.models.username_info import UsernameInfo
from regy.common.models.vat_number_info import VatNumberInfo
from regy.common.national_id.national_id import NationalId
from regy.common.password.password import Password
from regy.common.url.url import Url
from regy.common.username import Username
from regy.common.vat_number.vat_number import VatNumber
from regy.samples.constants.end_info_to_target import end_info_to_target
from regy.samples.constants.start_info_to_target import start_info_to_target
from regy.samples.tokens import Target
from regy.samples.utils.regex_info_to_tok import regex_info_to_tok


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
            'target'   : regex_info_to_tok[general_info['regexTarget']],
            'startInfo': regex_info_to_tok[general_info['startRegexMatchAt']],
            'endInfo'  : regex_info_to_tok[general_info['endRegexMatchAt']]
        }

    def _calculate_regex(self):
        self._parse_general_regex_info()

        sample_type = self._samples['type']
        info = self._samples['information']
        target = self._lang_info['target']
        regex = deque()

        if sample_type == 'Username':
            username_info = UsernameInfo(info)
            regex.append(Username(username_info, target).get_re())
        elif sample_type == 'Password':
            password_info = PasswordInfo(info)
            regex.append(Password(password_info, target).get_re())
        elif sample_type == 'Email address':
            email_info = EmailInfo(info)
            regex.append(Email(email_info, target).get_re())
        elif sample_type == 'URL':
            url_info = UrlInfo(info)
            regex.append(Url(url_info, target).get_re())
        elif sample_type == 'GUID':
            guid_info = GuidInfo(info)
            regex.append(Guid(guid_info, target).get_re())
        elif sample_type == 'Credit card number':
            credit_card_info = CreditCardInfo(info)
            regex.append(CreditCardNumber(credit_card_info, target).get_re())
        elif sample_type == 'National ID':
            national_id_info = NationalIdInfo(info)
            regex.append(NationalId(national_id_info, target).get_re())
        elif sample_type == 'VAT number':
            vat_number_info = VatNumberInfo(info)
            regex.append(VatNumber(vat_number_info, target).get_re())
        elif sample_type == 'IPv4 address':
            ipv4_info = Ipv4Info(info)
            regex.append(Ipv4Address(ipv4_info, target).get_re())
        elif sample_type == 'Currency':
            currency_info = CurrencyInfo(info)
            regex.append(Currency(currency_info, target).get_re())
        elif sample_type == 'Date and time':
            date_and_time_info = DateAndTimeInfo(info)
            regex.append(DateAndTime(date_and_time_info, target).get_re())

        self._add_general_info(regex)

        regex = ''.join(regex).strip()
        self._map_re_to_target(regex, target)

    def _map_re_to_target(self, regex, target):
        self._re = { 'regex': regex }

        compiled_re = None
        if target == Target.JAVA:
            compiled_re = 'Pattern regex = Pattern.compile("{}");'.format(regex)
        elif target == Target.PERL:
            compiled_re = ' my $regex = /{}/;'.format(regex)
        elif target == Target.POSIX:
            compiled_re = regex[:]

        self._re['compiledRegex'] = compiled_re

    def _add_general_info(self, regex):
        target = self._lang_info['target']
        start_info_to_re = start_info_to_target[target]
        end_info_to_re = end_info_to_target[target]

        regex.appendleft(start_info_to_re[self._lang_info['startInfo']])
        regex.append(end_info_to_re[self._lang_info['endInfo']])
