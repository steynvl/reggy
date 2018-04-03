from collections import deque
import re

from regy.common_use_cases.email.options_to_re import username_to_re, domain_name_to_re


class Email:

    def __init__(self, info, target):
        self._split_semicolons = re.compile(r'(?<![\\]);')
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        mail_to_prefix = self._info['mailtoPrefix']
        if mail_to_prefix == 'Optional prefix':
            self._re.append('(?:mailto:)?+')
        elif mail_to_prefix == 'Require prefix':
            self._re.append('mailto:')

        us = self._info['username']
        if us == 'Specific user names only':
            self._re.append(self._parse_specific_field(key='specificUserNamesOnly'))
        else:
            us_to_re = username_to_re[self._target]
            self._re.append(us_to_re[us])

        self._re.append('@')

        domain_name = self._info['domainName']
        domain_to_re = domain_name_to_re[self._target]
        if domain_name == 'Specific domains only':
            self._re.append(self._parse_specific_field(key='specificDomainsOnly'))
        elif domain_name == 'Allow any domain on specific TLD':
            self._re.append(domain_to_re[domain_name].format(self._info['domainOnSpecificTld']))
        elif domain_name == 'Allow any subdomain on specific domain':
            self._re.append(domain_to_re[domain_name].format(self._info['anySubDomainOnSpecificDomain']))
        else:
            self._re.append(domain_to_re[domain_name])

    def _parse_specific_field(self, key):
        field = filter(lambda u: u != '', re.split(self._split_semicolons, self._info[key].strip()))
        field = [i.replace('\\;', ';') for i in field]

        if len(field) == 1:
            return field[0]
        else:
            return '(?:{})'.format('|'.join(field))
