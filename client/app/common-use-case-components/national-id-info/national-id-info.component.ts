import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { NationalId } from '../../models/common-use-case-models/national-id';

@Component({
  selector: 'app-national-id-info',
  templateUrl: './national-id-info.component.html',
  styleUrls: ['./national-id-info.component.css']
})
export class NationalIdInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  nationalId: NationalId;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.nationalId = {
      kind: 'Austrian social security number'
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'National ID',
      information     : this.nationalId,
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
