from collections import deque
from reggy.samples import mapper
from reggy.samples.constants.end_info_to_target import end_info_to_target
from reggy.samples.constants.start_info_to_target import start_info_to_target
from reggy.samples.models.basic_characters_info import BasicCharactersInfo
from reggy.samples.models.control_characters_info import ControlCharactersInfo
from reggy.samples.models.digits_info import DigitsInfo
from reggy.samples.models.list_of_literal_text_info import ListOfLiteralTextInfo
from reggy.samples.models.literal_text_info import LiteralTextInfo
from reggy.samples.models.match_anything_info import MatchAnythingInfo
from reggy.samples.models.numbers_info import NumbersInfo
from reggy.samples.models.unicode_characters_info import UnicodeCharactersInfo
from reggy.samples.models.back_reference_info import BackReferenceInfo
from reggy.samples.parser.parser import Parser
from reggy.samples.tokens import Target
from reggy.samples.tokens.case_state import CaseSensitive


class SamplesAndSemantics:

    def __init__(self, samples):
        self._samples = samples
        self._re = None
        self._calculate_regex()

    def get_re(self):
        return self._re

    def _calculate_regex(self):
        parser = Parser(self._samples)
        parsed_samples = parser.get_parsed_samples()

        flat_samples = [item for sublist in parsed_samples.parsed_samples for item in sublist]

        state_info = {
            'case': CaseSensitive.ON,
            'hasChanged': False,
            'canUseCaseInsensitiveFlag': True,
            'currBackReferenceNum': 0,
            'markerToReference': {
                i: None for i in range(1, parser.nr_of_markers + 1)
            }
        }
        target_lang = parsed_samples.target
        curr_marker_id = 0

        regex = deque()
        for group in parsed_samples.parsed_samples:
            alternating_group = []

            for sample in group:
                curr_marker_id += 1
                state_info['isBackReferenced'] = self._is_back_referenced(curr_marker_id, flat_samples)

                if isinstance(sample, LiteralTextInfo):
                    alternating_group.append(mapper.MapLiteralText(sample, target_lang, state_info).get_re())
                elif isinstance(sample, DigitsInfo):
                    alternating_group.append(mapper.MapDigits(sample, target_lang, state_info).get_re())
                elif isinstance(sample, BasicCharactersInfo):
                    alternating_group.append(mapper.MapBasicCharacters(sample, target_lang, state_info).get_re())
                elif isinstance(sample, ControlCharactersInfo):
                    alternating_group.append(mapper.MapControlCharacters(sample, target_lang, state_info).get_re())
                elif isinstance(sample, UnicodeCharactersInfo):
                    alternating_group.append(mapper.MapUnicodeCharacters(sample, target_lang, state_info).get_re())
                elif isinstance(sample, MatchAnythingInfo):
                    alternating_group.append(mapper.MapMatchAnything(sample, target_lang, state_info).get_re())
                elif isinstance(sample, ListOfLiteralTextInfo):
                    alternating_group.append(mapper.MapListOfLiteralText(sample, target_lang, state_info).get_re())
                elif isinstance(sample, NumbersInfo):
                    alternating_group.append(mapper.MapNumbers(sample, target_lang).get_re())
                elif isinstance(sample, BackReferenceInfo):
                    alternating_group.append(mapper.MapBackReference(sample, target_lang, state_info).get_re())

            if len(alternating_group) <= 1:
                regex.append(''.join(alternating_group))
            else:
                regex.append('(?:{})'.format('|'.join(alternating_group)))

        self._add_general_info(parsed_samples, regex)

        regex = ''.join(regex)
        self._map_re_to_target(regex, target_lang, state_info)

    def _map_re_to_target(self, regex, target, case_state):
        self._re = { 'regex': regex }

        compiled_re = regex[:]
        if target == Target.JAVA:
            if case_state['canUseCaseInsensitiveFlag'] and case_state['hasChanged']:
                compiled_re = compiled_re.replace('(?i)', '').replace('(?-i)', '')
                compiled_re = 'Pattern regex = Pattern.compile("{}", Pattern.CASE_INSENSITIVE);'.format(compiled_re)
            else:
                compiled_re = 'Pattern regex = Pattern.compile("{}");'.format(compiled_re)

        elif target == Target.PERL:
            if case_state['canUseCaseInsensitiveFlag'] and case_state['hasChanged']:
                compiled_re = compiled_re.replace('(?i)', '').replace('(?-i)', '')
                compiled_re = 'my $regex = /{}/i;'.format(compiled_re)
            else:
                compiled_re = 'my $regex = /{}/;'.format(compiled_re)

        elif target == Target.PYTHON:
            if case_state['canUseCaseInsensitiveFlag'] and case_state['hasChanged']:
                compiled_re = compiled_re.replace('(?i)', '').replace('(?-i)', '')
                compiled_re = 'regex = re.compile(r\'{}\', re.IGNORECASE)'.format(compiled_re)
            else:
                compiled_re = 'regex = re.compile(r\'{}\')'.format(compiled_re)

        elif target == Target.JAVASCRIPT:
            if case_state['canUseCaseInsensitiveFlag'] and case_state['hasChanged']:
                compiled_re = compiled_re.replace('(?i)', '').replace('(?-i)', '')
                compiled_re = 'const regex = /{}/i;'.format(compiled_re)
            else:
                compiled_re = 'const regex = /{}/;'.format(compiled_re)

        elif target == Target.PHP:
            if case_state['canUseCaseInsensitiveFlag'] and case_state['hasChanged']:
                compiled_re = compiled_re.replace('(?i)', '').replace('(?-i)', '')
                compiled_re = '$regex = \'/{}/i\';'.format(compiled_re)
            else:
                compiled_re = '$regex = \'/{}/\';'.format(compiled_re)

        elif target == Target.GOLANG:
            compiled_re = 'regex, _ := regexp.Compile("{}")'.format(compiled_re)

        self._re['compiledRegex'] = compiled_re

    @staticmethod
    def _add_general_info(parsed_samples, regex):
        regex.appendleft(start_info_to_target[parsed_samples.target][parsed_samples.start_info])
        regex.append(end_info_to_target[parsed_samples.target][parsed_samples.end_info])

    @staticmethod
    def _is_back_referenced(curr_marker_id, samples):
        return any(isinstance(i, BackReferenceInfo) and i.marker['id'] == curr_marker_id for i in samples)
