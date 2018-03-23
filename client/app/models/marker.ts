import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Digits } from './marker-info/digits';
import { MarkedTextInfo } from './marked-text-info';
import { RepeatInfo } from './marker-info/repeat-info';
import { ControlCharacters } from './marker-info/control-characters';
import { UnicodeCharacters } from './marker-info/unicode-characters';

export class Marker {

  id: number;
  colour: string;
  fieldType: string;
  markedTextInfo: Array<MarkedTextInfo>;
  markerInfo: BasicCharacters | MarkedText | Digits | ControlCharacters | UnicodeCharacters;
  repeatInfo: RepeatInfo;

  repeatInfoView: Array<string>;

}
