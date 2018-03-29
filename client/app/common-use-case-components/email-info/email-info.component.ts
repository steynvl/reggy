import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';

@Component({
  selector: 'app-email-info',
  templateUrl: './email-info.component.html',
  styleUrls: ['./email-info.component.css']
})
export class EmailInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  generatedRegex: string;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) {

  }

  ngOnInit() { }

  private constructPayload(): PayloadCommon {
    return null;
  }

  generateRegex() {
    if (this.isValidUrlInfo()) {
      this.callService();
    } else {
      this.toast.setMessage('Invalid input information!', 'warning');
    }

  }

  private callService() {
    const payload = JSON.stringify(this.constructPayload());
    this.generateCommonService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  isValidUrlInfo(): boolean {
    return true;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
