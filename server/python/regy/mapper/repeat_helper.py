from regy.tokens.repeat_info import RepeatInfo
from regy.mapper.map_repeat_info import repeat_info_map

def repeat_info_to_regex(info):
    repeat_info = info['repeatInfo']

    if repeat_info == RepeatInfo.CUSTOM_RANGE:
        repeat_range = info['repeatRange']
        s = repeat_range['start']
        e = repeat_range['end']
        return repeat_info_map[RepeatInfo.CUSTOM_RANGE].format(s, e)
    elif repeat_info == RepeatInfo.MIN_TO_INF:
        s = info['repeatRange']['start']
        return repeat_info_map[RepeatInfo.MIN_TO_INF].format(s)
    else:
        return repeat_info_map[repeat_info]
