from reggy.samples.parser.repetition_info import RepetitionInfo


class UnicodeCharactersInfo:

    def __init__(self, marker_id, unicode_chars, individual_chars):
        self.marker_id = marker_id
        self.unicode_characters       = unicode_chars
        self.individual_unicode_chars = individual_chars
        self.repetition_info = RepetitionInfo()
