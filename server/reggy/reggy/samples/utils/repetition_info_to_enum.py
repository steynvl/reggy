from reggy.samples.tokens.repetition import Repetition

repetition_info_to_enum = {
    '0 or 1'   : Repetition.ZERO_OR_ONE,
    '0 or more': Repetition.ZERO_OR_MORE,
    '1 or more': Repetition.ONE_OR_MORE,
    '1'        : Repetition.ONE,
    '2'        : Repetition.TWO,
    '3'        : Repetition.THREE,
    '4'        : Repetition.FOUR,
    '5'        : Repetition.FIVE,
    '6'        : Repetition.SIX,
    '7'        : Repetition.SEVEN,
    '8'        : Repetition.EIGHT,
    '9'        : Repetition.NINE,
    '10'       : Repetition.TEN
}
