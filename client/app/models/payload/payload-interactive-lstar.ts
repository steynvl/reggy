export interface PayloadInteractiveLstar {
  algorithm: string;

  positiveExamples: Array<string>;

  stage: string;
  alphabet: Array<string>;
  blue: Array<string>;
  red: Array<string>;
  observationTable: object;
  exp: Array<string>;
  sta: Array<string>;

  queryAnswers: object;
  counterExample: string;

  closedMembershipQueries: boolean;
  consistentMembershipQueries: boolean;
}
