import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Email } from '../../models/common-use-case-models/email';

@Component({
  selector: 'app-email-info',
  templateUrl: './email-info.component.html',
  styleUrls: ['./email-info.component.css']
})
export class EmailInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  email: Email;

  generatedRegex: string;

  showUsernameErrorMsg: boolean;
  showDomainErrorMsg: boolean;

  domainErrorMsg: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.email = {
      username                    : 'Allow any user name',
      domainName                  : 'Allow any domain name',
      mailtoPrefix                : 'No prefix',
      specificUserNamesOnly       : '',
      domainOnSpecificTld         : '',
      anySubDomainOnSpecificDomain: '',
      specificDomainsOnly         : ''
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Email address',
      information     : this.email,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    this.generatedRegex = undefined;

    if (this.email.username === 'Specific user names only') {
      this.showUsernameErrorMsg = this.email.specificUserNamesOnly === undefined || this.email.specificUserNamesOnly.trim() === '';
    }

    if (this.email.domainName === 'Allow any domain on specific TLD') {
      if (this.email.domainOnSpecificTld === undefined || this.email.domainOnSpecificTld.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please specify a top-level domain in the text box below!';
      } else {
        this.showDomainErrorMsg = false;
      }
    } else if (this.email.domainName === 'Allow any subdomain on specific domain') {
      if (this.email.anySubDomainOnSpecificDomain === undefined || this.email.anySubDomainOnSpecificDomain.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please specify a domain in the text box below';
      } else {
        this.showDomainErrorMsg = false;
      }
    } else if (this.email.domainName === 'Specific domains only') {
      if (this.email.specificDomainsOnly === undefined || this.email.specificDomainsOnly.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please add specific domains to match in the text box below!';
      } else {
        this.showDomainErrorMsg = false;
      }
    }

    if (this.showUsernameErrorMsg || this.showDomainErrorMsg) {
      this.toast.setMessage('Invalid input information!', 'warning');
    } else {
      this.callService();
    }
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
