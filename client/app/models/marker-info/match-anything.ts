export class MatchAnything {
  matchAnythingExcept: string;
  specificCharacters : string;
  specificCharacter  : string;
  canSpanAcrossLines : boolean;
  basicCharacters: {
    lowerCaseLetters       : boolean;
    upperCaseLetters       : boolean;
    digits                 : boolean;
    punctuationAndSymbols  : boolean;
    whiteSpace             : boolean;
    lineBreaks             : boolean;
  };
}
