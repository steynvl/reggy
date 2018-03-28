import { Component, OnInit } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';
import { GenerateCommonService } from '../../services/generate.common.service';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { Username } from '../../models/common-use-case-models/username';
import { ValidateCommon } from '../../validation/validate.common';
import { PayloadCommon } from '../../models/payload/payload-common';

@Component({
  selector: 'app-generate-common',
  templateUrl: './generate.common.component.html',
  styleUrls: ['./generate.common.component.css']
})
export class GenerateCommonComponent implements OnInit {

  type: string;

  username: Username;

  generatedRegex: string;
  generalRegexInfo: GeneralRegexInfo;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) {
  }

  ngOnInit() {
    this.generalRegexInfo = {
      startRegexMatchAt: 'Anywhere',
      endRegexMatchAt  : 'Anywhere',
      regexTarget      : 'Java'
    };
    this.username = {
      shouldStartWith: '',
      shouldContain  : [],
      minimumLength  : '',
      maximumLength  : ''
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : this.type,
      information     : this.username,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  private callService() {
    const payload = JSON.stringify(this.constructPayload());
    this.generateCommonService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  generateRegex() {
    this.generatedRegex = undefined;

    switch (this.type) {
      case 'Username':
        console.log(this.username);
        if (ValidateCommon.isValidUsernameInfo(this.username)) {
          this.callService();
        } else {
          this.toast.setMessage('Invalid input information!', 'warning');
        }
        break;

      case 'Password':

        break;

      case 'Email address':

        break;

      case 'URL':

        break;

      default:
        // TODO
        break;

    }

    // const payload = JSON.stringify(this.constructPayload());

    // this.generateService.generateRegex(payload).subscribe(
    //   data => this.generatedRegex = data.trim(),
    //   error => console.log(error)
    // );
  }


  // clickCopyToClipboard() {
  //   this.toast.setMessage('Regex copied to clipboard! ', 'success');
  // }

}
