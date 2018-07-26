from collections import deque

from reggy.common.credt_card_number.credit_card_number import CreditCardNumber
from reggy.common.currency.currency import Currency
from reggy.common.date_and_time.date_and_time import DateAndTime
from reggy.common.email.email import Email
from reggy.common.guid.guid import Guid
from reggy.common.ipv4_address.ipv4_address import Ipv4Address
from reggy.common.models.credit_card_info import CreditCardInfo
from reggy.common.models.currency_info import CurrencyInfo
from reggy.common.models.date_and_time_info import DateAndTimeInfo
from reggy.common.models.email_info import EmailInfo
from reggy.common.models.guid_info import GuidInfo
from reggy.common.models.ipv4_info import Ipv4Info
from reggy.common.models.national_id_info import NationalIdInfo
from reggy.common.models.password_info import PasswordInfo
from reggy.common.models.url_info import UrlInfo
from reggy.common.models.username_info import UsernameInfo
from reggy.common.models.vat_number_info import VatNumberInfo
from reggy.common.national_id.national_id import NationalId
from reggy.common.password.password import Password
from reggy.common.url.url import Url
from reggy.common.username import Username
from reggy.common.vat_number.vat_number import VatNumber
from reggy.samples.constants.end_info_to_target import end_info_to_target
from reggy.samples.constants.start_info_to_target import start_info_to_target
from reggy.samples.tokens import Target
from reggy.samples.utils.regex_info_to_tok import regex_info_to_tok


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
        elif target == Target.PYTHON:
            compiled_re = 'regex = re.compile(r\'{}\')'.format(regex)
        elif target == Target.JAVASCRIPT:
            compiled_re = 'const regex = /{}/;'.format(regex)
        elif target == Target.PHP:
            compiled_re = '$regex = \'/{}/\';'.format(regex)
        elif target == Target.GOLANG:
            compiled_re = 'regex, _ := regexp.Compile("{}")'.format(regex)
        elif target == Target.RUST:
            compiled_re = 'let re = Regex::new(r"{}").unwrap();'.format(regex)

        self._re['compiledRegex'] = compiled_re

    def _add_general_info(self, regex):
        target = self._lang_info['target']
        start_info_to_re = start_info_to_target[target]
        end_info_to_re = end_info_to_target[target]

        regex.appendleft(start_info_to_re[self._lang_info['startInfo']])
        regex.append(end_info_to_re[self._lang_info['endInfo']])
