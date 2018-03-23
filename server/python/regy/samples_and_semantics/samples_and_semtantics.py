from collections import deque
from regy.samples_and_semantics import mapper
from regy.samples_and_semantics.mapper.end_info_to_lang import end_info_to_lang
from regy.samples_and_semantics.mapper.start_info_to_lang import start_info_to_lang
from regy.samples_and_semantics.scanner.scanner import Scanner
from regy.samples_and_semantics.tokens import Token, MarkerType

class SamplesAndSemantics:

    def __init__(self, samples):
        self._samples = samples
        self._re = deque()
        self._calculate_regex()

    def get_re(self):
        return ''.join(self._re)

    def _calculate_regex(self):
        scanner = Scanner(self._samples)
        scanned_samples = scanner.get_scanned_samples()

        target_lang = scanned_samples[Token.GENERAL_REGEX_INFO][Token.TARGET_LANGUAGE]
        for scanned_sample in scanned_samples[Token.SAMPLE_STRINGS_INFO]:

            marker_type = scanned_sample[Token.MARKER_TYPE]
            if marker_type == MarkerType.MARKED_TEXT:
                self._re.extend(mapper.MapMarkedText(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.NUMBERS:
                self._re.extend(mapper.MapNumbers(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.BASIC_CHARACTERS:
                self._re.extend(mapper.MapBasicCharacters(scanned_sample, target_lang).get_re())
            elif marker_type == MarkerType.CONTROL_CHARACTERS:
                self._re.extend(mapper.MapControlCharacters(scanned_sample, target_lang).get_re())

        self._add_general_info(scanned_samples)

    def _add_general_info(self, scanned_samples):
        general_info = scanned_samples[Token.GENERAL_REGEX_INFO]
        target_lang = general_info[Token.TARGET_LANGUAGE]
        start_info = general_info[Token.REGEX_START_INFO]
        end_info = general_info[Token.REGEX_END_INFO]

        self._re.appendleft(start_info_to_lang[target_lang][start_info])
        self._re.append(end_info_to_lang[target_lang][end_info])
