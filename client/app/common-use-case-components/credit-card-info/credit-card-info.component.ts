import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { CreditCardNumber } from '../../models/common-use-cases/credit-card-number';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-credit-card-info',
  templateUrl: './credit-card-info.component.html',
  styleUrls: ['./credit-card-info.component.css']
})
export class CreditCardInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  creditCardNumber: CreditCardNumber;

  generatedRegex: GeneratedRegex;

  isLoading = false;

  constructor(private generateService: GenerateService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.creditCardNumber = {
      visa           : false,
      dinersClub     : false,
      masterCard     : false,
      discover       : false,
      americanExpress: false,
      jcb            : false,
      spacesAndDashes: 'No spaces or dashes'
    };

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Credit card number',
      information     : this.creditCardNumber,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    const ccn = this.creditCardNumber;

    if (!ccn.visa && !ccn.dinersClub && !ccn.masterCard && !ccn.discover
        && !ccn.americanExpress && !ccn.jcb) {
      this.toast.setMessage('Please select atleast one credit card number type!', 'warning');
    } else {
      this.callService();
    }
  }

  private callService() {
    this.isLoading = true;

    this.generatedRegex = undefined;
    const payload = this.constructPayload();
    this.generateService.generateRegex(payload).subscribe(
      data => {
        const response = data;
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = {
            regex        : response.regex,
            compiledRegex: response.compiledRegex
          };
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        this.isLoading = false;
      }
    );
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
