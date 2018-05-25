from reggy.samples.parser.repetition_info import RepetitionInfo


class LiteralTextInfo:

    def __init__(self, literal_text: str, extra_info: list):
        self.literal_text = literal_text
        self.extra_info = extra_info
        self.repetition_info = RepetitionInfo()