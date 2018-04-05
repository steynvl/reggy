import { BasicCharacters } from './marker-info/basic-characters';
import { LiteralText } from './marker-info/literal-text';
import { Digits } from './marker-info/digits';
import { RepeatInfo } from './marker-info/repeat-info';
import { ControlCharacters } from './marker-info/control-characters';
import { UnicodeCharacters } from './marker-info/unicode-characters';
import { MatchAnything } from './marker-info/match-anything';

export class SampleStringsInfo {

  /* type of the specific marker */
  markerType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* semantical information about the marker  */
  markerInfo: LiteralText | BasicCharacters | Digits | ControlCharacters | UnicodeCharacters | MatchAnything;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: RepeatInfo;

}
