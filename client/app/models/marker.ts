import { BasicCharacters } from './samples/basic-characters';
import { LiteralText } from './samples/literal-text';
import { Digits } from './samples/digits';
import { MarkedTextInfo } from './marked-text-info';
import { RepeatInfo } from './samples/repeat-info';
import { ControlCharacters } from './samples/control-characters';
import { UnicodeCharacters } from './samples/unicode-characters';
import { MatchAnything } from './samples/match-anything';
import { ListOfLiteralText } from './samples/list-of-literal-text';
import { Numbers } from './samples/numbers';
import { BasicCharactersErr } from './samples/basic-characters-err';
import { ControlCharactersErr } from './samples/control-characters-err';
import { DigitsErr } from './samples/digits-err';
import { ListOfLiteralTextErr } from './samples/list-of-literal-text-err';
import { MatchAnythingErr } from './samples/match-anything-err';
import { NumbersErr } from './samples/numbers-err';
import { UnicodeCharactersErr } from './samples/unicode-characters-err';
import { Backreference } from './samples/backreference';

export class Marker {

  id: number;
  colour: string;
  fieldType: string;
  markedTextInfo: Array<MarkedTextInfo>;

  markerInfo: BasicCharacters | LiteralText | Digits | ControlCharacters | UnicodeCharacters
    | MatchAnything | ListOfLiteralText | Numbers | Backreference;
  repeatInfo: RepeatInfo;

  error: BasicCharactersErr | ControlCharactersErr | DigitsErr | ListOfLiteralTextErr
    | MatchAnythingErr | NumbersErr | UnicodeCharactersErr;

  repeatInfoView: Array<string>;

}
