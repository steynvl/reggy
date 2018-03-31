import { GeneralRegexInfo } from '../general-regex-info';
import { Username } from '../common-use-case-models/username';
import { Password } from '../common-use-case-models/password';
import { Email } from '../common-use-case-models/email';
import { Url } from '../common-use-case-models/url';
import { Guid } from '../common-use-case-models/guid';

export class PayloadCommon {

  /* type of the common use case */
  type: string;

  /* information about the common use case */
  information: Username | Password | Email | Url | Guid;

  /* general information about the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
