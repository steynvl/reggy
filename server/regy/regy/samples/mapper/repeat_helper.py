from regy.samples.tokens import Token
from regy.samples.tokens.repeat_info import RepeatInfo
from regy.samples.mapper.map_repeat_info import repeat_info_map

def repeat_info_to_regex(info):
    repeat_info = info[Token.REPEAT_INFO]

    if repeat_info == RepeatInfo.CUSTOM_RANGE:
        repeat_range = info[Token.REPEAT_RANGE]
        s = repeat_range[Token.REPEAT_START]
        e = repeat_range[Token.REPEAT_END]
        return repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
    elif repeat_info == RepeatInfo.N_OR_MORE_TIMES:
        s = info[Token.REPEAT_RANGE][Token.REPEAT_START]
        return repeat_info_map[RepeatInfo.N_OR_MORE_TIMES].format(s)
    else:
        return repeat_info_map[repeat_info]
