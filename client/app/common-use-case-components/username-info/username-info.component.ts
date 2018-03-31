import { Component, Input, OnInit } from '@angular/core';
import { Username } from '../../models/common-use-case-models/username';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';

@Component({
  selector: 'app-username-info',
  templateUrl: './username-info.component.html',
  styleUrls: ['./username-info.component.css']
})
export class UsernameInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  username: Username;

  shouldStartWithMsg = 'Should start with: ';
  shouldStartWithData = ['Anything', 'Letter', 'Letter or number', 'Lowercase letter', 'Uppercase letter'];

  shouldContainMsg = 'Should contain: ';
  shouldContainData = ['Lowercase letter', 'Number', 'Special character', 'Uppercase letter'];

  minimumLengthMsg = 'Minimum length (inclusive): ';
  minimumLengthData = ['1', '2', '3', '4', '5', 'Custom length'];
  minLengthIsCustom: boolean;

  maximumLengthMsg = 'Maximum length (inclusive): ';
  maximumLengthData = ['6', '7', '8', '9', '10', 'Custom length', 'No maximum length required'];
  maxLengthIsCustom: boolean;

  validLength = /^[1-9]\d*$/;

  generatedRegex: string;

  shouldStartWithIsValid   = true;
  minLengthIsValid         = true;
  maxLengthIsValid         = true;
  minRangeIsLess           = true;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) {

  }

  ngOnInit() {
    this.username = {
      shouldStartWith: '',
      shouldContain  : [],
      minimumLength  : '',
      maximumLength  : ''
    };
  }

  shouldStartWithChange(choice: string) {
    this.username.shouldStartWith = choice;
    this.shouldStartWithMsg = `Should start with: ${choice}`;
  }

  addToShouldContain(event: any, choice: string) {
    if (event.target.checked && this.username.shouldContain.indexOf(choice) === -1) {
      this.username.shouldContain.push(choice);
    } else {
      this.username.shouldContain = this.username.shouldContain.filter(u => u !== choice);
    }

    const newMsg = ['Should contain: '];
    if (this.username.shouldContain.length > 0) {
      newMsg.push('[');
      this.username.shouldContain.forEach((u, index) => {
        index === this.username.shouldContain.length - 1 ? newMsg.push(`${u}]`) : newMsg.push(`${u}, `);
      });
    }
    this.shouldContainMsg = newMsg.join('');
  }

  changeMinData(choice: string) {
    this.minLengthIsCustom = choice === 'Custom length';
    if (!this.minLengthIsCustom) {
      this.username.minimumLength = choice;
      this.minimumLengthMsg = `Minimum length (inclusive): ${choice}`;
      this.updateMaxLengths();
    }
  }

  minCustomChange() {
    this.minimumLengthMsg = `Minimum length (inclusive): ${this.username.minimumLength}`;
    this.updateMaxLengths();
  }

  updateMaxLengths() {
    const minVal = Number.parseInt(this.username.minimumLength);

    this.maximumLengthData = [];
    for (let i = 1; i <= 5; i++) {
      this.maximumLengthData.push((minVal + i).toString());
    }
    this.maximumLengthData.push('Custom length');
    this.maximumLengthData.push('No maximum length required');
  }

  changeMaxData(choice: string) {
    if (this.username.maximumLength !== 'No maximum length required') {
      this.maxLengthIsCustom = choice === 'Custom length';
      if (!this.maxLengthIsCustom) {
        this.username.maximumLength = choice;
        this.maximumLengthMsg = `Maximum length (exclusive): ${choice}`;
        this.updateMinLengths();
      }
    }
  }

  maxCustomChange() {
    this.maximumLengthMsg = `Maximum length (exclusive): ${this.username.maximumLength}`;
    this.updateMinLengths();
  }

  updateMinLengths() {
    const maxVal = Number.parseInt(this.username.maximumLength);

    this.minimumLengthData = [];
    for (let i = 5; i >= 1; i--) {
      const val = maxVal - i;
      if (val <= 0) {
        continue;
      }
      this.minimumLengthData.push(val.toString());
    }
    this.minimumLengthData.push('Custom length');
  }

  minRangeIsValid(): boolean {
    return this.validLength.test(this.username.minimumLength) &&
      Number.parseInt(this.username.minimumLength) <  Number.parseInt(this.username.maximumLength);
  }

  maxRangeIsValid(): boolean {
    return this.validLength.test(this.username.maximumLength) &&
      Number.parseInt(this.username.maximumLength) >  Number.parseInt(this.username.minimumLength);
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Username',
      information     : this.username,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    if (this.isValidUsernameInfo()) {
      this.callService();
    } else {
      this.toast.setMessage('Invalid input information!', 'warning');
    }
  }

  private callService() {
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  isValidUsernameInfo(): boolean {
    const validLength = /^[1-9]\d*$/;

    this.username.minimumLength += '';
    this.username.maximumLength += '';

    this.shouldStartWithIsValid = this.username.shouldStartWith.trim() !== '';
    this.minLengthIsValid = this.username.minimumLength.trim() !== '' && validLength.test(this.username.minimumLength);

    const noMaxLength = this.username.maximumLength === 'No maximum length required';
    if (noMaxLength) {
      this.maxLengthIsValid = true;
    } else {
      this.maxLengthIsValid = this.username.maximumLength.trim() !== '' && validLength.test(this.username.maximumLength);
    }

    if (!noMaxLength) {
      if (this.minLengthIsValid && this.maxLengthIsValid) {
        this.minRangeIsLess = Number.parseInt(this.username.minimumLength) < Number.parseInt(this.username.maximumLength);
      }
    } else {
      this.minRangeIsLess = true;
    }

    return this.shouldStartWithIsValid && this.minLengthIsValid && this.maxLengthIsValid && this.minRangeIsLess;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
