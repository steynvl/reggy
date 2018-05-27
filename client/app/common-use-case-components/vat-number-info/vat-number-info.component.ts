import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { VatNumber } from '../../models/common-use-cases/vat-number';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-vat-number-info',
  templateUrl: './vat-number-info.component.html',
  styleUrls: ['./vat-number-info.component.css']
})
export class VatNumberInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  vatNumber: VatNumber;
  selectAll = false;
  isLoading = false;

  generatedRegex: GeneratedRegex;

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

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
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
    if (this.validInfo()) {
      this.callService();
    } else {
      this.toast.setMessage('Please select atleast one VAT number!', 'warning');
    }
  }

  private callService() {
    this.isLoading = true;

    this.generatedRegex = undefined;
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
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

  checkedSelectAll() {
    this.selectAll = !this.selectAll;

    Object.keys(this.vatNumber).forEach(prop => {
      if (prop !== 'countryCode' && prop !== 'groupingCharacters') {
        this.vatNumber[prop] = this.selectAll;
      }
    });
  }

  validInfo(): boolean {
    return Object.values(this.vatNumber).some(vatNr => {
      if (typeof vatNr === 'boolean') {
        return vatNr;
      }
    });
  }
}
