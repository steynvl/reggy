import { Component, OnInit } from '@angular/core';
import { InferrerService } from '../../../services/inferrer.service';
import { ToastComponent } from '../../../shared/toast/toast.component';
import { PayloadInferrer } from '../../../models/payload/payload-inferrer';

import Viz from 'viz.js';
import { Module, render } from 'viz.js/full.render.js';

@Component({
  selector: 'app-interactive-lstar',
  templateUrl: './interactive-lstar.component.html',
  styleUrls: ['./interactive-lstar.component.css']
})
export class InteractiveLstarComponent implements OnInit {

  isLoading = false;

  isReading = true;
  providingInfo = false;
  provideInfoErr = false;
  isInferring = false;

  alphabet = '';

  payload: PayloadInferrer;
  positiveExamples = '';

  regex: string;

  constructor(private inferrerService: InferrerService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.isLoading = false;

    this.isReading = true;
    this.providingInfo = false;
    this.provideInfoErr = false;
    this.isInferring = false;

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

  }

  inferGrammar() {

  }

  showDfa(dot: string) {
    // const viz = new Viz({ Module, render });
    //
    // viz.renderSVGElement(dot)
    //   .then(element => {
    //     this.dfaIsDisplayed = true;
    //     document.getElementById('dfa').innerHTML = '';
    //     document.getElementById('dfa').appendChild(element);
    //   });
  }

  finishedInfoRead() {
    this.isReading = false;
    this.providingInfo = true;
  }

  startLearning() {
    if (this.alphabet === '') {
      this.provideInfoErr = true;
    } else {
      this.payload.positiveExamples = this.positiveExamples.split('\n');
      this.provideInfoErr = false;
      this.providingInfo = false;
      this.isInferring = true;
    }
  }

  fileChange(event, positiveExamples: boolean) {
    const fileList: FileList = event.target.files;

    if (fileList.length === 1) {
      const reader = new FileReader();
      reader.readAsText(fileList[0]);

      reader.onload = () => {
        this.positiveExamples = reader.result;
      };
    }

  }

  finishedReading() {
    this.isReading = false;

  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
