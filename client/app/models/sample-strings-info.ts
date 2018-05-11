import { BasicCharacters } from './marker-info/basic-characters';
import { LiteralText } from './marker-info/literal-text';
import { Digits } from './marker-info/digits';
import { RepeatInfo } from './marker-info/repeat-info';
import { ControlCharacters } from './marker-info/control-characters';
import { UnicodeCharacters } from './marker-info/unicode-characters';
import { MatchAnything } from './marker-info/match-anything';
import { ListOfLiteralText } from './marker-info/list-of-literal-text';
import { Numbers } from './marker-info/numbers';

export class SampleStringsInfo {

  /* type of the specific marker */
  markerType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* semantical information home the marker  */
  markerInfo: LiteralText | BasicCharacters | Digits | ControlCharacters | UnicodeCharacters
    | MatchAnything | ListOfLiteralText | Numbers;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: RepeatInfo;

}
