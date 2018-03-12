from regy.tokens import RepeatInfo

repeat_info_to_enum = {
    '0 or 1'   : RepeatInfo.ZERO_OR_ONE,
    '0 or more': RepeatInfo.ZERO_OR_MORE,
    '1 or more': RepeatInfo.ONE_OR_MORE,
    '1'        : RepeatInfo.ONE,
    '2'        : RepeatInfo.TWO,
    '3'        : RepeatInfo.THREE,
    '4'        : RepeatInfo.FOUR,
    '5'        : RepeatInfo.FIVE,
    '6'        : RepeatInfo.SIX,
    '7'        : RepeatInfo.SEVEN,
    '8'        : RepeatInfo.EIGHT,
    '9'        : RepeatInfo.NINE,
    '10'       : RepeatInfo.TEN
}
