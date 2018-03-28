import { Component } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';

import { GenerateInductionService } from '../../services/generate.induction.service';

@Component({
  selector: 'app-generate-induction',
  templateUrl: './generate.induction.component.html',
  styleUrls: ['./generate.induction.component.css']
})
export class GenerateInductionComponent {

  // generatedRegex: string;
  // generalRegexInfo: GeneralRegexInfo;

  constructor(private generateService: GenerateInductionService,
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