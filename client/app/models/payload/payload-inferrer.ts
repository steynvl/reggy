export interface PayloadInferrer {
  positiveExamples : Array<string>;
  negativeExamples : Array<string>;
  algorithm        : string;

  satisfied        : boolean;
  equivalenceQuery : string;
  membershipQueries: { string: boolean };
}
