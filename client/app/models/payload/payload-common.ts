import { GeneralRegexInfo } from '../general-regex-info';
import { Username } from '../common-use-case-models/username';
import { Password } from '../common-use-case-models/password';
import { Email } from '../common-use-case-models/email';
import { Url } from '../common-use-case-models/url';
import { Guid } from '../common-use-case-models/guid';
import { CreditCardNumber } from '../common-use-case-models/credit-card-number';
import { NationalId } from '../common-use-case-models/national-id';
import { VatNumber } from '../common-use-case-models/vat-number';
import { Ipv4Address } from '../common-use-case-models/ipv4-address';
import { Currency } from '../common-use-case-models/currency';

export class PayloadCommon {

  /* type of the common use case */
  type: string;

  /* information about the common use case */
  information: Username | Password | Email | Url
    | Guid | CreditCardNumber | NationalId | VatNumber
    | Ipv4Address | Currency;

  /* general information about the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
