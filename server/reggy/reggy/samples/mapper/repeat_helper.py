from reggy.samples.tokens.repetition import Repetition
from reggy.samples.constants.map_repeat_info import repeat_info_map

def repeat_info_to_regex(info):
    repeat_info = info.repetition_info.repeat_info

    if repeat_info == Repetition.CUSTOM_RANGE:
        repeat_range = info.repetition_info
        s = repeat_range.repeat_start
        e = repeat_range.repeat_end
        return repeat_info_map[Repetition.CUSTOM_RANGE].format(s, e)
    elif repeat_info == Repetition.N_OR_MORE_TIMES:
        s = info.repetition_info.repeat_start
        return repeat_info_map[Repetition.N_OR_MORE_TIMES].format(s)
    else:
        return repeat_info_map[repeat_info]
