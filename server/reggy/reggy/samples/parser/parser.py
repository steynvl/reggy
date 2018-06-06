from reggy.samples.models.basic_characters_info import BasicCharactersInfo
from reggy.samples.models.control_characters_info import ControlCharactersInfo
from reggy.samples.models.digits_info import DigitsInfo
from reggy.samples.models.list_of_literal_text_info import ListOfLiteralTextInfo
from reggy.samples.models.literal_text_info import LiteralTextInfo
from reggy.samples.models.match_anything_info import MatchAnythingInfo
from reggy.samples.models.numbers_info import NumbersInfo
from reggy.samples.models.unicode_characters_info import UnicodeCharactersInfo
from reggy.samples.parser.samples import Samples
from reggy.samples.constants.control_characters import control_char_to_token, control_chars
from reggy.samples.constants.match_anything import basic_char_to_tok
from reggy.samples.tokens.repetition import Repetition
from reggy.samples.tokens import LiteralTextTok
from reggy.samples.constants.unicode_characters import unicode_chars, unicode_char_to_token
from reggy.samples.utils.regex_info_to_tok import regex_info_to_tok
from reggy.samples.utils.repetition_info_to_enum import repetition_info_to_enum
from reggy.samples.utils.digit_to_enum import digit_to_enum


class Parser:

    def __init__(self, regex_info):
        self._samples = Samples()
        self._parse_samples(regex_info)

    def get_parsed_samples(self):
        return self._samples

    def _parse_samples(self, regex_info):
        self._parse_general_regex_info(regex_info)

        for group in regex_info['sampleStringsInfo']:
            self._alternating_group = []

            for sample in group:
                marker_type = sample['markerType']

                if marker_type == 'Literal text':
                    self._parse_literal_text(sample)
                elif marker_type == 'Basic characters':
                    self._parse_basic_characters(sample)
                elif marker_type == 'Digits':
                    self._parse_digits(sample)
                elif marker_type == 'Control characters':
                    self._parse_control_characters(sample)
                elif marker_type == 'Unicode characters':
                    self._parse_unicode_characters(sample)
                elif marker_type == 'Match anything':
                    self._parse_match_anything(sample)
                elif marker_type == 'List of literal text':
                    self._parse_list_of_literal_text(sample)
                elif marker_type == 'Numbers':
                    self._parse_numbers(sample)

                self._insert_repeat_info(sample)

            self._samples.parsed_samples.append(self._alternating_group)

    def _parse_basic_characters(self, sample):
        marker_info = sample['markerInfo']
        self._alternating_group.append(BasicCharactersInfo(marker_info))

    def _parse_literal_text(self, sample):
        marker_info = sample['markerInfo']

        extra_info = []
        if marker_info['caseInsensitive']:
            extra_info.append(LiteralTextTok.CASE_INSENSITIVE)
        else:
            extra_info.append(LiteralTextTok.CASE_SENSITIVE)
        
        if marker_info['matchAllExceptSpecified']:
            extra_info.append(LiteralTextTok.MATCH_ALL_EXCEPT_SPECIFIED)

        self._alternating_group.append(LiteralTextInfo(sample['markedStrings'], extra_info))

    def _parse_digits(self, sample):
        marker_info = sample['markerInfo']

        digits_info = DigitsInfo()
        for i in marker_info:
            if i != 'minus' and marker_info[i]:
                digits_info.digits.append(digit_to_enum[i])
            else:
                minus_info = marker_info['minus']

                digits_info.include_minus = minus_info['minus']
                digits_info.include_optional_minus = minus_info['optional']

        self._alternating_group.append(digits_info)

    def _parse_control_characters(self, sample):
        marker_info = sample['markerInfo']
        match_all_except_spec = marker_info['matchAllExceptSelectedOnes']

        wanted_control_chars = []
        for control_char in control_chars:
            if not match_all_except_spec and marker_info[control_char]:
                wanted_control_chars.append(control_char_to_token[control_char])
            elif match_all_except_spec and not marker_info[control_char]:
                wanted_control_chars.append(control_char_to_token[control_char])

        self._alternating_group.append(ControlCharactersInfo(wanted_control_chars))

    def _parse_unicode_characters(self, sample):
        marker_info = sample['markerInfo']
        match_all_except_spec = marker_info['matchAllExceptSelectedOnes']

        wanted_unicode_chars = []
        for unicode_char in unicode_chars:
            if not match_all_except_spec and marker_info[unicode_char]:
                wanted_unicode_chars.append(unicode_char_to_token[unicode_char])
            elif match_all_except_spec and not marker_info[unicode_char]:
                wanted_unicode_chars.append(unicode_char_to_token[unicode_char])

        unicode_info = UnicodeCharactersInfo(wanted_unicode_chars,
                                              marker_info['individualCharacters'].split())

        self._alternating_group.append(unicode_info)

    def _parse_match_anything(self, sample):
        marker_info = sample['markerInfo']
        match_anything_info = MatchAnythingInfo()

        match_anything_except = marker_info['matchAnythingExcept']
        if match_anything_except == 'Specific characters':
            match_anything_info.specific_characters = ''.join(set(marker_info['specificCharacters']))
        elif match_anything_except == 'Specific character':
            match_anything_info.specific_character = marker_info['specificCharacter'][0]
        elif match_anything_except == 'Nothing':
            match_anything_info.nothing = True
        elif match_anything_except == 'Basic characters':
            basic_chars = marker_info['basicCharacters']
            match_anything_info.basic_characters = [basic_char_to_tok[i] for i in basic_chars.keys() if basic_chars[i]]

        match_anything_info.can_span_across_lines = marker_info['canSpanAcrossLines']
        match_anything_info.case_insensitive = marker_info['caseInsensitive']

        self._alternating_group.append(match_anything_info)

    def _parse_list_of_literal_text(self, sample):
        marker_info = sample['markerInfo']
        self._alternating_group.append(ListOfLiteralTextInfo(marker_info['matchAnythingExceptSpecified'],
                                                                  marker_info['literalText'],
                                                                  marker_info['caseInsensitive']))

    def _parse_numbers(self, sample):
        marker_info = sample['markerInfo']
        self._alternating_group.append(NumbersInfo(marker_info))

    def _parse_general_regex_info(self, regex_info):
        gen_re_info = regex_info['generalRegexInfo']

        self._samples.target     = regex_info_to_tok[gen_re_info['regexTarget']]
        self._samples.start_info = regex_info_to_tok[gen_re_info['startRegexMatchAt']]
        self._samples.end_info   = regex_info_to_tok[gen_re_info['endRegexMatchAt']]

    def _insert_repeat_info(self, sample):
        repeat_info = sample['repeatInfo']['repeat']

        curr = self._alternating_group[-1].repetition_info

        if repeat_info == 'Custom range':
            curr.repeat_info = Repetition.CUSTOM_RANGE
            curr.repeat_start = int(sample['repeatInfo']['start'])
            curr.repeat_end = int(sample['repeatInfo']['end'])
        elif repeat_info == 'n or more times':
            curr.repeat_info = Repetition.N_OR_MORE_TIMES
            curr.repeat_start = int(sample['repeatInfo']['start'])
        else:
            curr.repeat_info = repetition_info_to_enum[repeat_info]
