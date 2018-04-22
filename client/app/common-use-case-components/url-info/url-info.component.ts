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

  portNumbersErr: string;
  userNamesErr  : string;
  domainNameErr : string;
  foldersErr    : string;
  fileNamesErr  : string;
  parametersErr : string;

  validPortNumbersRe = /^(\d+;)*\d+$/;

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

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
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
    if (this.isValidUrl()) {
      this.callService();
    } else {
      this.toast.setMessage('Invalid input information!', 'warning')
    }
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

  isValidUrl(): boolean {
    if (this.url.portNumbers === 'Specify optional port numbers' || this.url.portNumbers === 'Specify required port numbers') {
      const p = this.url.portNumbers === 'Specify optional port numbers'
                ? this.url.specOptionalPortNumbers 
                : this.url.specRequiredPortNumbers;
      
      if (p.trim() === '') {
        this.portNumbersErr = 'Please specify port numbers separated by semicolons above!';
      } else if (!this.validPortNumbersRe.test(p)) {
        this.portNumbersErr = 'Wrong format, only digits separated by semicolons allowed!';
      } else {
        this.portNumbersErr = undefined;
      }
    }

    if (this.url.username === 'Specific user names only') {
      const u = this.url.specUserNames;

      if (u.trim() === '') {
        this.userNamesErr = 'Please specify usernames separated by semicolons!';
      } else if (!/^\w+$/.test(u)) {
        this.userNamesErr = 'Only basic characters [a-zA-Z0-9_] allowed!';
      } else {
        this.userNamesErr = undefined;
      }
    }

    if (this.url.domainName === 'Allow any domain on specific TLD'
                || this.url.domainName === 'Allow any subdomain on specific domain'
                || this.url.domainName === 'Specific domains only') {
          
      // TODO domain names
    }

    if (this.url.folders === 'Specific folders only' || this.url.folders === 'Specific paths only') {
      const f = this.url.portNumbers === 'Specific folders only'
      ? this.url.specFoldersOnly 
      : this.url.specFileNames;
      
      // TODO folders
    }

    if (this.url.fileNames === 'Specific extensions only' || this.url.fileNames === 'Specific file names only') {
      const f = this.url.fileNames === 'Specific extensions only'
      ? this.url.specExtensions
      : this.url.specFileNames;

      // TODO file names
    }

    if (this.url.parameters === 'Specific parameters only') {
      const p = this.url.specParameters;

      // TODO parameters
    }

    return !this.portNumbersErr && !this.userNamesErr && !this.domainNameErr
      && !this.foldersErr && !this.fileNamesErr && !this.parametersErr;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
