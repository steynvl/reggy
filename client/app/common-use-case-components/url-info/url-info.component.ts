import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Url } from '../../models/common-use-case-models/url';

declare var jQuery: any;

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

  portNumbersErr    : string;
  userNamesErr      : string;
  domainNameErr     : string;
  foldersErr        : string;
  foldersMinDepthErr: string;
  foldersMaxDepthErr: string;
  fileNamesErr      : string;
  parametersErr     : string;

  validNumberRe      = /^(?:0|[1-9]\d*)$/;
  validPortNumbersRe = /^(\d+;)*\d+$/;
  validTldRe         = /^[a-z]+(;[a-z]+)*$/;
  validSubDomainRe   = /^[a-z]+(\.[a-z]+)*(;[a-z]+(\.[a-z]+)*)*$/;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    jQuery('[data-toggle="tooltip"]').tooltip({ trigger: 'hover' });

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
      this.toast.setMessage('Invalid input information!', 'warning');
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
      } else if (!/^(\w+)(;\w+)*$/.test(u)) {
        this.userNamesErr = 'Only basic characters [a-zA-Z0-9_] allowed!';
      } else {
        this.userNamesErr = undefined;
      }
    }

    if (this.url.domainName === 'Allow any domain on specific TLD(s)') {
      if (this.url.specificTld === undefined || this.url.specificTld.trim() === '') {
        this.domainNameErr = 'Please specify a top-level domain in the text box above!';
      } else if (!this.validTldRe.test(this.url.specificTld)) {
        this.domainNameErr = 'Only top-level domains [a-z] separated by semicolons allowed!';
      } else {
        this.domainNameErr = undefined;
      }
    } else if (this.url.domainName === 'Allow any subdomain on specific domain(s)') {
      if (this.url.subdomainOnSpecDomain === undefined || this.url.subdomainOnSpecDomain.trim() === '') {
        this.domainNameErr = 'Please specify a domain in the text box below!';
      } else if (!this.validSubDomainRe.test(this.url.subdomainOnSpecDomain)) {
        this.domainNameErr = 'Only domains [a-z] separated by semicolons allowed!';
      } else {
        this.domainNameErr = undefined;
      }
    } else if (this.url.domainName === 'Specific domains only') {
      if (this.url.specDomainNames === undefined || this.url.specDomainNames.trim() === '') {
        this.domainNameErr = 'Please add specific domains to match in the text box below!';
      } else if (!this.validSubDomainRe.test(this.url.specDomainNames)) {
        this.domainNameErr = 'Only domains [a-z] separated by semicolons allowed!';
      } else {
        this.domainNameErr = undefined;
      }
    } else {
      this.domainNameErr = undefined;
    }

    if (this.url.folders === 'Specific folders only') {
      const f = this.url.specFoldersOnly;

      if (f === undefined || f.trim() === '') {
        this.foldersErr = 'Please specify folders!';
      } else if (!/^(\/?(?:[a-z]+\/)+)(;\/?(?:[a-z]+\/)+)*$/.test(f)) {
        this.foldersErr = 'Wrong format!';
      } else {
        this.foldersErr = undefined;
      }

      this.foldersMinDepthErr = undefined;
      this.foldersMaxDepthErr = undefined;
    } else if (this.url.folders !== 'No folders') {

      if (this.url.minFolderDepth === undefined || !this.validNumberRe.test(this.url.minFolderDepth)) {
        this.foldersMinDepthErr = 'Invalid number!';
      } else {
        this.foldersMinDepthErr = undefined;
      }

      if (this.url.maxFolderDepth === undefined || !this.validNumberRe.test(this.url.maxFolderDepth)) {
        this.foldersMaxDepthErr = 'Invalid number!';
      } else {
        this.foldersMaxDepthErr = undefined;
      }

    }

    if (this.url.fileNames === 'Specific extensions only') {
      const f = this.url.specExtensions;

      if (f === undefined || f.trim() === '') {
        this.fileNamesErr = 'Please specify extensions!';
      } else if (!/^\.?[a-z]+(;\.?[a-z]+)*$/.test(f)) {
        this.fileNamesErr = 'Wrong format!';
      } else {
        this.fileNamesErr = undefined;
      }

    } else if (this.url.fileNames === 'Specific file names only') {
      const f = this.url.specFileNames;

      if (f === undefined || f.trim() === '') {
        this.fileNamesErr = 'Please specify filenames!';
      } else if (!/^[a-z]+(?:\.[a-z]+)?(;[a-z]+(?:\.[a-z]+)?)*$/.test(f)) {
        this.fileNamesErr = 'Wrong format!';
      } else {
        this.fileNamesErr = undefined;
      }

    } else {
      this.fileNamesErr = undefined;
    }

    if (this.url.parameters === 'Specific parameters only') {
      const p = this.url.specParameters;

      if (p === undefined || p.trim() === '') {
        this.parametersErr = 'Please specify parameters!';
      } else if (!/^[a-z]+(?:;[a-z]+)*$/.test(p)) {
        this.parametersErr = 'Wrong format!';
      } else {
        this.parametersErr = undefined;
      }
    }

    return !this.portNumbersErr && !this.userNamesErr && !this.domainNameErr
      && !this.foldersErr && !this.foldersMinDepthErr && !this.foldersMaxDepthErr
      && !this.fileNamesErr && !this.parametersErr;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
