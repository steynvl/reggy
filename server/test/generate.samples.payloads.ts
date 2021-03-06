export const basicCharacters = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Basic characters',
        'markedStrings': [
          'dasdas'
        ],
        'markerInfo': {
          'caseInsensitive': false,
          'lowerCaseLetters': true,
          'upperCaseLetters': true,
          'digits': false,
          'punctuationAndSymbols': false,
          'matchAllExceptSpecified': false,
          'whiteSpace': false,
          'lineBreaks': false,
          'individualCharacters': ''
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Java'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const controlCharacters = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Control characters',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'nul': false,
          'startOfHeading': false,
          'startOfText': false,
          'endOfText': false,
          'endOfTransmission': false,
          'enquiry': false,
          'acknowledge': false,
          'bell': false,
          'backspace': false,
          'horizontalTab': true,
          'newLine': true,
          'verticalTab': false,
          'formFeed': false,
          'carriageReturn': false,
          'shiftOut': false,
          'shiftIn': false,
          'dataLinkEscape': false,
          'deviceControlOne': false,
          'deviceControlTwo': false,
          'deviceControlThree': false,
          'deviceControlFour': false,
          'negativeAcknowledge': false,
          'synchronousIdle': false,
          'endOfTransBlock': false,
          'cancel': false,
          'endOfMedium': false,
          'substitute': false,
          'escape': false,
          'fileSeparator': false,
          'groupSeparator': false,
          'recordSeparator': false,
          'unitSeparator': false,
          'matchAllExceptSelectedOnes': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const digits = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Digits',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'zero': true,
          'one': true,
          'two': true,
          'three': true,
          'four': true,
          'five': false,
          'six': true,
          'seven': true,
          'eight': true,
          'nine': true,
          'minus': {
            'minus': false,
            'optional': false
          }
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const listOfLiteralText = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'List of literal text',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'literalText': [
            'a',
            'b'
          ],
          'matchAnythingExceptSpecified': false,
          'caseInsensitive': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const literalText = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Literal text',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'caseInsensitive': true,
          'matchAllExceptSpecified': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const matchAnything = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Match anything',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'matchAnythingExcept': 'Basic characters',
          'specificCharacters': '',
          'specificCharacter': '',
          'canSpanAcrossLines': false,
          'caseInsensitive': false,
          'basicCharacters': {
            'lowerCaseLetters': true,
            'upperCaseLetters': true,
            'digits': false,
            'punctuationAndSymbols': false,
            'whiteSpace': false,
            'lineBreaks': false
          }
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const numbers = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Numbers',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'minValOfIntPart': 0,
          'maxValOfIntPart': 100,
          'decimalSeparator': 'Any',
          'minNrOfDecimals': 0,
          'maxNrOfDecimals': 0,
          'thousandSeparator': 'None',
          'codePosition': 'Before only',
          'currencySign': 'None',
          'currencyCodes': '',
          'limitIntegerPart': true,
          'allowPlusSign': false,
          'allowMinusSign': false,
          'signIsRequired': false,
          'whitespaceAllowedAfterSign': false,
          'thousandSeparatorsAreRequired': false,
          'allowLeadingZeros': false,
          'requireIntegerPart': false,
          'allowExponent': false,
          'currencySignOrCodeRequired': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const unicodeCharacters = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Unicode characters',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'lowercaseLetters': false,
          'uppercaseLetters': false,
          'titleCaseLetters': false,
          'casedLetters': true,
          'modifierLetters': false,
          'otherLetters': false,
          'nonSpacingMarks': false,
          'spacingCombiningMarks': false,
          'enclosingMarks': false,
          'spaceSeparators': false,
          'lineSeparators': false,
          'paragraphSeparators': false,
          'mathSymbols': true,
          'currencySymbols': false,
          'modifierSymbols': false,
          'otherSymbols': false,
          'decimalDigitNumbers': false,
          'letterNumbers': false,
          'otherNumbers': false,
          'dashPunctuation': false,
          'openPunctuation': false,
          'closePunctuation': false,
          'initialPunctuation': false,
          'finalPunctuation': false,
          'connectorPunctuation': false,
          'otherPunctuation': false,
          'controlCharacters': false,
          'formatCharacters': false,
          'privateUseCharacters': false,
          'surrogateCharacters': false,
          'unassignedCharacters': false,
          'matchAllExceptSelectedOnes': false,
          'individualCharacters': ''
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const literalTextFactorise = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Literal text',
        'markedStrings': [
          'abcqqqklm',
          'abcrrrklm'
        ],
        'markerInfo': {
          'caseInsensitive': false,
          'matchAllExceptSpecified': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const repetition = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Digits',
        'markedStrings': [
          'asdsa'
        ],
        'markerInfo': {
          'zero': true,
          'one': true,
          'two': true,
          'three': true,
          'four': true,
          'five': false,
          'six': true,
          'seven': true,
          'eight': true,
          'nine': true,
          'minus': {
            'minus': false,
            'optional': false
          }
        },
        'repeatInfo': {
          'repeat': 'Custom range',
          'start': 1,
          'end': 3
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const alternation = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Literal text',
        'markedStrings': [
          'dsa'
        ],
        'markerInfo': {
          'caseInsensitive': false,
          'matchAllExceptSpecified': false
        },
        'repeatInfo': {
          'repeat': '1'
        }
      },
      {
        'markerType': 'Digits',
        'markedStrings': [
          'adas'
        ],
        'markerInfo': {
          'zero': true,
          'one': true,
          'two': true,
          'three': true,
          'four': true,
          'five': false,
          'six': true,
          'seven': true,
          'eight': true,
          'nine': true,
          'minus': {
            'minus': false,
            'optional': false
          }
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};

export const backReference = {
  'sampleStringsInfo': [
    [
      {
        'markerType': 'Digits',
        'markedStrings': [
          'asa'
        ],
        'markerInfo': {
          'zero': true,
          'one': true,
          'two': true,
          'three': false,
          'four': true,
          'five': true,
          'six': true,
          'seven': true,
          'eight': true,
          'nine': true,
          'minus': {
            'minus': false,
            'optional': false
          }
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ],
    [
      {
        'markerType': 'Backreference match of preceding marker',
        'markedStrings': [
          'asa'
        ],
        'markerInfo': {
          'marker': {
            'id': 1,
            'colour': '#FFAEB9',
            'fieldType': 'Digits',
            'markerInfo': {
              'zero': true,
              'one': true,
              'two': true,
              'three': false,
              'four': true,
              'five': true,
              'six': true,
              'seven': true,
              'eight': true,
              'nine': true,
              'minus': {
                'minus': false,
                'optional': false
              }
            },
            'markedTextInfo': [
              {
                'start': 0,
                'end': 3,
                'text': 'asa'
              }
            ],
            'repeatInfo': {
              'repeat': '1'
            },
            'error': {},
            'repeatInfoView': [
              'Custom range',
              'n or more times',
              '0 or 1',
              '0 or more',
              '1 or more',
              '1',
              '2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              '10'
            ]
          }
        },
        'repeatInfo': {
          'repeat': '1'
        }
      }
    ]
  ],
  'generalRegexInfo': {
    'startRegexMatchAt': 'Anywhere',
    'endRegexMatchAt': 'Anywhere',
    'regexTarget': 'Python'
  },
  'generateMethod': 'samplesAndSemantics'
};
