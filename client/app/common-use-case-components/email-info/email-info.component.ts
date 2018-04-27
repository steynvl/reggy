import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Email } from '../../models/common-use-case-models/email';

declare var jQuery: any;

@Component({
  selector: 'app-email-info',
  templateUrl: './email-info.component.html',
  styleUrls: ['./email-info.component.css']
})
export class EmailInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  email: Email;

  generatedRegex: string;
  isLoading = false;

  showUsernameErrorMsg: boolean;
  showDomainErrorMsg: boolean;

  domainErrorMsg: string;
  usernameErrorMsg: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    jQuery('[data-toggle="tooltip"]').tooltip({ trigger: 'hover' });

    this.email = {
      username                    : 'Allow any user name',
      domainName                  : 'Allow any domain name',
      mailtoPrefix                : 'No prefix',
      specificUserNamesOnly       : '',
      domainOnSpecificTld         : '',
      anySubDomainOnSpecificDomain: '',
      specificDomainsOnly         : ''
    };

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
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
    if (this.email.username === 'Specific user names only') {
      if (this.email.specificUserNamesOnly === undefined || this.email.specificUserNamesOnly.trim() === '') {
          this.usernameErrorMsg = 'Please specify usernames in the text box below!';
          this.showUsernameErrorMsg = true;
      } else if (!/^\w+(;\w+)*$/.test(this.email.specificUserNamesOnly)) {
          this.usernameErrorMsg = 'Only basic characters [a-zA-Z0-9_] allowed!';
          this.showUsernameErrorMsg = true;
      } else {
          this.showUsernameErrorMsg = false;
      }
    } else {
      this.showUsernameErrorMsg = false;
    }

    if (this.email.domainName === 'Allow any domain on specific TLD(s)') {
      if (this.email.domainOnSpecificTld === undefined || this.email.domainOnSpecificTld.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please specify a top-level domain in the text box below!';
      } else if (!/^[a-z]+(;[a-z]+)*$/.test(this.email.domainOnSpecificTld)) {
          this.showDomainErrorMsg = true;
          this.domainErrorMsg = 'Only top-level domains [a-z] separated by semicolons allowed!';
      } else {
        this.showDomainErrorMsg = false;
      }
    } else if (this.email.domainName === 'Allow any subdomain on specific domain(s)') {
      if (this.email.anySubDomainOnSpecificDomain === undefined || this.email.anySubDomainOnSpecificDomain.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please specify a domain in the text box below';
      } else if (!/^[a-z]+(\.[a-z]+)*(;[a-z]+(\.[a-z]+)*)*$/.test(this.email.anySubDomainOnSpecificDomain)) {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Only domains [a-z] separated by semicolons allowed!';
      } else {
        this.showDomainErrorMsg = false;
      }
    } else if (this.email.domainName === 'Specific domains only') {
      if (this.email.specificDomainsOnly === undefined || this.email.specificDomainsOnly.trim() === '') {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Please add specific domains to match in the text box below!';
      } else if (!/^[a-z]+(\.[a-z]+)*(;[a-z]+(\.[a-z]+)*)*$/.test(this.email.specificDomainsOnly)) {
        this.showDomainErrorMsg = true;
        this.domainErrorMsg = 'Only domains [a-z] separated by semicolons allowed!';
      } else {
        this.showDomainErrorMsg = false;
      }
    } else {
      this.showDomainErrorMsg = false;
    }

    if (this.showUsernameErrorMsg || this.showDomainErrorMsg) {
      this.toast.setMessage('Invalid input information!', 'warning');
    } else {
      this.callService();
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
          this.generatedRegex = response.regex;
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
