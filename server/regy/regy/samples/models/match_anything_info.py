from regy.samples.parser.repetition_info import RepetitionInfo


class MatchAnythingInfo:

    def __init__(self):
        self.specific_characters   = None
        self.specific_character    = None
        self.nothing               = None
        self.basic_characters      = None
        self.can_span_across_lines = None
        self.case_insensitive      = None

        self.repetition_info = RepetitionInfo()