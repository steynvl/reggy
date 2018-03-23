from enum import Enum

from regy.samples_and_semantics.tokens import TargetLanguage


class ControlCharactersInfo(Enum):

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


control_chars = [
    'nul', 'startOfHeading', 'startOfText',
    'endOfText', 'endOfTransmission', 'enquiry',
    'acknowledge', 'bell', 'backspace', 'horizontalTab',
    'newLine', 'verticalTab', 'formFeed',
    'carriageReturn', 'shiftOut', 'shiftIn', 'dataLinkEscape',
    'deviceControlOne', 'deviceControlTwo', 'deviceControlThree',
    'deviceControlFour', 'negativeAcknowledge', 'synchronousIdle',
    'endOfTransBlock', 'cancel', 'endOfMedium',
    'substitute', 'escape', 'fileSeparator',
    'groupSeparator', 'recordSeparator', 'unitSeparator'
]

control_char_to_token = {
    'nul'                       : ControlCharactersInfo.NULL,
    'startOfHeading'            : ControlCharactersInfo.START_OF_HEADING,
    'startOfText'               : ControlCharactersInfo.START_OF_TEXT,
    'endOfText'                 : ControlCharactersInfo.END_OF_TEXT,
    'endOfTransmission'         : ControlCharactersInfo.END_OF_TRANSMISSION,
    'enquiry'                   : ControlCharactersInfo.ENQUIRY,
    'acknowledge'               : ControlCharactersInfo.ACKNOWLEDGE,
    'bell'                      : ControlCharactersInfo.BELL,
    'backspace'                 : ControlCharactersInfo.BACKSPACE,
    'horizontalTab'             : ControlCharactersInfo.HORIZONTAL_TAB,
    'newLine'                   : ControlCharactersInfo.NEW_LINE,
    'verticalTab'               : ControlCharactersInfo.VERTICAL_TAB,
    'formFeed'                  : ControlCharactersInfo.FORM_FEED,
    'carriageReturn'            : ControlCharactersInfo.CARRIAGE_RETURN,
    'shiftOut'                  : ControlCharactersInfo.SHIFT_OUT,
    'shiftIn'                   : ControlCharactersInfo.SHIFT_IN,
    'dataLinkEscape'            : ControlCharactersInfo.DATA_LINK_ESCAPE,
    'deviceControlOne'          : ControlCharactersInfo.DEVICE_CONTROL_ONE,
    'deviceControlTwo'          : ControlCharactersInfo.DEVICE_CONTROL_TWO,
    'deviceControlThree'        : ControlCharactersInfo.DEVICE_CONTROL_THREE,
    'deviceControlFour'         : ControlCharactersInfo.DEVICE_CONTROL_FOUR,
    'negativeAcknowledge'       : ControlCharactersInfo.NEGATIVE_ACKNOWLEDGE,
    'synchronousIdle'           : ControlCharactersInfo.SYNCHRONOUS_IDLE,
    'endOfTransBlock'           : ControlCharactersInfo.END_OF_TRANSMISSION_BLOCK,
    'cancel'                    : ControlCharactersInfo.CANCEL,
    'endOfMedium'               : ControlCharactersInfo.END_OF_MEDIUM,
    'substitute'                : ControlCharactersInfo.SUBSTITUTE,
    'escape'                    : ControlCharactersInfo.ESCAPE,
    'fileSeparator'             : ControlCharactersInfo.FILE_SEPARATOR,
    'groupSeparator'            : ControlCharactersInfo.GROUP_SEPARATOR,
    'recordSeparator'           : ControlCharactersInfo.RECORD_SEPARATOR,
    'unitSeparator'             : ControlCharactersInfo.UNIT_SEPARATOR
}

control_char_to_re = {

    TargetLanguage.JAVA: {
        ControlCharactersInfo.NULL                          : '\\\\x00',
        ControlCharactersInfo.START_OF_HEADING              : '\\\\x01',
        ControlCharactersInfo.START_OF_TEXT                 : '\\\\x02',
        ControlCharactersInfo.END_OF_TEXT                   : '\\\\x03',
        ControlCharactersInfo.END_OF_TRANSMISSION           : '\\\\x04',
        ControlCharactersInfo.ENQUIRY                       : '\\\\x05',
        ControlCharactersInfo.ACKNOWLEDGE                   : '\\\\x06',
        ControlCharactersInfo.BELL                          : '\\\\x07',
        ControlCharactersInfo.BACKSPACE                     : '\\\\x08',
        ControlCharactersInfo.HORIZONTAL_TAB                : '\\\\x09',
        ControlCharactersInfo.NEW_LINE                      : '\\\\x0A',
        ControlCharactersInfo.VERTICAL_TAB                  : '\\\\x0B',
        ControlCharactersInfo.FORM_FEED                     : '\\\\x0C',
        ControlCharactersInfo.CARRIAGE_RETURN               : '\\\\x0D',
        ControlCharactersInfo.SHIFT_OUT                     : '\\\\x0E',
        ControlCharactersInfo.SHIFT_IN                      : '\\\\x0F',
        ControlCharactersInfo.DATA_LINK_ESCAPE              : '\\\\x10',
        ControlCharactersInfo.DEVICE_CONTROL_ONE            : '\\\\x11',
        ControlCharactersInfo.DEVICE_CONTROL_TWO            : '\\\\x12',
        ControlCharactersInfo.DEVICE_CONTROL_THREE          : '\\\\x13',
        ControlCharactersInfo.DEVICE_CONTROL_FOUR           : '\\\\x14',
        ControlCharactersInfo.NEGATIVE_ACKNOWLEDGE          : '\\\\x15',
        ControlCharactersInfo.SYNCHRONOUS_IDLE              : '\\\\x16',
        ControlCharactersInfo.END_OF_TRANSMISSION_BLOCK     : '\\\\x17',
        ControlCharactersInfo.CANCEL                        : '\\\\x18',
        ControlCharactersInfo.END_OF_MEDIUM                 : '\\\\x19',
        ControlCharactersInfo.SUBSTITUTE                    : '\\\\x1A',
        ControlCharactersInfo.ESCAPE                        : '\\\\x1B',
        ControlCharactersInfo.FILE_SEPARATOR                : '\\\\x1C',
        ControlCharactersInfo.GROUP_SEPARATOR               : '\\\\x1D',
        ControlCharactersInfo.RECORD_SEPARATOR              : '\\\\x1E',
        ControlCharactersInfo.UNIT_SEPARATOR                : '\\\\x1F'
    },

    TargetLanguage.PERL: {
        ControlCharactersInfo.NULL                     : '\\x00',
        ControlCharactersInfo.START_OF_HEADING         : '\\x01',
        ControlCharactersInfo.START_OF_TEXT            : '\\x02',
        ControlCharactersInfo.END_OF_TEXT              : '\\x03',
        ControlCharactersInfo.END_OF_TRANSMISSION      : '\\x04',
        ControlCharactersInfo.ENQUIRY                  : '\\x05',
        ControlCharactersInfo.ACKNOWLEDGE              : '\\x06',
        ControlCharactersInfo.BELL                     : '\\x07',
        ControlCharactersInfo.BACKSPACE                : '\\x08',
        ControlCharactersInfo.HORIZONTAL_TAB           : '\\x09',
        ControlCharactersInfo.NEW_LINE                 : '\\x0A',
        ControlCharactersInfo.VERTICAL_TAB             : '\\x0B',
        ControlCharactersInfo.FORM_FEED                : '\\x0C',
        ControlCharactersInfo.CARRIAGE_RETURN          : '\\x0D',
        ControlCharactersInfo.SHIFT_OUT                : '\\x0E',
        ControlCharactersInfo.SHIFT_IN                 : '\\x0F',
        ControlCharactersInfo.DATA_LINK_ESCAPE         : '\\x10',
        ControlCharactersInfo.DEVICE_CONTROL_ONE       : '\\x11',
        ControlCharactersInfo.DEVICE_CONTROL_TWO       : '\\x12',
        ControlCharactersInfo.DEVICE_CONTROL_THREE     : '\\x13',
        ControlCharactersInfo.DEVICE_CONTROL_FOUR      : '\\x14',
        ControlCharactersInfo.NEGATIVE_ACKNOWLEDGE     : '\\x15',
        ControlCharactersInfo.SYNCHRONOUS_IDLE         : '\\x16',
        ControlCharactersInfo.END_OF_TRANSMISSION_BLOCK: '\\x17',
        ControlCharactersInfo.CANCEL                   : '\\x18',
        ControlCharactersInfo.END_OF_MEDIUM            : '\\x19',
        ControlCharactersInfo.SUBSTITUTE               : '\\x1A',
        ControlCharactersInfo.ESCAPE                   : '\\x1B',
        ControlCharactersInfo.FILE_SEPARATOR           : '\\x1C',
        ControlCharactersInfo.GROUP_SEPARATOR          : '\\x1D',
        ControlCharactersInfo.RECORD_SEPARATOR         : '\\x1E',
        ControlCharactersInfo.UNIT_SEPARATOR           : '\\x1F'
    },

    TargetLanguage.POSIX: {

    }


}
