from reggy.samples.parser.repetition_info import RepetitionInfo


class BackReferenceInfo:

    def __init__(self, marker_id, info):
        self.marker_id = marker_id
        self.marker = info['marker']
        self.repetition_info = RepetitionInfo()
