import re
from collections import OrderedDict
from regy.samples.parser.repetition_info import RepetitionInfo


class BasicCharactersInfo:

    def __init__(self, info):
        self.case_insensitive           = info['caseInsensitive']
        self.lower_case_letters         = info['lowerCaseLetters']
        self.upper_case_letters         = info['upperCaseLetters']
        self.digits                     = info['digits']
        self.punctuation_and_symbols    = info['punctuationAndSymbols']
        self.match_all_except_specified = info['matchAllExceptSpecified']
        self.white_space                = info['whiteSpace']
        self.line_breaks                = info['lineBreaks']

        self.individual_chars = ''.join(OrderedDict.fromkeys(re.sub(r'\s', '', info['individualCharacters'])))
        self.repetition_info = RepetitionInfo()
