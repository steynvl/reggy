from regy.common.guid.options_to_re import braces_to_re, case_to_re
from regy.common.models.guid_info import GuidInfo


class Guid:

    def __init__(self, info: GuidInfo, target):
        self._info = info
        self._target = target
        self._re = []
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        case_char_class = case_to_re[self._target][self._info.guid_case]

        hyphens_in = self._info.hyphens_in
        if hyphens_in == 'Required':
            self._re.append('-'.join(['{}{{{}}}'.format(case_char_class, i) for i in ['8', '4', '4', '4', '12']]))
        elif hyphens_in == 'Optional':
            self._re.append('(?:')
            self._re.append('{}{{32}}'.format(case_char_class))
            self._re.append('|')
            self._re.append('-'.join(['{}{{{}}}'.format(case_char_class, i) for i in ['8', '4', '4', '4', '12']]))
            self._re.append(')')
        elif hyphens_in == 'Not allowed':
            self._re.append('{}{{32}}'.format(case_char_class))

        braces = braces_to_re[self._target]
        braces_around = self._info.braces_around
        if braces_around == 'Required':
            self._re = [braces[braces_around] % ''.join(self._re)]
        elif braces_around == 'Optional':
            re_body = ''.join(self._re)
            self._re = [braces[braces_around] % (re_body, re_body)]
