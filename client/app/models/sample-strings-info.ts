import { BasicCharacters } from './samples/basic-characters';
import { LiteralText } from './samples/literal-text';
import { Digits } from './samples/digits';
import { RepeatInfo } from './samples/repeat-info';
import { ControlCharacters } from './samples/control-characters';
import { UnicodeCharacters } from './samples/unicode-characters';
import { MatchAnything } from './samples/match-anything';
import { ListOfLiteralText } from './samples/list-of-literal-text';
import { Numbers } from './samples/numbers';
import { Backreference } from './samples/backreference';

export class SampleStringsInfo {

  /* type of the specific marker */
  markerType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* semantical information home the marker  */
  markerInfo: LiteralText | BasicCharacters | Digits | ControlCharacters | UnicodeCharacters
    | MatchAnything | ListOfLiteralText | Numbers | Backreference;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: RepeatInfo;

}
