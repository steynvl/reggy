from reggy.samples.parser.repetition_info import RepetitionInfo


class ListOfLiteralTextInfo:

    def __init__(self, marker_id, match_anything_except: bool, literal_text: list, case_insensitive: bool):
        self.marker_id = marker_id
        self.literal_text = literal_text
        self.match_anything_except_specified = match_anything_except
        self.case_insensitive = case_insensitive
        self.repetition_info = RepetitionInfo()
