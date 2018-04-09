from collections import deque

from regy.common_use_cases.models.vat_number_info import VatNumberInfo
from regy.common_use_cases.vat_number.options_to_re import vat_to_re, group_chars_to_re, countries_with_two_groupings


class VatNumber:

    def __init__(self, info: VatNumberInfo, target):
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        vat = vat_to_re[self._target]

        countries = self._info.get_checked_countries()
        country_code = self._info.country_code
        grouping_chars = self._info.grouping_characters
        grouping_chars_re = group_chars_to_re[self._target][grouping_chars]

        optional_code = country_code == 'Optional country code'
        require_code = country_code == 'Require country code'

        for country in countries:
            country_mappings = vat[country]

            if country == 'belgium' and country_code != 'No country code':
                self._add_regex_body(grouping_chars, country_mappings, grouping_chars_re)
                self._add_belgium_country_code(optional_code, country_mappings, grouping_chars_re)
            elif country == 'greece':
                self._add_regex_body(grouping_chars, country_mappings, grouping_chars_re)
                if country_code != 'No country code':
                    self._add_greece_country_code(optional_code, country_mappings)
            elif country == 'ireland':
                self._add_ireland_body_and_code(optional_code, require_code, country_mappings, grouping_chars, grouping_chars_re)
            elif country == 'spain':
                self._add_spain_body_and_code(optional_code, require_code, country_mappings, grouping_chars_re, grouping_chars)
            else:
                if grouping_chars == 'None':
                    self._re.append(country_mappings['noGroup'])
                else:
                    g = grouping_chars_re
                    if country in countries_with_two_groupings:
                        self._re.append(country_mappings['group'].format(g, g))
                    elif country == 'netherlands':
                        self._re.append(country_mappings['group'].format(g, g, g))
                    elif country == 'unitedKingdom':
                        self._re.append(country_mappings['group'].format(g, g, g, g))
                    else:
                        self._re.append(country_mappings['group'].format(g))

                if optional_code:
                    self._re.appendleft('(?:{})?'.format(country_mappings['code']))
                elif require_code:
                    self._re.appendleft(country_mappings['code'])

    def _add_regex_body(self, grouping_chars, country_mappings, grouping_chars_re):
        if grouping_chars == 'None':
            self._re.append(country_mappings['noGroup'])
        else:
            self._re.append(country_mappings['group'].format(grouping_chars_re))

    def _add_belgium_country_code(self, optional_code, country_mappings, grouping_chars_re):
        if optional_code:
            self._re.appendleft('(?:{})?{}*'.format(country_mappings['code'], grouping_chars_re))
        else:
            self._re.appendleft('{}{}*'.format(country_mappings['code'], grouping_chars_re))

    def _add_greece_country_code(self, optional_code, country_mappings):
        if optional_code:
            self._re.appendleft('?')
        self._re.appendleft(country_mappings['code'])

    def _add_ireland_body_and_code(self, optional_code, require_code, country_mappings, grouping_chars, grouping_chars_re):
        if optional_code:
            if grouping_chars == 'None':
                self._re.append('(?:{})?'.format(country_mappings['code']))
                self._re.append(country_mappings['noGroup'])
            else:
                g = grouping_chars_re
                self._re.append(country_mappings['optionalCode'].format(g, g, g, g, g, g))
        elif require_code:
            if grouping_chars == 'None':
                self._re.append('(?:{})'.format(country_mappings['code']))
                self._re.append(country_mappings['noGroup'])
            else:
                g = grouping_chars_re
                self._re.append(country_mappings['requireCode'].format(g, g, g, g, g, g))
        else:
            if grouping_chars == 'None':
                self._re.append(country_mappings['noGroup'])
            else:
                g = grouping_chars_re
                self._re.append(country_mappings['group'].format(g, g, g, g, g, g))

    def _add_spain_body_and_code(self, optional_code, require_code, country_mappings, grouping_chars_re, grouping_chars):
        if grouping_chars == 'None':
            self._re.append(country_mappings['noGroup'])
        else:
            self._re.append(country_mappings['group'].format(grouping_chars_re, grouping_chars_re))

        if optional_code:
            if grouping_chars == 'None':
                self._re.appendleft('(?:{})?'.format(country_mappings['code']))
            else:
                self._re.appendleft('(?:{})?{}*'.format(country_mappings['code'], grouping_chars_re))
        elif require_code:
            if grouping_chars == 'None':
                self._re.appendleft(country_mappings['code'])
            else:
                self._re.appendleft('{}{}*'.format(country_mappings['code'], grouping_chars_re))

