import { Component, OnInit } from '@angular/core';
import { InferrerService } from '../../../services/inferrer.service';
import { ToastComponent } from '../../../shared/toast/toast.component';
import { PayloadInteractiveLstar } from '../../../models/payload/payload-interactive-lstar';
import { InteractiveResponse } from '../../../models/server-response/interactive-response';

import Viz from 'viz.js';
import { Module, render } from 'viz.js/full.render.js';

@Component({
  selector: 'app-interactive-lstar',
  templateUrl: './interactive-lstar.component.html',
  styleUrls: ['./interactive-lstar.component.scss']
})
export class InteractiveLstarComponent implements OnInit {

  isLoading = false;

  isReading = true;
  providingInfo = false;
  provideInfoErr = false;
  isInferring = false;

  alphabet = '';
  positiveExamples = '';

  payload: PayloadInteractiveLstar;
  response: InteractiveResponse;

  getEquivalenceQuery = false;
  counterExample: string;
  counterExampleErr = false;

  state: string;
  membershipQueries: Array<string>;
  membershipAnswers: object;

  regex: string;

  constructor(private inferrerService: InferrerService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.isLoading = false;

    this.isReading = true;
    this.providingInfo = false;
    this.provideInfoErr = false;
    this.isInferring = false;
  }

  finishedInfoRead() {
    this.isReading = false;
    this.providingInfo = true;
  }

  startLearning() {
    if (this.alphabet === '') {
      this.provideInfoErr = true;
    } else {
      this.provideInfoErr = false;
      this.providingInfo = false;
      this.isInferring = true;

      this.membershipAnswers = {};
      this.state = 'start';

      this.membershipQueries = this.alphabet.split('');
      this.membershipQueries.push('');
      this.membershipQueries = this.removeDuplicates(this.membershipQueries);
      this.membershipQueries.forEach(mq => this.membershipAnswers[mq] = false);
    }
  }

  submitMembershipQueries() {
    this.payload = {
      algorithm: 'interactive lstar',
      positiveExamples: this.positiveExamples.split('\n'),
      alphabet: this.removeDuplicates(this.alphabet.split('')),
      stage: undefined,
      blue: undefined,
      red: undefined,
      observationTable: undefined,
      exp: undefined,
      sta: undefined,
      queryAnswers: this.membershipAnswers,
      counterExample: this.counterExample,
      closedMembershipQueries: false,
      consistentMembershipQueries: false
    };

    if (this.state === 'start') {
      this.payload.stage = 'start';
    } else {
      if (this.state === 'equivalenceQueries') {
        this.payload.stage = 'equivalenceQueries';
      } else {
        this.payload.stage = 'membershipQueries';
      }

      if (this.response.stage === 'closedMembershipQueries') {
        this.payload.closedMembershipQueries = true;
      } else if (this.response.stage === 'consistentMembershipQueries') {
        this.payload.consistentMembershipQueries = true;
      }
      this.payload.blue = this.response.blue;
      this.payload.red = this.response.red;
      this.payload.observationTable = this.response.observationTable;
      this.payload.exp = this.response.exp;
      this.payload.sta = this.response.sta;
    }

    this.isLoading = true;
    this.inferrerService.interactiveLstar(this.payload).subscribe(
      data => {
        this.response = data;

        if (data.stage === 'eq') {
          this.state = 'eq';
          this.showHypothesis('dfa1');
        } else {
          this.state = 'mq';
          this.membershipQueries = data.mq;
          this.membershipQueries.forEach(mq => this.membershipAnswers[mq] = false);
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('An unexpected error occurred on the server!', 'danger');
        this.isLoading = false;
      }
    );
  }

  showHypothesis(id: string) {
    this.getEquivalenceQuery = false;

    const viz = new Viz({ Module, render });
    viz.renderSVGElement(this.response.dot)
      .then(element => {
        document.getElementById(id).innerHTML = '';
        document.getElementById(id).appendChild(element);
      });
  }

  submitEquivalenceQuery() {
    if (!this.counterExample) {
      this.counterExampleErr = true;
      return;
    } else {
      this.counterExampleErr = false;
    }


    this.payload = {
      algorithm: 'interactive lstar',
      positiveExamples: this.positiveExamples.split('\n'),
      alphabet: this.removeDuplicates(this.alphabet.split('')),
      stage: 'counterExample',
      blue: this.response.blue,
      red: this.response.red,
      observationTable: this.response.observationTable,
      exp: this.response.exp,
      sta: this.response.sta,
      queryAnswers: this.membershipAnswers,
      counterExample: this.counterExample,
      closedMembershipQueries: false,
      consistentMembershipQueries: false
    };

    this.isLoading = true;
    this.inferrerService.interactiveLstar(this.payload).subscribe(
      data => {
        this.state = 'equivalenceQueries';
        this.response = data;
        this.membershipQueries = data.mq;
        this.membershipQueries.forEach(mq => this.membershipAnswers[mq] = false);
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('An unexpected error occurred on the server!', 'danger');
        this.isLoading = false;
      }
    );
  }

  fileChange(event) {
    const fileList: FileList = event.target.files;

    if (fileList.length === 1) {
      const reader = new FileReader();
      reader.readAsText(fileList[0]);

      reader.onload = () => {
        this.positiveExamples = reader.result;
      };
    }

  }

  removeDuplicates(values: Array<string>): Array<string> {
    return values.filter((e, i) => values.indexOf(e) === i);
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

  correct() {
    this.regex = this.response.regex;
    this.state = 'done';
    this.showHypothesis('dfa2');
  }

  restart() {
    this.isLoading = false;

    this.isReading = true;
    this.providingInfo = false;
    this.provideInfoErr = false;
    this.isInferring = false;
  }

}
