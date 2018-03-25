import { GeneralRegexInfo } from '../general-regex-info';
import { SampleStringsInfo } from '../sample-strings-info';

export class PayloadSamples {

  /* array of sample strings info */
  sampleStringsInfo: Array<SampleStringsInfo>;

  /* general information about the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
