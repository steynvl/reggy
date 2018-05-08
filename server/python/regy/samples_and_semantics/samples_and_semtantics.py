from collections import deque
from regy.samples_and_semantics import mapper
from regy.samples_and_semantics.mapper.end_info_to_target import end_info_to_target
from regy.samples_and_semantics.mapper.start_info_to_target import start_info_to_target
from regy.samples_and_semantics.scanner.scanner import Scanner
from regy.samples_and_semantics.tokens import Token, MarkerType
from regy.samples_and_semantics.tokens.case_state import CaseSensitive


class SamplesAndSemantics:

    def __init__(self, samples):
        self._samples = samples
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re).strip()

    def _calculate_regex(self):
        scanner = Scanner(self._samples)
        scanned_samples = scanner.get_scanned_samples()

        case_state = {
            'case'      : CaseSensitive.ON,
            'hasChanged': False
        }
        target_lang = scanned_samples[Token.GENERAL_REGEX_INFO][Token.TARGET]

        for scanned_sample in scanned_samples[Token.SAMPLE_STRINGS_INFO]:

            marker_type = scanned_sample[Token.MARKER_TYPE]
            if marker_type == MarkerType.LITERAL_TEXT:
                self._re.extend(mapper.MapLiteralText(scanned_sample, target_lang, case_state).get_re())
            elif marker_type == MarkerType.DIGITS:
                self._re.extend(mapper.MapDigits(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.BASIC_CHARACTERS:
                self._re.extend(mapper.MapBasicCharacters(scanned_sample, target_lang, case_state).get_re())
            elif marker_type == MarkerType.CONTROL_CHARACTERS:
                self._re.extend(mapper.MapControlCharacters(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.UNICODE_CHARACTERS:
                self._re.extend(mapper.MapUnicodeCharacters(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.MATCH_ANYTHING:
                self._re.extend(mapper.MapMatchAnything(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.LIST_OF_LITERAL_TEXT:
                self._re.extend(mapper.MapListOfLiteralText(scanned_sample, target_lang, case_state).get_re())

        self._add_general_info(scanned_samples)

    def _add_general_info(self, scanned_samples):
        general_info = scanned_samples[Token.GENERAL_REGEX_INFO]
        target_lang = general_info[Token.TARGET]
        start_info = general_info[Token.REGEX_START_INFO]
        end_info = general_info[Token.REGEX_END_INFO]

        self._re.appendleft(start_info_to_target[target_lang][start_info])
        self._re.append(end_info_to_target[target_lang][end_info])
