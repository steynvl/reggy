import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Numbers } from './marker-info/numbers';

export class SampleStringsInfo {

  /* field type of the specific marker */
  fieldType: string;

  /* array containing actual values highlighted by user for this marker */
  markedStrings: Array<string>;

  /* type of the marker */
  markerType: MarkerType;

  /* semantical information about the marker  */
  markerInfo: MarkedText | BasicCharacters | Numbers;

  /* tells us how many times the marker needs to be repeated */
  repeatInfo: string;

}
