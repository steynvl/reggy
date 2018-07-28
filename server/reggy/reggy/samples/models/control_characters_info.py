from reggy.samples.parser.repetition_info import RepetitionInfo


class ControlCharactersInfo:

    def __init__(self, marker_id, wanted_control_chars: list):
        self.marker_id = marker_id
        self.wanted_control_chars = wanted_control_chars
        self.repetition_info = RepetitionInfo()
