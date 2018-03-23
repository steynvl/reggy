import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Digits } from './marker-info/digits';
import { RepeatInfo } from './marker-info/repeat-info';
import { ControlCharacters } from './marker-info/control-characters';

export class SampleStringsInfo {

  /* type of the specific marker */
  markerType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* semantical information about the marker  */
  markerInfo: MarkedText | BasicCharacters | Digits | ControlCharacters;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: RepeatInfo;

}
