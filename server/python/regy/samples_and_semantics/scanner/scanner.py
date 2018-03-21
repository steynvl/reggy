import json
import re
from collections import OrderedDict

from regy.samples_and_semantics.tokens.basic_characters_info import BasicCharactersInfo
from regy.samples_and_semantics.tokens.token import Token
from regy.samples_and_semantics.tokens import MarkerType, MarkerTextInfo, RepeatInfo
from regy.samples_and_semantics.utils.repeat_info_to_enum import repeat_info_to_enum
from regy.samples_and_semantics.utils.number_to_enum import number_to_enum_dict
from regy.samples_and_semantics.utils.language_to_tok import language_to_tok
from regy.samples_and_semantics.utils.regex_start_info_to_tok import regex_start_info_to_tok
from regy.samples_and_semantics.utils.regex_end_info_to_tok import regex_end_info_to_tok

class Scanner:

    def __init__(self, samples):
        self.samples = samples
        self._scanned_samples = {}
        self._parse_samples()

    def get_scanned_samples(self):
        return self._scanned_samples

    @staticmethod
    def _insert_repeat_info(samples, info):
        repeat_info = samples['repeatInfo']['repeat']

        if repeat_info == 'Custom range':
            info[Token.REPEAT_INFO] = RepeatInfo.CUSTOM_RANGE
            info[Token.REPEAT_RANGE] = {
                Token.REPEAT_START: int(samples['repeatInfo']['start']),
                Token.REPEAT_END  : int(samples['repeatInfo']['end']),
            }
        elif repeat_info == 'n or more times':
            info[Token.REPEAT_INFO] = RepeatInfo.N_OR_MORE_TIMES
            info[Token.REPEAT_RANGE] = {
                Token.REPEAT_START: int(samples['repeatInfo']['start'])
            }
        else:
            info[Token.REPEAT_INFO] = repeat_info_to_enum[repeat_info]


    def _deserialize_samples(self):
        return json.loads(self.samples)

    def _parse_samples(self):
        samples_info = self._deserialize_samples()
        self._parse_general_regex_info(samples_info['generalRegexInfo'])

        self._scanned_samples[Token.SAMPLE_STRINGS_INFO] = []

        for sample in samples_info['sampleStringsInfo']:
            info = {}
            if sample['markerType'] == 'Marked text':
                info[Token.MARKER_TYPE] = MarkerType.MARKED_TEXT
                self._parse_marked_text(sample, info)
            elif sample['markerType'] == 'Basic characters':
                info[Token.MARKER_TYPE] = MarkerType.BASIC_CHARACTERS
                self._parse_basic_characters(sample, info)
            elif sample['markerType'] == 'Numbers':
                info[Token.MARKER_TYPE] = MarkerType.NUMBERS
                self._parse_numbers(sample, info)

            self._scanned_samples[Token.SAMPLE_STRINGS_INFO].append(info)

    def _parse_marked_text(self, sample, info):
        info[Token.MARKED_TEXT_STRINGS] = sample['markedStrings']
        info[Token.MARKER_INFO] = []

        marker_info = sample['markerInfo']
        if marker_info['caseInsensitive']:
            info[Token.MARKER_INFO].append(MarkerTextInfo.CASE_INSENSITIVE)
        else:
            info[Token.MARKER_INFO].append(MarkerTextInfo.CASE_SENSITIVE)

        self._insert_repeat_info(sample, info)

    def _parse_basic_characters(self, sample, info):
        marker_info = sample['markerInfo']

        info[BasicCharactersInfo.CASE_INSENSITIVE]           = marker_info['caseInsensitive']
        info[BasicCharactersInfo.LOWER_CASE_LETTERS]         = marker_info['lowerCaseLetters']
        info[BasicCharactersInfo.UPPER_CASE_LETTERS]         = marker_info['upperCaseLetters']
        info[BasicCharactersInfo.DIGITS]                     = marker_info['digits']
        info[BasicCharactersInfo.PUNCTUATION_AND_SYMBOLS]    = marker_info['punctuationAndSymbols']
        info[BasicCharactersInfo.MATCH_ALL_EXCEPT_SPECIFIED] = marker_info['matchAllExceptSpecified']
        info[BasicCharactersInfo.WHITE_SPACE]                = marker_info['whiteSpace']
        info[BasicCharactersInfo.LINE_BREAKS]                = marker_info['lineBreaks']

        individual_chars = marker_info['individualCharacters']
        distinct_chars = ''.join(OrderedDict.fromkeys(re.sub(r'\s', '', individual_chars)))
        info[BasicCharactersInfo.INDIVIDUAL_CHARACTERS] = distinct_chars

        self._insert_repeat_info(sample, info)

    def _parse_numbers(self, sample, info):
        marker_info = sample['markerInfo']
        info[Token.NUMBERS] = []
        for i in marker_info:
            if i != 'minus' and marker_info[i]:
                info[Token.NUMBERS].append(number_to_enum_dict[i])
            else:
                info[Token.MINUS_INFO] = {
                    Token.INCLUDE_MINUS         : marker_info['minus']['minus'],
                    Token.INCLUDE_OPTIONAL_MINUS: marker_info['minus']['optional']
                }

        self._insert_repeat_info(sample, info)

    def _parse_general_regex_info(self, regex_info):
        self._scanned_samples[Token.GENERAL_REGEX_INFO] = {
            Token.TARGET_LANGUAGE : language_to_tok[regex_info['regexTarget']],
            Token.REGEX_START_INFO: regex_start_info_to_tok[regex_info['startRegexMatchAt']],
            Token.REGEX_END_INFO  : regex_end_info_to_tok[regex_info['endRegexMatchAt']]
        }