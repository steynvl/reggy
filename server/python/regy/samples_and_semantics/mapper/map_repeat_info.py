from regy.samples_and_semantics.tokens.repeat_info import RepeatInfo

repeat_info_map = {
    RepeatInfo.CUSTOM_RANGE   : '{{{},{}}}',
    RepeatInfo.ZERO_OR_ONE    : '?',
    RepeatInfo.ZERO_OR_MORE   : '*',
    RepeatInfo.ONE_OR_MORE    : '+',
    RepeatInfo.ONE            : '',
    RepeatInfo.TWO            : '{2}',
    RepeatInfo.THREE          : '{3}',
    RepeatInfo.FOUR           : '{4}',
    RepeatInfo.FIVE           : '{5}',
    RepeatInfo.SIX            : '{6}',
    RepeatInfo.SEVEN          : '{7}',
    RepeatInfo.EIGHT          : '{8}',
    RepeatInfo.NINE           : '{9}',
    RepeatInfo.TEN            : '{10}',
    RepeatInfo.N_OR_MORE_TIMES: '{{{},}}'
}
