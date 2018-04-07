import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Url } from '../../models/common-use-case-models/url';

@Component({
  selector: 'app-url-info',
  templateUrl: './url-info.component.html',
  styleUrls: ['./url-info.component.css']
})
export class UrlInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  url: Url;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.url = {
      schemes                : 'http',
      portNumbers            : 'No port number',
      specOptionalPortNumbers: '',
      specRequiredPortNumbers: '',
      username               : 'No user names',
      specUserNames          : '',
      password               : 'No password',
      domainName             : 'Allow any domain name',
      folders                : 'No folders',
      fileNames              : 'No file names',
      parameters             : 'No parameters'
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'URL',
      information     : this.url,
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
