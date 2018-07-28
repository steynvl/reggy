import { GeneralRegexInfo } from '../general-regex-info';
import { SampleStringsInfo } from '../sample-strings-info';

export class PayloadSamples {

  /* array of an array of sample strings info, the sub-arrays represents alternating groups */
  sampleStringsInfo: Array<Array<SampleStringsInfo>>;

  /* general information home the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
