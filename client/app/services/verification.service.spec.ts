import { VerificationService } from './verification.service';
import { BasicCharacters } from '../models/samples/basic-characters';
import { ControlCharacters } from '../models/samples/control-characters';
import { Digits } from '../models/samples/digits';
import { ListOfLiteralText } from '../models/samples/list-of-literal-text';
import { MatchAnything } from '../models/samples/match-anything';
import { Numbers } from '../models/samples/numbers';
import { UnicodeCharacters } from '../models/samples/unicode-characters';
import { RepeatInfo } from '../models/samples/repeat-info';
import { MatchAnythingErr } from '../models/samples/match-anything-err';
import { NumbersErr } from '../models/samples/numbers-err';

describe('VerificationService', () => {
  let service: VerificationService;
  let basicCharacters: BasicCharacters;
  let controlCharacters: ControlCharacters;
  let digits: Digits;
  let listOfLiteralText: ListOfLiteralText;
  let matchAnything: MatchAnything;
  let numbers: Numbers;
  let unicodeCharacters: UnicodeCharacters;
  let repeatInfo: RepeatInfo;

  let err: MatchAnythingErr;
  let numbersErr: NumbersErr;

  beforeAll(() => { service = new VerificationService(); });

  it('Should be valid basic character info ', () => {
    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(true);

    basicCharacters.digits = false;
    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(true);

    basicCharacters.whiteSpace = false;
    basicCharacters.lowerCaseLetters = false;
    basicCharacters.punctuationAndSymbols = false;
    basicCharacters.lineBreaks = false;
    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(true);

    basicCharacters.upperCaseLetters = false;
    basicCharacters.individualCharacters = 'a';
    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(true);
  });

  it('Should be invalid basic character info ', () => {
    basicCharacters.digits = false;
    basicCharacters.whiteSpace = false;
    basicCharacters.lowerCaseLetters = false;
    basicCharacters.punctuationAndSymbols = false;
    basicCharacters.lineBreaks = false;
    basicCharacters.upperCaseLetters = false;
    basicCharacters.individualCharacters = '';

    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(false);

    basicCharacters.matchAllExceptSpecified = true;
    basicCharacters.caseInsensitive = true;
    expect(service.isValidBasicCharactersInfo(basicCharacters)).toBe(false);
  });

  it('Should be valid control character info ', () => {
    controlCharacters.matchAllExceptSelectedOnes = true;
    expect(service.isValidControlCharactersInfo(controlCharacters)).toBe(true);

    controlCharacters.matchAllExceptSelectedOnes = false;
    controlCharacters.nul = true;
    expect(service.isValidControlCharactersInfo(controlCharacters)).toBe(true);

    controlCharacters.backspace = true;
    expect(service.isValidControlCharactersInfo(controlCharacters)).toBe(true);
  });

  it('Should be invalid control character info ', () => {
    controlCharacters.nul = false;
    expect(service.isValidControlCharactersInfo(controlCharacters)).toBe(false);
  });

  it('Should be valid digits info ', () => {
    expect(service.isValidDigitsInfo(digits)).toBe(true);

    digits.zero = false;
    digits.one = false;
    digits.two = false;
    digits.three = false;
    digits.four = false;
    digits.five = false;
    digits.six = false;
    digits.seven = false;
    digits.eight = false;
    expect(service.isValidDigitsInfo(digits)).toBe(true);

    digits.nine = false;
    digits.one = true;
    expect(service.isValidDigitsInfo(digits)).toBe(true);
  });

  it('Should be invalid digits info ', () => {
    digits.zero = false;
    digits.one = false;
    digits.two = false;
    digits.three = false;
    digits.four = false;
    digits.five = false;
    digits.six = false;
    digits.seven = false;
    digits.eight = false;
    digits.nine = false;
    expect(service.isValidDigitsInfo(digits)).toBe(false);
  });

  it('Should be valid list of literal text info ', () => {
    listOfLiteralText.literalText.push('a');
    expect(service.isValidListOfLiteralTextInfo(listOfLiteralText)).toBe(true);
    listOfLiteralText.literalText.push('b');
    expect(service.isValidListOfLiteralTextInfo(listOfLiteralText)).toBe(true);
    listOfLiteralText.literalText.push('c');
    expect(service.isValidListOfLiteralTextInfo(listOfLiteralText)).toBe(true);
  });

  it('Should be invalid list of literal text info ', () => {
    listOfLiteralText.literalText = [];
    expect(service.isValidListOfLiteralTextInfo(listOfLiteralText)).toBe(false);
    listOfLiteralText.literalText.push('');
    expect(service.isValidListOfLiteralTextInfo(listOfLiteralText)).toBe(false);
  });

  it('Should be valid match anything info ', () => {
    matchAnything.matchAnythingExcept = 'Basic characters';
    matchAnything.basicCharacters.digits = true;
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(true);

    matchAnything.matchAnythingExcept = 'Specific characters';
    matchAnything.specificCharacters = 'a';
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(true);

    matchAnything.matchAnythingExcept = 'Specific character';
    matchAnything.specificCharacter = 'a';
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(true);
  });

  it('Should be invalid match anything info ', () => {
    matchAnything.matchAnythingExcept = 'Basic characters';
    matchAnything.basicCharacters.digits = false;
    matchAnything.basicCharacters.lowerCaseLetters = false;
    matchAnything.basicCharacters.upperCaseLetters = false;
    matchAnything.basicCharacters.punctuationAndSymbols = false;
    matchAnything.basicCharacters.whiteSpace = false;
    matchAnything.basicCharacters.lineBreaks = false;
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(false);

    matchAnything.matchAnythingExcept = 'Specific characters';
    matchAnything.specificCharacters = '';
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(false);

    matchAnything.matchAnythingExcept = 'Specific character';
    matchAnything.specificCharacter = '';
    expect(service.isValidMatchAnythingInfo(matchAnything, err)).toBe(false);
  });

  it('Should be valid numbers info ', () => {
    expect(service.isValidNumbersInfo(numbers, numbersErr)).toBe(true);
  });

  it('Should be invalid numbers info ', () => {
    numbers.minNrOfDecimals = 0;
    expect(service.isValidNumbersInfo(numbers, numbersErr)).toBe(false);
  });

  it('Should be valid unicode character info ', () => {
    unicodeCharacters.matchAllExceptSelectedOnes = true;
    expect(service.isValidUnicodeCharactersInfo(unicodeCharacters)).toBe(true);

    unicodeCharacters.matchAllExceptSelectedOnes = false;
    unicodeCharacters.lowercaseLetters = true;
    expect(service.isValidUnicodeCharactersInfo(unicodeCharacters)).toBe(true);

    unicodeCharacters.mathSymbols = true;
    expect(service.isValidUnicodeCharactersInfo(unicodeCharacters)).toBe(true);
  });

  it('Should be invalid unicode character info ', () => {
    unicodeCharacters.lowercaseLetters = false;
    unicodeCharacters.mathSymbols = false;
    expect(service.isValidUnicodeCharactersInfo(unicodeCharacters)).toBe(false);
  });

  /* set up mock objects */
  beforeEach(() => {
    basicCharacters = {
      caseInsensitive        : true,
      lowerCaseLetters       : true,
      upperCaseLetters       : true,
      digits                 : true,
      punctuationAndSymbols  : true,
      matchAllExceptSpecified: true,
      whiteSpace             : true,
      lineBreaks             : true,
      individualCharacters   : ''
    };

    controlCharacters = new ControlCharacters();

    digits = {
      zero: true,
      one: true,
      two: true,
      three: true,
      four: true,
      five: true,
      six: true,
      seven: true,
      eight: true,
      nine: true,
      minus: {
        minus: true,
        optional: true
      }
    };

    listOfLiteralText = {
      literalText: [],
      matchAnythingExceptSpecified: true,
      caseInsensitive: true
    };

    matchAnything = {
      matchAnythingExcept: '',
      specificCharacters : '',
      specificCharacter  : '',
      canSpanAcrossLines : true,
      caseInsensitive    : true,
      basicCharacters: {
        lowerCaseLetters       : true,
        upperCaseLetters       : true,
        digits                 : true,
        punctuationAndSymbols  : true,
        whiteSpace             : true,
        lineBreaks             : true
      }
    };

    numbers = {
      minValOfIntPart              : 0,
      maxValOfIntPart              : 100,
      decimalSeparator             : '',
      minNrOfDecimals              : 1,
      maxNrOfDecimals              : 3,
      thousandSeparator            : '',
      codePosition                 : '',
      currencySign                 : '',
      currencyCodes                : '',
      limitIntegerPart             : false,
      allowPlusSign                : false,
      allowMinusSign               : false,
      signIsRequired               : false,
      whitespaceAllowedAfterSign   : false,
      thousandSeparatorsAreRequired: false,
      allowLeadingZeros            : false,
      requireIntegerPart           : false,
      allowExponent                : false,
      currencySignOrCodeRequired   : false
    };

    unicodeCharacters = new UnicodeCharacters();

    repeatInfo = {
      repeat: '',
      start: 0,
      end: 1
    };

    err = {
      basicCharactersMsg: '',
      specCharacterMsg  : '',
      specCharactersMsg : ''
    };

    numbersErr = {
      currencyCodes: '',
      currencySignOrCode: '',
      decimalPart: '',
      integerPart: '',
      thousandSeparator: ''
    };

  });

});
