import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { DateAndTime } from '../../models/common-use-case-models/date-and-time';
import { ServerResponse } from '../../models/server-response/server-response';

declare var jQuery: any;

@Component({
  selector: 'app-date-and-time-info',
  templateUrl: './date-and-time-info.component.html',
  styleUrls: ['./date-and-time-info.component.css']
})
export class DateAndTimeInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  dateAndTime: DateAndTime;

  generatedRegex: string;
  isLoading = false;

  isValidInfo = true;
  errorMsg: string;
  
  showInfo = false;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    jQuery('[data-toggle="tooltip"]').tooltip({ trigger: 'hover' });

    this.dateAndTime = {
      dateSeparator: 'Forward slash',
      timeSeparator: 'Colon',
      amPmIndicator: 'AM',
      leadingZeros : 'No leading zeros allowed',
      dateFormats  : ''
    };

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
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
      this.errorMsg = undefined;
      this.callService();
    } else {
      this.isValidInfo = false;

      setTimeout(() => {
        this.isValidInfo = true;
      }, 3000);

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
          this.generatedRegex = response.regex.trim();
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        this.isLoading = false;
      }
    );
  }

  isValidUrlInfo(): boolean {
    const input = this.dateAndTime.dateFormats.trim();
    const validChars = /^[dmyYhHns/a:\s]+$/

    if (input === '') {
      this.errorMsg = 'Please input a date format to match in the text box above!';
      return false;
    } else {
      this.errorMsg = 'Only the characters a,d,m,y,Y,h,H,n,s/,: are allowed in the text box!';
    }

    return /^[dmyYhHns/a:\s]+$/.test(this.dateAndTime.dateFormats.trim())
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
