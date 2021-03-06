import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { DateAndTime } from '../../models/common-use-cases/date-and-time';
import { GeneratedRegex } from '../../models/generated-regex';

declare var jQuery: any;

@Component({
  selector: 'app-date-and-time-info',
  templateUrl: './date-and-time-info.component.html',
  styleUrls: ['./date-and-time-info.component.scss']
})
export class DateAndTimeInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  dateAndTime: DateAndTime;

  generatedRegex: GeneratedRegex;
  isLoading = false;

  isValidInfo = true;
  errorMsg: string;

  showInfo = false;

  constructor(private generateService: GenerateService,
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
    this.generateService.generateRegex(payload).subscribe(
      data => {
        const response = data;
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = {
            regex        : response.regex,
            compiledRegex: response.compiledRegex
          };
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
    const validChars = /^[dmyYhHns/a:\s]+$/;

    if (input === '') {
      this.errorMsg = 'Please input a date format to match in the text box above!';
      return false;
    } else {
      this.errorMsg = 'Only the characters a,d,m,y,Y,h,H,n,s/,: are allowed in the text box!';
    }

    return validChars.test(this.dateAndTime.dateFormats.trim());
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
