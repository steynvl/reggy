import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Numbers } from './marker-info/numbers';
import { MarkedTextInfo } from './marked-text-info';

export class Marker {

  id: number;
  colour: string;
  fieldType: string;
  markedTextInfo: Array<MarkedTextInfo>;
  markerInfo: BasicCharacters | MarkedText | Numbers;

}
