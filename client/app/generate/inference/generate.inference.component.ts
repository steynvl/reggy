import { Component, OnInit } from '@angular/core';
import { InferrerService } from '../../services/inferrer.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Title } from '@angular/platform-browser';
import { PayloadInferrer } from '../../models/payload/payload-inferrer';

import Viz from 'viz.js';
import { Module, render } from 'viz.js/full.render.js';

@Component({
  selector: 'app-generate-inference',
  templateUrl: './generate.inference.component.html',
  styleUrls: ['./generate.inference.component.css']
})
export class GenerateInferenceComponent implements OnInit {

  isLoading = false;

  payload: PayloadInferrer;
  algorithm = 'Regular Positive and Negative Inference (RPNI) algorithm';
  positiveExamples = '';
  negativeExamples = '';
  dfaIsDisplayed = false;

  regex: string;

  constructor(private inferrerService: InferrerService,
              public toast: ToastComponent,
              private titleService: Title) {
  }

  ngOnInit() {
    this.titleService.setTitle('Inference | Reggy');

    this.payload = {
      positiveExamples : undefined,
      negativeExamples : undefined,
      algorithm        : undefined,
      satisfied        : undefined,
      equivalenceQuery : undefined,
      membershipQueries: undefined
    };

  }

  constructPayload() {
    switch (this.algorithm) {
      case 'Regular Positive and Negative Inference (RPNI) algorithm':
        this.payload.algorithm = 'rpni';
        break;
      case 'Angluin Learning (L*)':
        this.payload.algorithm = 'lstar';
        break;
      case 'Interactive Angluin Learning (L*)':
        this.payload.algorithm = 'interactive lstar';
        break;
      case 'E. Mark GOLD\'s algorithm':
        this.payload.algorithm = 'gold';
        break;
    }

    this.payload.positiveExamples = this.positiveExamples.split('\n');
    this.payload.negativeExamples = this.negativeExamples.split('\n');
  }

  inferGrammar() {
    this.isLoading = true;
    this.regex = undefined;
    this.dfaIsDisplayed = false;

    if (this.examplesIntersect()) {
      this.toast.setMessage('The sets of positive and negative example' +
        ' strings can not contain the same string(s).', 'warning', 5000);
    } else {
      this.constructPayload();
      this.inferrerService.inferGrammar(this.payload).subscribe(
        data => {

          if (data.code !== 0) {
            this.toast.setMessage('Unable to infer grammar, server responded with an error!', 'danger');
          } else {
            this.regex = data.regex;
            this.showDfa(data.dot);
          }
          this.isLoading = false;
        },
        _ => {
          this.toast.setMessage('Unable to infer grammar, server responded with an error!', 'danger');
          this.isLoading = false;
        }
      );
    }
  }

  showDfa(dot: string) {
    const viz = new Viz({ Module, render });

    viz.renderSVGElement(dot)
      .then(element => {
        this.dfaIsDisplayed = true;
        document.getElementById('dfa').innerHTML = '';
        document.getElementById('dfa').appendChild(element);
      });
  }

  examplesIntersect(): boolean {
    const positiveArr = this.positiveExamples.split('\n');
    const negativeArr = this.negativeExamples.split('\n');

    return positiveArr.some(s => negativeArr.indexOf(s) !== -1);
  }

  fileChange(event, positiveExamples: boolean) {
    const fileList: FileList = event.target.files;

    if (fileList.length === 1) {
      const reader = new FileReader();
      reader.readAsText(fileList[0]);

      reader.onload = () => {
        if (positiveExamples) {
          this.positiveExamples = reader.result;
        } else {
          this.negativeExamples = reader.result;
        }
      };
    }

  }

  canInfer(): boolean {
    return this.positiveExamples !== '' && this.negativeExamples !== '';
  }

  inferMethod(): string {
    switch (this.algorithm) {
      case 'Regular Positive and Negative Inference (RPNI) algorithm':
        return 'RPNI';
      case 'Angluin Learning (L*)':
        return 'L*';
      case 'E. Mark GOLD\'s algorithm':
        return 'GOLD';
    }
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
