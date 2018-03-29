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
export class UsernameComponent implements OnInit {

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
  maximumLengthData = ['6', '7', '8', '9', '10', 'Custom length'];
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
      // TODO update max length options
    }
  }

  minCustomChange() {
    this.minimumLengthMsg = `Minimum length (inclusive): ${this.username.minimumLength}`;
    // TODO update max length options
  }

  changeMaxData(choice: string) {
    this.maxLengthIsCustom = choice === 'Custom length';
    if (!this.maxLengthIsCustom) {
      this.username.maximumLength = choice;
      this.maximumLengthMsg = `Maximum length (exclusive): ${choice}`;
      // TODO update min values
    }
  }

  maxCustomChange() {
    this.maximumLengthMsg = `Maximum length (exclusive): ${this.username.maximumLength}`;
    // TODO update min length options
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

      console.log('not valid');
      console.log(this.shouldStartWithIsValid);
      console.log(this.minLengthIsValid);
      console.log(this.maxLengthIsValid);
      console.log(this.minRangeIsLess);

      this.toast.setMessage('Invalid input information!', 'warning');
    }

  }

  private callService() {
    const payload = JSON.stringify(this.constructPayload());
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
    this.maxLengthIsValid = this.username.maximumLength.trim() !== '' && validLength.test(this.username.maximumLength);

    if (this.minLengthIsValid && this.maxLengthIsValid) {
        this.minRangeIsLess = Number.parseInt(this.username.minimumLength) < Number.parseInt(this.username.maximumLength);
    }

    return this.shouldStartWithIsValid && this.minLengthIsValid && this.maxLengthIsValid && this.minRangeIsLess;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
