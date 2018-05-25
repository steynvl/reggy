from reggy.samples.parser.repetition_info import RepetitionInfo


class ControlCharactersInfo:

    def __init__(self, wanted_control_chars: list):
        self.wanted_control_chars = wanted_control_chars
        self.repetition_info = RepetitionInfo()
