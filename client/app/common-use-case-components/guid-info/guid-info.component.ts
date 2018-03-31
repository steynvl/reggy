import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Guid } from '../../models/common-use-case-models/guid';

@Component({
  selector: 'app-guid-info',
  templateUrl: './guid-info.component.html',
  styleUrls: ['./guid-info.component.css']
})
export class GuidInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  guid: Guid;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.guid = {
      bracesAround: 'Required',
      hyphensIn   : 'Required',
      guidCase    : 'Case insensitive'
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'GUID',
      information     : this.guid,
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
