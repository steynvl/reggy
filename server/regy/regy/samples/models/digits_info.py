from regy.samples.parser.repetition_info import RepetitionInfo


class DigitsInfo:

    def __init__(self):
        self.digits = []
        self.include_minus = False
        self.include_optional_minus = False
        self.repetition_info = RepetitionInfo()