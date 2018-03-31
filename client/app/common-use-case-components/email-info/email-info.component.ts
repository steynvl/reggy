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

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) {
  }

  ngOnInit() {
    this.email = {
      username    : 'Allow any user name',
      domainName  : 'Allow any domain name',
      mailtoPrefix: 'No prefix'
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
