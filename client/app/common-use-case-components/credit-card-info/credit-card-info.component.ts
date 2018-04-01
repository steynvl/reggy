import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { CreditCardNumber } from '../../models/common-use-case-models/credit-card-number';

@Component({
  selector: 'app-credit-card-info',
  templateUrl: './credit-card-info.component.html',
  styleUrls: ['./credit-card-info.component.css']
})
export class CreditCardInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  creditCardNumber: CreditCardNumber;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
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
    this.callService();
  }

  private callService() {
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
