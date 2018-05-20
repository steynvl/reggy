from collections import deque
from regy.samples import mapper
from regy.samples.mapper.end_info_to_target import end_info_to_target
from regy.samples.mapper.start_info_to_target import start_info_to_target
from regy.samples.models.basic_characters_info import BasicCharactersInfo
from regy.samples.models.control_characters_info import ControlCharactersInfo
from regy.samples.models.digits_info import DigitsInfo
from regy.samples.models.list_of_literal_text_info import ListOfLiteralTextInfo
from regy.samples.models.literal_text_info import LiteralTextInfo
from regy.samples.models.match_anything_info import MatchAnythingInfo
from regy.samples.models.numbers_info import NumbersInfo
from regy.samples.models.unicode_characters_info import UnicodeCharactersInfo
from regy.samples.parser.parser import Parser
from regy.samples.tokens import Target
from regy.samples.tokens.case_state import CaseSensitive


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

        case_state = { 'case': CaseSensitive.ON, 'hasChanged': False, 'canUseCaseInsensitiveFlag': True }
        target_lang = parsed_samples.target

        regex = deque()
        for parsed_sample in parsed_samples.parsed_samples:
            if isinstance(parsed_sample, LiteralTextInfo):
                regex.extend(mapper.MapLiteralText(parsed_sample, target_lang, case_state).get_re())
            elif isinstance(parsed_sample, DigitsInfo):
                regex.extend(mapper.MapDigits(parsed_sample, target_lang).get_re())
            elif isinstance(parsed_sample, BasicCharactersInfo):
                regex.extend(mapper.MapBasicCharacters(parsed_sample, target_lang, case_state).get_re())
            elif isinstance(parsed_sample, ControlCharactersInfo):
                regex.extend(mapper.MapControlCharacters(parsed_sample, target_lang).get_re())
            elif isinstance(parsed_sample, UnicodeCharactersInfo):
                regex.extend(mapper.MapUnicodeCharacters(parsed_sample, target_lang).get_re())
            elif isinstance(parsed_sample, MatchAnythingInfo):
                regex.extend(mapper.MapMatchAnything(parsed_sample, target_lang, case_state).get_re())
            elif isinstance(parsed_sample, ListOfLiteralTextInfo):
                regex.extend(mapper.MapListOfLiteralText(parsed_sample, target_lang, case_state).get_re())
            elif isinstance(parsed_sample, NumbersInfo):
                regex.extend(mapper.MapNumbers(parsed_sample, target_lang).get_re())

        self._add_general_info(parsed_samples, regex)

        regex = ''.join(regex)
        self._map_re_to_target(regex, target_lang, case_state)

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

        elif target == Target.POSIX:
            pass

        self._re['compiledRegex'] = compiled_re

    @staticmethod
    def _add_general_info(parsed_samples, regex):
        regex.appendleft(start_info_to_target[parsed_samples.target][parsed_samples.start_info])
        regex.append(end_info_to_target[parsed_samples.target][parsed_samples.end_info])
