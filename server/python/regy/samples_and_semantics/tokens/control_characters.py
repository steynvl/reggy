from enum import Enum

from regy.samples_and_semantics.tokens import TargetLanguage


class ControlCharacters(Enum):

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
    'nul'                       : ControlCharacters.NULL,
    'startOfHeading'            : ControlCharacters.START_OF_HEADING,
    'startOfText'               : ControlCharacters.START_OF_TEXT,
    'endOfText'                 : ControlCharacters.END_OF_TEXT,
    'endOfTransmission'         : ControlCharacters.END_OF_TRANSMISSION,
    'enquiry'                   : ControlCharacters.ENQUIRY,
    'acknowledge'               : ControlCharacters.ACKNOWLEDGE,
    'bell'                      : ControlCharacters.BELL,
    'backspace'                 : ControlCharacters.BACKSPACE,
    'horizontalTab'             : ControlCharacters.HORIZONTAL_TAB,
    'newLine'                   : ControlCharacters.NEW_LINE,
    'verticalTab'               : ControlCharacters.VERTICAL_TAB,
    'formFeed'                  : ControlCharacters.FORM_FEED,
    'carriageReturn'            : ControlCharacters.CARRIAGE_RETURN,
    'shiftOut'                  : ControlCharacters.SHIFT_OUT,
    'shiftIn'                   : ControlCharacters.SHIFT_IN,
    'dataLinkEscape'            : ControlCharacters.DATA_LINK_ESCAPE,
    'deviceControlOne'          : ControlCharacters.DEVICE_CONTROL_ONE,
    'deviceControlTwo'          : ControlCharacters.DEVICE_CONTROL_TWO,
    'deviceControlThree'        : ControlCharacters.DEVICE_CONTROL_THREE,
    'deviceControlFour'         : ControlCharacters.DEVICE_CONTROL_FOUR,
    'negativeAcknowledge'       : ControlCharacters.NEGATIVE_ACKNOWLEDGE,
    'synchronousIdle'           : ControlCharacters.SYNCHRONOUS_IDLE,
    'endOfTransBlock'           : ControlCharacters.END_OF_TRANSMISSION_BLOCK,
    'cancel'                    : ControlCharacters.CANCEL,
    'endOfMedium'               : ControlCharacters.END_OF_MEDIUM,
    'substitute'                : ControlCharacters.SUBSTITUTE,
    'escape'                    : ControlCharacters.ESCAPE,
    'fileSeparator'             : ControlCharacters.FILE_SEPARATOR,
    'groupSeparator'            : ControlCharacters.GROUP_SEPARATOR,
    'recordSeparator'           : ControlCharacters.RECORD_SEPARATOR,
    'unitSeparator'             : ControlCharacters.UNIT_SEPARATOR
}

control_char_to_re = {

    TargetLanguage.JAVA: {
        ControlCharacters.NULL                          : '\\\\x00',
        ControlCharacters.START_OF_HEADING              : '\\\\x01',
        ControlCharacters.START_OF_TEXT                 : '\\\\x02',
        ControlCharacters.END_OF_TEXT                   : '\\\\x03',
        ControlCharacters.END_OF_TRANSMISSION           : '\\\\x04',
        ControlCharacters.ENQUIRY                       : '\\\\x05',
        ControlCharacters.ACKNOWLEDGE                   : '\\\\x06',
        ControlCharacters.BELL                          : '\\\\x07',
        ControlCharacters.BACKSPACE                     : '\\\\x08',
        ControlCharacters.HORIZONTAL_TAB                : '\\\\x09',
        ControlCharacters.NEW_LINE                      : '\\\\x0A',
        ControlCharacters.VERTICAL_TAB                  : '\\\\x0B',
        ControlCharacters.FORM_FEED                     : '\\\\x0C',
        ControlCharacters.CARRIAGE_RETURN               : '\\\\x0D',
        ControlCharacters.SHIFT_OUT                     : '\\\\x0E',
        ControlCharacters.SHIFT_IN                      : '\\\\x0F',
        ControlCharacters.DATA_LINK_ESCAPE              : '\\\\x10',
        ControlCharacters.DEVICE_CONTROL_ONE            : '\\\\x11',
        ControlCharacters.DEVICE_CONTROL_TWO            : '\\\\x12',
        ControlCharacters.DEVICE_CONTROL_THREE          : '\\\\x13',
        ControlCharacters.DEVICE_CONTROL_FOUR           : '\\\\x14',
        ControlCharacters.NEGATIVE_ACKNOWLEDGE          : '\\\\x15',
        ControlCharacters.SYNCHRONOUS_IDLE              : '\\\\x16',
        ControlCharacters.END_OF_TRANSMISSION_BLOCK     : '\\\\x17',
        ControlCharacters.CANCEL                        : '\\\\x18',
        ControlCharacters.END_OF_MEDIUM                 : '\\\\x19',
        ControlCharacters.SUBSTITUTE                    : '\\\\x1A',
        ControlCharacters.ESCAPE                        : '\\\\x1B',
        ControlCharacters.FILE_SEPARATOR                : '\\\\x1C',
        ControlCharacters.GROUP_SEPARATOR               : '\\\\x1D',
        ControlCharacters.RECORD_SEPARATOR              : '\\\\x1E',
        ControlCharacters.UNIT_SEPARATOR                : '\\\\x1F'
    },

    TargetLanguage.PERL: {
        ControlCharacters.NULL                     : '\\x00',
        ControlCharacters.START_OF_HEADING         : '\\x01',
        ControlCharacters.START_OF_TEXT            : '\\x02',
        ControlCharacters.END_OF_TEXT              : '\\x03',
        ControlCharacters.END_OF_TRANSMISSION      : '\\x04',
        ControlCharacters.ENQUIRY                  : '\\x05',
        ControlCharacters.ACKNOWLEDGE              : '\\x06',
        ControlCharacters.BELL                     : '\\x07',
        ControlCharacters.BACKSPACE                : '\\x08',
        ControlCharacters.HORIZONTAL_TAB           : '\\x09',
        ControlCharacters.NEW_LINE                 : '\\x0A',
        ControlCharacters.VERTICAL_TAB             : '\\x0B',
        ControlCharacters.FORM_FEED                : '\\x0C',
        ControlCharacters.CARRIAGE_RETURN          : '\\x0D',
        ControlCharacters.SHIFT_OUT                : '\\x0E',
        ControlCharacters.SHIFT_IN                 : '\\x0F',
        ControlCharacters.DATA_LINK_ESCAPE         : '\\x10',
        ControlCharacters.DEVICE_CONTROL_ONE       : '\\x11',
        ControlCharacters.DEVICE_CONTROL_TWO       : '\\x12',
        ControlCharacters.DEVICE_CONTROL_THREE     : '\\x13',
        ControlCharacters.DEVICE_CONTROL_FOUR      : '\\x14',
        ControlCharacters.NEGATIVE_ACKNOWLEDGE     : '\\x15',
        ControlCharacters.SYNCHRONOUS_IDLE         : '\\x16',
        ControlCharacters.END_OF_TRANSMISSION_BLOCK: '\\x17',
        ControlCharacters.CANCEL                   : '\\x18',
        ControlCharacters.END_OF_MEDIUM            : '\\x19',
        ControlCharacters.SUBSTITUTE               : '\\x1A',
        ControlCharacters.ESCAPE                   : '\\x1B',
        ControlCharacters.FILE_SEPARATOR           : '\\x1C',
        ControlCharacters.GROUP_SEPARATOR          : '\\x1D',
        ControlCharacters.RECORD_SEPARATOR         : '\\x1E',
        ControlCharacters.UNIT_SEPARATOR           : '\\x1F'
    },

    TargetLanguage.POSIX: {

    }


}
