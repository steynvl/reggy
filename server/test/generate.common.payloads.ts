export const creditCardNumbers = {
  'type': 'Credit card number',
  'information': {
    'visa': false,
    'dinersClub': false,
    'masterCard': false,
    'discover': false,
    'americanExpress': true,
    'jcb': false,
    'spacesAndDashes': 'No spaces or dashes'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const currencies = {
  'type': 'Currency',
  'information': {
    'currencies': [
      'Albanian lek',
      'United States dollar',
      'European euro',
      'Bhutanese ngultrum',
      'Cape Verdean escudo'
    ]
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const dateAndTime = {
  'type': 'Date and time',
  'information': {
    'dateSeparator': 'Forward slash',
    'timeSeparator': 'Colon',
    'amPmIndicator': 'AM',
    'leadingZeros': 'No leading zeros allowed',
    'dateFormats': 'y/m/d'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const emailAddresses = {
  'type': 'Email address',
  'information': {
    'username': 'Allow any user name',
    'domainName': 'Allow any domain name',
    'mailtoPrefix': 'No prefix',
    'specificUserNamesOnly': '',
    'domainOnSpecificTld': '',
    'anySubDomainOnSpecificDomain': '',
    'specificDomainsOnly': ''
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const GUID = {
  'type': 'GUID',
  'information': {
    'bracesAround': 'Required',
    'hyphensIn': 'Required',
    'guidCase': 'Case insensitive'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const ipv4 = {
  'type': 'IPv4 address',
  'information': {
    'dotted': true,
    'decimal': false,
    'hexadecimal1': false,
    'hexadecimal2': false,
    'hexadecimal3': false
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const nationalID = {
  'type': 'National ID',
  'information': {
    'kind': 'US social security number'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const password = {
  'type': 'Password',
  'information': {
    'shouldStartWith': 'Anything',
    'shouldContain': [
      'Digit',
      'Lowercase letter',
      'Uppercase letter'
    ],
    'minimumLength': '5',
    'maximumLength': 'No maximum length required'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of line',
    'endRegexMatchAt': 'End of line',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const URL = {
  'type': 'URL',
  'information': {
    'schemes': 'http',
    'portNumbers': 'No port number',
    'specOptionalPortNumbers': '',
    'specRequiredPortNumbers': '',
    'username': 'No user names',
    'specUserNames': '',
    'password': 'No password',
    'domainName': 'Allow any domain name',
    'specDomainNames': '',
    'specificTld': '',
    'subdomainOnSpecDomain': '',
    'folders': 'No folders',
    'minFolderDepth': '',
    'maxFolderDepth': '',
    'specFoldersOnly': '',
    'fileNames': 'No file names',
    'specExtensions': '',
    'specFileNames': '',
    'optionalFileNames': false,
    'parameters': 'No parameters',
    'specParameters': ''
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const username = {
  'type': 'Username',
  'information': {
    'shouldStartWith': 'Letter',
    'shouldContain': [],
    'minimumLength': '5',
    'maximumLength': '50'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of line',
    'endRegexMatchAt': 'End of line',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};

export const VAT = {
  'type': 'VAT number',
  'information': {
    'austria': true,
    'belgium': false,
    'bulgaria': false,
    'cyprus': false,
    'czechRepublic': false,
    'germany': false,
    'denmark': false,
    'slovakia': false,
    'estonia': false,
    'greece': false,
    'ireland': false,
    'poland': false,
    'spain': true,
    'italy': false,
    'portugal': false,
    'finland': true,
    'lithuania': false,
    'romania': false,
    'france': false,
    'luxembourg': false,
    'unitedKingdom': false,
    'latvia': false,
    'sweden': false,
    'croatia': false,
    'malta': false,
    'slovenia': false,
    'hungary': false,
    'netherlands': false,
    'countryCode': 'No country code',
    'groupingCharacters': 'None'
  },
  'generalRegexInfo': {
    'startRegexMatchAt': 'Start of word',
    'endRegexMatchAt': 'End of word',
    'regexTarget': 'Python'
  },
  'generateMethod': 'commonUseCases'
};
