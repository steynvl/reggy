import { Injectable } from '@angular/core';
import { MatchAnything } from '../models/samples/match-anything';
import { ControlCharacters } from '../models/samples/control-characters';
import { RepeatInfo } from '../models/samples/repeat-info';
import { UnicodeCharacters } from '../models/samples/unicode-characters';
import { BasicCharacters } from '../models/samples/basic-characters';
import { ListOfLiteralText } from '../models/samples/list-of-literal-text';
import { Numbers } from '../models/samples/numbers';
import { Digits } from '../models/samples/digits';
import { MatchAnythingErr } from '../models/samples/match-anything-err';
import { NumbersErr } from '../models/samples/numbers-err';


@Injectable()
export class VerificationService {

  isValidBasicCharactersInfo(info: BasicCharacters): boolean {
    if (info.individualCharacters !== undefined && info.individualCharacters !== '') {
      return true;
    }

    return !(!info.digits && !info.whiteSpace && !info.lowerCaseLetters
      && !info.punctuationAndSymbols && !info.lineBreaks
      && !info.upperCaseLetters);
  }

  isValidControlCharactersInfo(info: ControlCharacters): boolean {
    return Object.keys(info).filter(cc => cc !== 'matchAllExceptSelectedOnes')
      .some(cc => info[cc]);
  }

  isValidDigitsInfo(info: Digits): boolean {
    const props = [];
    Object.values(info).forEach(prop => {
      if (typeof prop === 'object') {
        props.push(prop.minus);
        props.push(prop.optional);
      } else {
        props.push(prop);
      }
    });

    return props.some(d => d);
  }

  isValidListOfLiteralTextInfo(info: ListOfLiteralText): boolean {
    return info.literalText.every(llt => llt !== undefined && llt !== '');
  }

  isValidMatchAnythingInfo(info: MatchAnything, err: MatchAnythingErr): boolean {
    let valid: boolean;

    switch (info.matchAnythingExcept) {

      case 'Basic characters':
        const bc = info.basicCharacters;
        valid = !(!bc.lowerCaseLetters && !bc.digits && !bc.whiteSpace
          && !bc.upperCaseLetters && !bc.punctuationAndSymbols
          && !bc.lineBreaks);

        if (!valid) {
          err.basicCharactersMsg = 'Please select at least one of the options above!';
        }
        return valid;
      case 'Specific characters':
        valid = info.specificCharacters !== undefined && info.specificCharacters !== '';

        if (!valid) {
          err.specCharactersMsg = 'Please input character(s) that should not be matched in the field above!';
        }
        return valid;
      case 'Specific character':
        valid = info.specificCharacter !== undefined && /^.$/.test(info.specificCharacter);

        if (!valid) {
          err.specCharacterMsg = 'Please input the character that should not be matched in the field above!';
        }
        return valid;
      default:
        break;

    }

    return true;
  }

  isValidNumbersInfo(info: Numbers, err: NumbersErr): boolean {
    let valid = true;
    const min = info.minValOfIntPart;
    const max = info.maxValOfIntPart;

    if (info.limitIntegerPart) {
      if (min >= max) {
        err.integerPart = 'The min value should be less than the max value!';
        valid = false;
      }
    }

    const minDec = info.minNrOfDecimals;
    const maxDec = info.maxNrOfDecimals;
    if (minDec !== 0 || maxDec !== 0) {
      if (!(minDec > 0 && maxDec > 0 && minDec <= maxDec)) {
        err.decimalPart = 'Both values should be positive integers and min should be less than max!';
        valid = false;
      }
    }

    if (info.currencyCodes !== '') {
      if (!/^[A-Z]{3}(?:;[A-Z]{3})*$/.test(info.currencyCodes)) {
        err.currencyCodes = 'Currency codes should be three uppercase letters separated by semicolons!';
        valid = false;
      }
    }

    if (info.allowPlusSign && info.limitIntegerPart) {
      if (min <= 0 && max <= 0) {
        err.integerPart = '"Allow plus sign" ticked, but both values are negative!';
        valid = false;
      }
    }

    if (info.thousandSeparatorsAreRequired && info.thousandSeparator === 'None') {
      err.thousandSeparator = '"Thousand separators are required" ticked, but no separator selected!';
      valid = false;
    }

    if (info.currencySignOrCodeRequired && info.currencySign === 'None' && info.currencyCodes.trim() === '') {
      err.currencySignOrCode = '"Currency sign or code required" ticked, but no currency sign or code specified!';
      valid = false;
    }

    return valid;
  }

  isValidUnicodeCharactersInfo(info: UnicodeCharacters): boolean {
    const validUnicode = /^U\+[A-Z\d]{2,5}(?:-U\+[A-Z\d]{2,5})?(?: U\+[A-Z\d]{2,5}(?:-U\+[A-Z\d]{2,5})?)*$/;

    const validInput = info.individualCharacters === '' || validUnicode.test(info.individualCharacters);

    const checkboxes = Object.keys(info)
      .filter(cc => cc !== 'matchAllExceptSelectedOnes' && cc !== 'individualCharacters')
      .some(cc => info[cc]);

    if (validInput || checkboxes) {
      return !(!checkboxes && info.individualCharacters === '');
    } else {
      return false;
    }
  }

  isValidRepeatInfo(info: RepeatInfo): boolean {
    switch (info.repeat) {
      case 'Custom range':
        return info.start >= 0 && info.end >= 0 && info.start < info.end;
      case 'n or more times':
        return info.start >= 0;
      default:
        return true;
    }
  }

}
