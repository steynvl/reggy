import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { VatNumber } from '../../models/common-use-case-models/vat-number';

@Component({
  selector: 'app-vat-number-info',
  templateUrl: './vat-number-info.component.html',
  styleUrls: ['./vat-number-info.component.css']
})
export class VatNumberInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  vatNumber: VatNumber;
  selectAll = false;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.vatNumber = {
      austria           : false,
      belgium           : false,
      bulgaria          : false,
      cyprus            : false,
      czechRepublic     : false,
      germany           : false,
      denmark           : false,
      slovakia          : false,
      estonia           : false,
      greece            : false,
      ireland           : false,
      poland            : false,
      spain             : false,
      italy             : false,
      portugal          : false,
      finland           : false,
      lithuania         : false,
      romania           : false,
      france            : false,
      luxembourg        : false,
      unitedKingdom     : false,
      latvia            : false,
      sweden            : false,
      croatia           : false,
      malta             : false,
      slovenia          : false,
      hungary           : false,
      netherlands       : false,
      countryCode       : 'No country code',
      groupingCharacters: 'None'
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'VAT number',
      information     : this.vatNumber,
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
      data => {
        const response = data;
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = response.regex;
        }
      },
      _ => this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger')
    );
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

  checkedSelectAll() {
    this.selectAll = !this.selectAll;

    Object.keys(this.vatNumber).forEach(prop => {
      if (prop !== 'countryCode' && prop !== 'groupingCharacters') {
        this.vatNumber[prop] = this.selectAll;
      }
    });
  }

}
