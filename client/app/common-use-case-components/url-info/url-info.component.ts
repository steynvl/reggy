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
  isLoading = false;

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
      specDomainNames        : '',
      specificTld            : '',
      subdomainOnSpecDomain  : '',
      folders                : 'No folders',
      minFolderDepth         : '',
      maxFolderDepth         : '',
      specFoldersOnly        : '',
      specPathsOnly          : '',
      fileNames              : 'No file names',
      specExtensions         : '',
      specFileNames          : '',
      optionalFileNames      : false,
      parameters             : 'No parameters',
      specParameters         : ''
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
    if (this.generatedRegex === undefined) {
      this.isLoading = true;
    }

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
