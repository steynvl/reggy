import { Component, OnInit } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';
import { GenerateCommonService } from '../../services/generate.common.service';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { Username } from '../../models/common-use-case-models/username';

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

  constructor(private generateService: GenerateCommonService,
              public toast: ToastComponent) {
  }

  ngOnInit() {
    this.generalRegexInfo = {
      startRegexMatchAt: 'Anywhere',
      endRegexMatchAt  : 'Anywhere',
      regexTarget      : 'Java'
    };
  }

  generateRegex() {
  //   this.generatedRegex = undefined;
  //
  //   const payload = JSON.stringify(this.constructPayload());
  //
  //   this.generateService.generateRegex(payload).subscribe(
  //     data => this.generatedRegex = data.trim(),
  //     error => console.log(error)
  //   );
  }


  // clickCopyToClipboard() {
  //   this.toast.setMessage('Regex copied to clipboard! ', 'success');
  // }

}
