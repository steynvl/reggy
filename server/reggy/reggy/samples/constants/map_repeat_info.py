from reggy.samples.tokens.repetition import Repetition

repeat_info_map = {
    Repetition.CUSTOM_RANGE   : '{{{},{}}}',
    Repetition.ZERO_OR_ONE    : '?',
    Repetition.ZERO_OR_MORE   : '*',
    Repetition.ONE_OR_MORE    : '+',
    Repetition.ONE            : '',
    Repetition.TWO            : '{2}',
    Repetition.THREE          : '{3}',
    Repetition.FOUR           : '{4}',
    Repetition.FIVE           : '{5}',
    Repetition.SIX            : '{6}',
    Repetition.SEVEN          : '{7}',
    Repetition.EIGHT          : '{8}',
    Repetition.NINE           : '{9}',
    Repetition.TEN            : '{10}',
    Repetition.N_OR_MORE_TIMES: '{{{},}}'
}
