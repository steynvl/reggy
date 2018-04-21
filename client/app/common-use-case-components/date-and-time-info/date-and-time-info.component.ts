import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { DateAndTime } from '../../models/common-use-case-models/date-and-time';
import { ServerResponse } from '../../models/server-response/server-response';

@Component({
  selector: 'app-date-and-time-info',
  templateUrl: './date-and-time-info.component.html',
  styleUrls: ['./date-and-time-info.component.css']
})
export class DateAndTimeInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  dateAndTime: DateAndTime;

  generatedRegex: string;

  isValidInfo = true;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.dateAndTime = {
      dateSeparator: 'Forward slash',
      timeSeparator: 'Colon',
      amPmIndicator: 'AM',
      leadingZeros : 'No leading zeros allowed',
      dateFormats  : ''
    };
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Date and time',
      information     : this.dateAndTime,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    if (this.isValidUrlInfo()) {
      this.callService();
    } else {
      this.isValidInfo = false;

      setTimeout(() => {
        this.isValidInfo = true;
      }, 5000);

      this.toast.setMessage('Invalid input information!', 'warning');
    }

  }

  private callService() {
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
      data => {
        const response = data;
        console.log(response);
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = response.regex;
        }
      },
      _ => this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger')
    );
  }

  isValidUrlInfo(): boolean {
    return this.dateAndTime.dateFormats.trim() !== '';
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
