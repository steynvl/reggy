import { Component, OnInit } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-generate-induction',
  templateUrl: './generate.induction.component.html',
  styleUrls: ['./generate.induction.component.css']
})
export class GenerateInductionComponent implements OnInit {

  // generatedRegex: string;
  // generalRegexInfo: GeneralRegexInfo;

  constructor(private generateService: GenerateService,
              public toast: ToastComponent,
              private titleService: Title) {
  }


  ngOnInit() {
    this.titleService.setTitle('Induction | Reggy');
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
