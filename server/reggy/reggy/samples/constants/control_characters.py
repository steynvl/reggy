from reggy.samples.tokens import Target
from reggy.samples.tokens.control_characters_tok import ControlCharactersTok

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
    'nul'                : ControlCharactersTok.NULL,
    'startOfHeading'     : ControlCharactersTok.START_OF_HEADING,
    'startOfText'        : ControlCharactersTok.START_OF_TEXT,
    'endOfText'          : ControlCharactersTok.END_OF_TEXT,
    'endOfTransmission'  : ControlCharactersTok.END_OF_TRANSMISSION,
    'enquiry'            : ControlCharactersTok.ENQUIRY,
    'acknowledge'        : ControlCharactersTok.ACKNOWLEDGE,
    'bell'               : ControlCharactersTok.BELL,
    'backspace'          : ControlCharactersTok.BACKSPACE,
    'horizontalTab'      : ControlCharactersTok.HORIZONTAL_TAB,
    'newLine'            : ControlCharactersTok.NEW_LINE,
    'verticalTab'        : ControlCharactersTok.VERTICAL_TAB,
    'formFeed'           : ControlCharactersTok.FORM_FEED,
    'carriageReturn'     : ControlCharactersTok.CARRIAGE_RETURN,
    'shiftOut'           : ControlCharactersTok.SHIFT_OUT,
    'shiftIn'            : ControlCharactersTok.SHIFT_IN,
    'dataLinkEscape'     : ControlCharactersTok.DATA_LINK_ESCAPE,
    'deviceControlOne'   : ControlCharactersTok.DEVICE_CONTROL_ONE,
    'deviceControlTwo'   : ControlCharactersTok.DEVICE_CONTROL_TWO,
    'deviceControlThree' : ControlCharactersTok.DEVICE_CONTROL_THREE,
    'deviceControlFour'  : ControlCharactersTok.DEVICE_CONTROL_FOUR,
    'negativeAcknowledge': ControlCharactersTok.NEGATIVE_ACKNOWLEDGE,
    'synchronousIdle'    : ControlCharactersTok.SYNCHRONOUS_IDLE,
    'endOfTransBlock'    : ControlCharactersTok.END_OF_TRANSMISSION_BLOCK,
    'cancel'             : ControlCharactersTok.CANCEL,
    'endOfMedium'        : ControlCharactersTok.END_OF_MEDIUM,
    'substitute'         : ControlCharactersTok.SUBSTITUTE,
    'escape'             : ControlCharactersTok.ESCAPE,
    'fileSeparator'      : ControlCharactersTok.FILE_SEPARATOR,
    'groupSeparator'     : ControlCharactersTok.GROUP_SEPARATOR,
    'recordSeparator'    : ControlCharactersTok.RECORD_SEPARATOR,
    'unitSeparator'      : ControlCharactersTok.UNIT_SEPARATOR
}

control_char_to_re = {

    Target.JAVA: {
        ControlCharactersTok.NULL                     : '\\\\x00',
        ControlCharactersTok.START_OF_HEADING         : '\\\\x01',
        ControlCharactersTok.START_OF_TEXT            : '\\\\x02',
        ControlCharactersTok.END_OF_TEXT              : '\\\\x03',
        ControlCharactersTok.END_OF_TRANSMISSION      : '\\\\x04',
        ControlCharactersTok.ENQUIRY                  : '\\\\x05',
        ControlCharactersTok.ACKNOWLEDGE              : '\\\\x06',
        ControlCharactersTok.BELL                     : '\\\\x07',
        ControlCharactersTok.BACKSPACE                : '\\\\x08',
        ControlCharactersTok.HORIZONTAL_TAB           : '\\\\x09',
        ControlCharactersTok.NEW_LINE                 : '\\\\x0A',
        ControlCharactersTok.VERTICAL_TAB             : '\\\\x0B',
        ControlCharactersTok.FORM_FEED                : '\\\\x0C',
        ControlCharactersTok.CARRIAGE_RETURN          : '\\\\x0D',
        ControlCharactersTok.SHIFT_OUT                : '\\\\x0E',
        ControlCharactersTok.SHIFT_IN                 : '\\\\x0F',
        ControlCharactersTok.DATA_LINK_ESCAPE         : '\\\\x10',
        ControlCharactersTok.DEVICE_CONTROL_ONE       : '\\\\x11',
        ControlCharactersTok.DEVICE_CONTROL_TWO       : '\\\\x12',
        ControlCharactersTok.DEVICE_CONTROL_THREE     : '\\\\x13',
        ControlCharactersTok.DEVICE_CONTROL_FOUR      : '\\\\x14',
        ControlCharactersTok.NEGATIVE_ACKNOWLEDGE     : '\\\\x15',
        ControlCharactersTok.SYNCHRONOUS_IDLE         : '\\\\x16',
        ControlCharactersTok.END_OF_TRANSMISSION_BLOCK: '\\\\x17',
        ControlCharactersTok.CANCEL                   : '\\\\x18',
        ControlCharactersTok.END_OF_MEDIUM            : '\\\\x19',
        ControlCharactersTok.SUBSTITUTE               : '\\\\x1A',
        ControlCharactersTok.ESCAPE                   : '\\\\x1B',
        ControlCharactersTok.FILE_SEPARATOR           : '\\\\x1C',
        ControlCharactersTok.GROUP_SEPARATOR          : '\\\\x1D',
        ControlCharactersTok.RECORD_SEPARATOR         : '\\\\x1E',
        ControlCharactersTok.UNIT_SEPARATOR           : '\\\\x1F'
    },

    Target.PERL: {
        ControlCharactersTok.NULL                     : '\\x00',
        ControlCharactersTok.START_OF_HEADING         : '\\x01',
        ControlCharactersTok.START_OF_TEXT            : '\\x02',
        ControlCharactersTok.END_OF_TEXT              : '\\x03',
        ControlCharactersTok.END_OF_TRANSMISSION      : '\\x04',
        ControlCharactersTok.ENQUIRY                  : '\\x05',
        ControlCharactersTok.ACKNOWLEDGE              : '\\x06',
        ControlCharactersTok.BELL                     : '\\x07',
        ControlCharactersTok.BACKSPACE                : '\\x08',
        ControlCharactersTok.HORIZONTAL_TAB           : '\\x09',
        ControlCharactersTok.NEW_LINE                 : '\\x0A',
        ControlCharactersTok.VERTICAL_TAB             : '\\x0B',
        ControlCharactersTok.FORM_FEED                : '\\x0C',
        ControlCharactersTok.CARRIAGE_RETURN          : '\\x0D',
        ControlCharactersTok.SHIFT_OUT                : '\\x0E',
        ControlCharactersTok.SHIFT_IN                 : '\\x0F',
        ControlCharactersTok.DATA_LINK_ESCAPE         : '\\x10',
        ControlCharactersTok.DEVICE_CONTROL_ONE       : '\\x11',
        ControlCharactersTok.DEVICE_CONTROL_TWO       : '\\x12',
        ControlCharactersTok.DEVICE_CONTROL_THREE     : '\\x13',
        ControlCharactersTok.DEVICE_CONTROL_FOUR      : '\\x14',
        ControlCharactersTok.NEGATIVE_ACKNOWLEDGE     : '\\x15',
        ControlCharactersTok.SYNCHRONOUS_IDLE         : '\\x16',
        ControlCharactersTok.END_OF_TRANSMISSION_BLOCK: '\\x17',
        ControlCharactersTok.CANCEL                   : '\\x18',
        ControlCharactersTok.END_OF_MEDIUM            : '\\x19',
        ControlCharactersTok.SUBSTITUTE               : '\\x1A',
        ControlCharactersTok.ESCAPE                   : '\\x1B',
        ControlCharactersTok.FILE_SEPARATOR           : '\\x1C',
        ControlCharactersTok.GROUP_SEPARATOR          : '\\x1D',
        ControlCharactersTok.RECORD_SEPARATOR         : '\\x1E',
        ControlCharactersTok.UNIT_SEPARATOR           : '\\x1F'
    },

    Target.POSIX: {
        ControlCharactersTok.NULL                     : '\\x00',
        ControlCharactersTok.START_OF_HEADING         : '\\x01',
        ControlCharactersTok.START_OF_TEXT            : '\\x02',
        ControlCharactersTok.END_OF_TEXT              : '\\x03',
        ControlCharactersTok.END_OF_TRANSMISSION      : '\\x04',
        ControlCharactersTok.ENQUIRY                  : '\\x05',
        ControlCharactersTok.ACKNOWLEDGE              : '\\x06',
        ControlCharactersTok.BELL                     : '\\x07',
        ControlCharactersTok.BACKSPACE                : '\\x08',
        ControlCharactersTok.HORIZONTAL_TAB           : '\\x09',
        ControlCharactersTok.NEW_LINE                 : '\\x0A',
        ControlCharactersTok.VERTICAL_TAB             : '\\x0B',
        ControlCharactersTok.FORM_FEED                : '\\x0C',
        ControlCharactersTok.CARRIAGE_RETURN          : '\\x0D',
        ControlCharactersTok.SHIFT_OUT                : '\\x0E',
        ControlCharactersTok.SHIFT_IN                 : '\\x0F',
        ControlCharactersTok.DATA_LINK_ESCAPE         : '\\x10',
        ControlCharactersTok.DEVICE_CONTROL_ONE       : '\\x11',
        ControlCharactersTok.DEVICE_CONTROL_TWO       : '\\x12',
        ControlCharactersTok.DEVICE_CONTROL_THREE     : '\\x13',
        ControlCharactersTok.DEVICE_CONTROL_FOUR      : '\\x14',
        ControlCharactersTok.NEGATIVE_ACKNOWLEDGE     : '\\x15',
        ControlCharactersTok.SYNCHRONOUS_IDLE         : '\\x16',
        ControlCharactersTok.END_OF_TRANSMISSION_BLOCK: '\\x17',
        ControlCharactersTok.CANCEL                   : '\\x18',
        ControlCharactersTok.END_OF_MEDIUM            : '\\x19',
        ControlCharactersTok.SUBSTITUTE               : '\\x1A',
        ControlCharactersTok.ESCAPE                   : '\\x1B',
        ControlCharactersTok.FILE_SEPARATOR           : '\\x1C',
        ControlCharactersTok.GROUP_SEPARATOR          : '\\x1D',
        ControlCharactersTok.RECORD_SEPARATOR         : '\\x1E',
        ControlCharactersTok.UNIT_SEPARATOR           : '\\x1F'
    },

    Target.PYTHON: {
        ControlCharactersTok.NULL: '\\x00',
        ControlCharactersTok.START_OF_HEADING: '\\x01',
        ControlCharactersTok.START_OF_TEXT: '\\x02',
        ControlCharactersTok.END_OF_TEXT: '\\x03',
        ControlCharactersTok.END_OF_TRANSMISSION: '\\x04',
        ControlCharactersTok.ENQUIRY: '\\x05',
        ControlCharactersTok.ACKNOWLEDGE: '\\x06',
        ControlCharactersTok.BELL: '\\x07',
        ControlCharactersTok.BACKSPACE: '\\x08',
        ControlCharactersTok.HORIZONTAL_TAB: '\\x09',
        ControlCharactersTok.NEW_LINE: '\\x0A',
        ControlCharactersTok.VERTICAL_TAB: '\\x0B',
        ControlCharactersTok.FORM_FEED: '\\x0C',
        ControlCharactersTok.CARRIAGE_RETURN: '\\x0D',
        ControlCharactersTok.SHIFT_OUT: '\\x0E',
        ControlCharactersTok.SHIFT_IN: '\\x0F',
        ControlCharactersTok.DATA_LINK_ESCAPE: '\\x10',
        ControlCharactersTok.DEVICE_CONTROL_ONE: '\\x11',
        ControlCharactersTok.DEVICE_CONTROL_TWO: '\\x12',
        ControlCharactersTok.DEVICE_CONTROL_THREE: '\\x13',
        ControlCharactersTok.DEVICE_CONTROL_FOUR: '\\x14',
        ControlCharactersTok.NEGATIVE_ACKNOWLEDGE: '\\x15',
        ControlCharactersTok.SYNCHRONOUS_IDLE: '\\x16',
        ControlCharactersTok.END_OF_TRANSMISSION_BLOCK: '\\x17',
        ControlCharactersTok.CANCEL: '\\x18',
        ControlCharactersTok.END_OF_MEDIUM: '\\x19',
        ControlCharactersTok.SUBSTITUTE: '\\x1A',
        ControlCharactersTok.ESCAPE: '\\x1B',
        ControlCharactersTok.FILE_SEPARATOR: '\\x1C',
        ControlCharactersTok.GROUP_SEPARATOR: '\\x1D',
        ControlCharactersTok.RECORD_SEPARATOR: '\\x1E',
        ControlCharactersTok.UNIT_SEPARATOR: '\\x1F'
    }

}
