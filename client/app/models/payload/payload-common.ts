import { GeneralRegexInfo } from '../general-regex-info';
import { Username } from '../common-use-case-models/username';

export class PayloadCommon {

  /* type of the common use case */
  type: string;

  /* information about the common use case */
  information: Username;

  /* general information about the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
