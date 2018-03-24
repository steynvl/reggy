import { Component } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';

import { GenerateCommonService } from '../../services/generate.common.service';

@Component({
  selector: 'app-generate-common',
  templateUrl: './generate.common.component.html',
  styleUrls: ['./generate.common.component.css']
})
export class GenerateCommonComponent {

  // generatedRegex: string;
  // generalRegexInfo: GeneralRegexInfo;

  constructor(private generateService: GenerateCommonService,
              public toast: ToastComponent) {
  }

  // generateRegex() {
  //   this.generatedRegex = undefined;
  //
  //   const payload = JSON.stringify(this.constructPayload());
  //
  //   this.generateService.generateRegex(payload).subscribe(
  //     data => this.generatedRegex = data.trim(),
  //     error => console.log(error)
  //   );
  // }


  // clickCopyToClipboard() {
  //   this.toast.setMessage('Regex copied to clipboard! ', 'success');
  // }

}
