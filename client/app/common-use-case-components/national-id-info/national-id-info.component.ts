import { Component, Input, OnInit } from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { NationalId } from '../../models/common-use-cases/national-id';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-national-id-info',
  templateUrl: './national-id-info.component.html',
  styleUrls: ['./national-id-info.component.scss']
})
export class NationalIdInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  nationalId: NationalId;

  generatedRegex: GeneratedRegex;
  isLoading = false;

  constructor(private generateService: GenerateService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.nationalId = {
      kind: 'Austrian social security number'
    };

    this.generalRegexInfo.startRegexMatchAt = 'Start of word';
    this.generalRegexInfo.endRegexMatchAt = 'End of word';
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

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
