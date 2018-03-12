import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Numbers } from './marker-info/numbers';
import { RepeatInfo } from './marker-info/repeat-info';

export class SampleStringsInfo {

  /* type of the specific marker */
  markerType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* semantical information about the marker  */
  markerInfo: MarkedText | BasicCharacters | Numbers;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: RepeatInfo;

}
