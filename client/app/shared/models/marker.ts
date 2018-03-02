import { BasicCharacters } from './marker-info/basic-characters';
import { MarkedText } from './marker-info/marked-text';
import { Numbers } from './marker-info/numbers';

export class Marker {

  id: number;
  colour: string;
  fieldType: string;
  markerInfo: BasicCharacters | MarkedText | Numbers;

}
