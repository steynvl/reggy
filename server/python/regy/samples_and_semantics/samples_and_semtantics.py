from collections import deque
from regy.samples_and_semantics import mapper
from regy.samples_and_semantics.mapper.end_info_to_target import end_info_to_target
from regy.samples_and_semantics.mapper.start_info_to_target import start_info_to_target
from regy.samples_and_semantics.scanner.scanner import Scanner
from regy.samples_and_semantics.tokens import Token, MarkerType, Target
from regy.samples_and_semantics.tokens.case_state import CaseSensitive


class SamplesAndSemantics:

    def __init__(self, samples):
        self._samples = samples
        self._re = None
        self._calculate_regex()

    def get_re(self):
        return self._re

    def _calculate_regex(self):
        scanner = Scanner(self._samples)
        scanned_samples = scanner.get_scanned_samples()

        case_state = { 'case': CaseSensitive.ON, 'hasChanged': False, 'canUseCaseInsensitiveFlag': True }
        target_lang = scanned_samples[Token.GENERAL_REGEX_INFO][Token.TARGET]

        regex = deque()
        for scanned_sample in scanned_samples[Token.SAMPLE_STRINGS_INFO]:

            marker_type = scanned_sample[Token.MARKER_TYPE]
            if marker_type == MarkerType.LITERAL_TEXT:
                regex.extend(mapper.MapLiteralText(scanned_sample, target_lang, case_state).get_re())
            elif marker_type == MarkerType.DIGITS:
                regex.extend(mapper.MapDigits(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.BASIC_CHARACTERS:
                regex.extend(mapper.MapBasicCharacters(scanned_sample, target_lang, case_state).get_re())
            elif marker_type == MarkerType.CONTROL_CHARACTERS:
                regex.extend(mapper.MapControlCharacters(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.UNICODE_CHARACTERS:
                regex.extend(mapper.MapUnicodeCharacters(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.MATCH_ANYTHING:
                regex.extend(mapper.MapMatchAnything(scanned_sample, target_lang, case_state).get_re())
            elif marker_type == MarkerType.LIST_OF_LITERAL_TEXT:
                regex.extend(mapper.MapListOfLiteralText(scanned_sample, target_lang, case_state).get_re())

        self._add_general_info(scanned_samples, regex)

        regex = ''.join(regex).strip()
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
                compiled_re = '/{}/i'.format(compiled_re)
            else:
                compiled_re = '/{}/'.format(compiled_re)

        elif target == Target.POSIX:
            pass

        self._re['compiledRegex'] = compiled_re

    @staticmethod
    def _add_general_info(scanned_samples, regex):
        general_info = scanned_samples[Token.GENERAL_REGEX_INFO]
        target_lang = general_info[Token.TARGET]
        start_info = general_info[Token.REGEX_START_INFO]
        end_info = general_info[Token.REGEX_END_INFO]

        regex.appendleft(start_info_to_target[target_lang][start_info])
        regex.append(end_info_to_target[target_lang][end_info])

