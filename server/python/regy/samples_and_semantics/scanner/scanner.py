import json
import re
from collections import OrderedDict

from regy.samples_and_semantics.tokens.basic_characters_ import BasicCharacters
from regy.samples_and_semantics.tokens.control_characters import control_char_to_token, control_chars
from regy.samples_and_semantics.tokens.token import Token
from regy.samples_and_semantics.tokens import MarkerType, MarkedText, RepeatInfo
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

    def _parse_samples(self):
        self._parse_general_regex_info(self.samples['generalRegexInfo'])

        self._scanned_samples[Token.SAMPLE_STRINGS_INFO] = []

        for sample in self.samples['sampleStringsInfo']:
            info = {}
            marker_type = sample['markerType']

            if marker_type == 'Marked text':
                info[Token.MARKER_TYPE] = MarkerType.MARKED_TEXT
                self._parse_marked_text(sample, info)
            elif marker_type == 'Basic characters':
                info[Token.MARKER_TYPE] = MarkerType.BASIC_CHARACTERS
                self._parse_basic_characters(sample, info)
            elif marker_type == 'Numbers':
                info[Token.MARKER_TYPE] = MarkerType.NUMBERS
                self._parse_numbers(sample, info)
            elif marker_type == 'Control characters':
                info[Token.MARKER_TYPE] = MarkerType.CONTROL_CHARACTERS
                self._parse_control_characters(sample, info)

            self._scanned_samples[Token.SAMPLE_STRINGS_INFO].append(info)

    def _parse_marked_text(self, sample, info):
        info[Token.MARKED_TEXT_STRINGS] = sample['markedStrings']
        info[Token.MARKER_INFO] = []

        marker_info = sample['markerInfo']
        if marker_info['caseInsensitive']:
            info[Token.MARKER_INFO].append(MarkedText.CASE_INSENSITIVE)
        else:
            info[Token.MARKER_INFO].append(MarkedText.CASE_SENSITIVE)

        self._insert_repeat_info(sample, info)

    def _parse_basic_characters(self, sample, info):
        marker_info = sample['markerInfo']

        info[BasicCharacters.CASE_INSENSITIVE]           = marker_info['caseInsensitive']
        info[BasicCharacters.LOWER_CASE_LETTERS]         = marker_info['lowerCaseLetters']
        info[BasicCharacters.UPPER_CASE_LETTERS]         = marker_info['upperCaseLetters']
        info[BasicCharacters.DIGITS]                     = marker_info['digits']
        info[BasicCharacters.PUNCTUATION_AND_SYMBOLS]    = marker_info['punctuationAndSymbols']
        info[BasicCharacters.MATCH_ALL_EXCEPT_SPECIFIED] = marker_info['matchAllExceptSpecified']
        info[BasicCharacters.WHITE_SPACE]                = marker_info['whiteSpace']
        info[BasicCharacters.LINE_BREAKS]                = marker_info['lineBreaks']

        individual_chars = marker_info['individualCharacters']
        distinct_chars = ''.join(OrderedDict.fromkeys(re.sub(r'\s', '', individual_chars)))
        info[BasicCharacters.INDIVIDUAL_CHARACTERS] = distinct_chars

        self._insert_repeat_info(sample, info)

    def _parse_numbers(self, sample, info):
        marker_info = sample['markerInfo']
        info[Token.NUMBERS] = []
        for i in marker_info:
            if i != 'minus' and marker_info[i]:
                info[Token.NUMBERS].append(number_to_enum_dict[i])
            else:
                minus_info = marker_info['minus']
                info[Token.MINUS_INFO] = {
                    Token.INCLUDE_MINUS         : minus_info['minus'],
                    Token.INCLUDE_OPTIONAL_MINUS: minus_info['optional']
                }

        self._insert_repeat_info(sample, info)

    def _parse_control_characters(self, sample, info):
        marker_info = sample['markerInfo']
        match_all_except_spec = marker_info['matchAllExceptSelectedOnes']

        wanted_control_chars = []

        for control_char in control_chars:
            if not match_all_except_spec and marker_info[control_char]:
                wanted_control_chars.append(control_char_to_token[control_char])
            elif match_all_except_spec and not marker_info[control_char]:
                wanted_control_chars.append(control_char_to_token[control_char])

        info[Token.CONTROL_CHARACTERS] = wanted_control_chars

        self._insert_repeat_info(sample, info)

    def _parse_general_regex_info(self, regex_info):
        self._scanned_samples[Token.GENERAL_REGEX_INFO] = {
            Token.TARGET_LANGUAGE : language_to_tok[regex_info['regexTarget']],
            Token.REGEX_START_INFO: regex_start_info_to_tok[regex_info['startRegexMatchAt']],
            Token.REGEX_END_INFO  : regex_end_info_to_tok[regex_info['endRegexMatchAt']]
        }

    @staticmethod
    def _insert_repeat_info(samples, info):
        repeat_info = samples['repeatInfo']['repeat']

        if repeat_info == 'Custom range':
            info[Token.REPEAT_INFO] = RepeatInfo.CUSTOM_RANGE
            info[Token.REPEAT_RANGE] = {
                Token.REPEAT_START: int(samples['repeatInfo']['start']),
                Token.REPEAT_END: int(samples['repeatInfo']['end']),
            }
        elif repeat_info == 'n or more times':
            info[Token.REPEAT_INFO] = RepeatInfo.N_OR_MORE_TIMES
            info[Token.REPEAT_RANGE] = {
                Token.REPEAT_START: int(samples['repeatInfo']['start'])
            }
        else:
            info[Token.REPEAT_INFO] = repeat_info_to_enum[repeat_info]
