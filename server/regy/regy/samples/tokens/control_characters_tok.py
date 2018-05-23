from enum import Enum


class ControlCharactersTok(Enum):
    NULL                           = 1
    START_OF_HEADING               = 2
    START_OF_TEXT                  = 3
    END_OF_TEXT                    = 4
    END_OF_TRANSMISSION            = 5
    ENQUIRY                        = 6
    ACKNOWLEDGE                    = 7
    BELL                           = 8
    BACKSPACE                      = 9
    HORIZONTAL_TAB                 = 10
    NEW_LINE                       = 11
    VERTICAL_TAB                   = 12
    FORM_FEED                      = 13
    CARRIAGE_RETURN                = 14
    SHIFT_OUT                      = 15
    SHIFT_IN                       = 16
    DATA_LINK_ESCAPE               = 17
    DEVICE_CONTROL_ONE             = 18
    DEVICE_CONTROL_TWO             = 19
    DEVICE_CONTROL_THREE           = 20
    DEVICE_CONTROL_FOUR            = 21
    NEGATIVE_ACKNOWLEDGE           = 22
    SYNCHRONOUS_IDLE               = 23
    END_OF_TRANSMISSION_BLOCK      = 24
    CANCEL                         = 25
    END_OF_MEDIUM                  = 26
    SUBSTITUTE                     = 27
    ESCAPE                         = 28
    FILE_SEPARATOR                 = 29
    GROUP_SEPARATOR                = 30
    RECORD_SEPARATOR               = 31
    UNIT_SEPARATOR                 = 32
    MATCH_ALL_EXCEPT_SELECTED_ONES = 33
