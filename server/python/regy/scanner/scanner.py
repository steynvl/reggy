import json
from regy.tokens import MarkerType, MarkerTextInfo, RepeatInfo
from regy.utils import repeat_info_to_enum, number_to_enum_dict


class Scanner:

    def __init__(self, samples):
        self.samples = samples
        self._scanned_samples = []
        self._parse_samples()

    def get_scanned_samples(self):
        return self._scanned_samples

    @staticmethod
    def _insert_repeat_info(sample, info):
        repeat_info = sample['repeatInfo']['repeat']
        if repeat_info != 'Custom range':
            info['repeatInfo'] = repeat_info_to_enum[repeat_info]
        else:
            info['repeatInfo'] = RepeatInfo.CUSTOM_RANGE
            info['repeatRange'] = {
                'start': int(sample['repeatInfo']['start']),
                'end': int(sample['repeatInfo']['end'])
            }

    def _deserialize_samples(self):
        return json.loads(self.samples)

    def _parse_samples(self):
        samples_list = self._deserialize_samples()

        for sample in samples_list:
            info = {}
            if sample['markerType'] == 'Marked text':
                info['markerType'] = MarkerType.MARKED_TEXT
                self._parse_marked_text(sample, info)
            elif sample['markerType'] == 'Basic characters':
                info['markerType'] = MarkerType.BASIC_CHARACTERS
                self._parse_basic_characters(sample, info)
            elif sample['markerType'] == 'Numbers':
                info['markerType'] = MarkerType.NUMBERS
                self._parse_numbers(sample, info)

            self._scanned_samples.append(info)

    def _parse_marked_text(self, sample, info):
        info['strings'] = sample['markedStrings']
        info['markerInfo'] = []

        marker_info = sample['markerInfo']
        if marker_info['caseInsensitive']:
            info['markerInfo'].append(MarkerTextInfo.CASE_INSENSITIVE)
        else:
            info['markerInfo'].append(MarkerTextInfo.CASE_SENSITIVE)

        self._insert_repeat_info(sample, info)

    def _parse_basic_characters(self, sample, info):
        info['lowerCaseLetters'] = sample['lowerCaseLetters']
        info['upperCaseLetters'] = sample['upperCaseLetters']
        info['containsDigits'] = sample['containsDigits']
        info['matchAllExceptSpecified'] = sample['matchAllExceptSpecified']

        self._insert_repeat_info(sample, info)

    def _parse_numbers(self, sample, info):
        marker_info = sample['markerInfo']
        info['numbers'] = []
        for i in marker_info:
            if i != 'minus' and marker_info[i]:
                info['numbers'].append(number_to_enum_dict[i])
            else:
                info['minus'] = {
                    'minus'   : marker_info['minus']['minus'],
                    'optional': marker_info['minus']['optional']
                }

        self._insert_repeat_info(sample, info)
