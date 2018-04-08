from collections import deque
import re
from regy.common_use_cases.url.options_to_re import url_to_re


class Url:

    def __init__(self, info, target):
        self._split_semicolons = re.compile(r'(?<![\\]);')
        self._info = info
        self._target = target
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        target = url_to_re[self._target]

        scheme_to_re   = target['scheme']
        username_to_re = target['username']
        password_to_re = target['password']
        domain_to_re   = target['host']
        port_nr_to_re  = target['portNumbers']
        folders_to_re  = target['folders']
        files_to_re    = target['fileNames']
        param_to_re    = target['parameters']


        self._re.append(scheme_to_re[self._info['scheme']])

        if self._info['password'] == 'No password':
            if self._info['username'] == 'Specific user names only':
                self._re.append(self._parse_specific_field(self._info['specUserNames']))
                self._re.append('@')
            elif self._info['username'] != 'No user names':
                self._re.append(username_to_re[self._info['username']].format('@', ')'))
        else:
            if self._info['username'] == 'Specific user names only':
                self._re.append(password_to_re['specUserOptionalPassword'])
            elif self._info['username'] != 'No user names':
                self._re.append(username_to_re[self._info['username']].format('', ''))

            if self._info['password'] == 'Optional password':
                self._re.append(password_to_re['specUserOptionalPassword'])
            elif self._info['password'] == 'Require password':
                self._re.append(password_to_re['specUserRequirePassword'])

        if self._info['domainName'] == 'Specific domains only':
            pass
        else:
            self._re.append('')

        port_nrs = self._info['portNumbers']
        if port_nrs == 'Optional port numbers' or port_nrs == 'Require port numbers':
            self._re.append(port_nr_to_re[port_nrs])
        elif port_nrs == 'Specify optional port numbers':
            alternation = self._alternate_sequence(self._info['specOptionalPortNumbers'])
            self._re.append(port_nr_to_re[port_nrs].format(alternation))
        elif port_nrs == 'Specify required port numbers':
            alternation = self._alternate_sequence(self._info['specRequiredPortNumbers'])
            self._re.append(port_nr_to_re[port_nrs].format(alternation))

        folders = self._info['folders']
        if folders != 'No folders':
            if folders == 'Specific folders only':
                spec_folders = self._parse_specific_field(self._info['specFoldersOnly'])
                self._re.append(folders_to_re[folders].format(spec_folders))
            elif folders == 'Specific paths only':
                spec_paths = self._parse_specific_field(self._info['specPathsOnly'])
                self._re.append(folders_to_re[folders].format(spec_paths))
            else:
                self._re.append(folders_to_re[folders])

            min_depth = int(self._info['minFolderDepth'])
            max_depth = int(self._info['maxFolderDepth'])
            self._re.append(self._get_folder_depth_range(min_depth, max_depth))

        files = self._info['fileNames']
        if files != 'No file names':
            option = 'optional' if self._info['optionalFileNames'] else 'required'
            if files == 'Specific extensions only':
                file_extensions = self._alternate_sequence(self._info['specExtensions'])
                self._re.append(files_to_re[option][file_extensions])
            elif files == 'Specific file names only':
                file_names = self._alternate_sequence(self._info['specFileNames'])
                self._re.append(files_to_re[option][file_names])
            else:
                self._re.append(files_to_re[option][files])

        parameters = self._info['parameters']
        if parameters != 'No parameters':
            if parameters == 'Specific parameters only':
                pass
            else:
                self._re.append(param_to_re[parameters])

    def _parse_specific_field(self, values):
        field = filter(lambda u: u != '', re.split(self._split_semicolons, values))
        field = [i.replace('\\;', ';') for i in field]

        if len(field) == 1:
            return field[0]
        else:
            return '(?:{})'.format('|'.join(field))

    @staticmethod
    def _alternate_sequence(seq):
        if len(seq) == 0:
            return ''
        elif len(seq) == 1:
            return seq[0]

        return '(?:{})'.format('|'.join(seq))

    @staticmethod
    def _get_folder_depth_range(min_val, max_val):
        if min_val == 0 and max_val == 1:
            return '?'
        elif min_val == 1 and max_val == 1:
            return ''
        elif min_val == max_val:
            return '{{{}}}'.format(min_val)
        else:
            return '{{{},{}}}'.format(min_val, max_val)
