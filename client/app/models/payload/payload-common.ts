import { GeneralRegexInfo } from '../general-regex-info';
import { Username } from '../common-use-cases/username';
import { Password } from '../common-use-cases/password';
import { Email } from '../common-use-cases/email';
import { Url } from '../common-use-cases/url';
import { Guid } from '../common-use-cases/guid';
import { CreditCardNumber } from '../common-use-cases/credit-card-number';
import { NationalId } from '../common-use-cases/national-id';
import { VatNumber } from '../common-use-cases/vat-number';
import { Ipv4Address } from '../common-use-cases/ipv4-address';
import { Currency } from '../common-use-cases/currency';
import { DateAndTime } from '../common-use-cases/date-and-time';

export class PayloadCommon {

  /* type of the common use case */
  type: string;

  /* information home the common use case */
  information: Username | Password | Email | Url
    | Guid | CreditCardNumber | NationalId | VatNumber
    | Ipv4Address | Currency | DateAndTime;

  /* general information home the regex to generate */
  generalRegexInfo: GeneralRegexInfo;

  /* method the backend should use to generate the regex */
  generateMethod: string;

}
