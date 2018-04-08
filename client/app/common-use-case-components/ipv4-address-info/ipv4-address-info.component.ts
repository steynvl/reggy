import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Ipv4Address } from '../../models/common-use-case-models/ipv4-address';

@Component({
  selector: 'app-ipv4-address-info',
  templateUrl: './ipv4-address-info.component.html',
  styleUrls: ['./ipv4-address-info.component.css']
})
export class Ipv4AddressInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  ipv4Address: Ipv4Address;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.ipv4Address = {
      dotted      : false,
      decimal     : false,
      hexadecimal1: false,
      hexadecimal2: false,
      hexadecimal3: false
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Password',
      information     : undefined,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    // if (this.isValidPasswordInfo()) {
    //   this.callService();
    // } else {
    //   this.toast.setMessage('Invalid input information!', 'warning');
    // }

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
