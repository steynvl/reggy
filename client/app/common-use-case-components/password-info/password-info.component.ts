import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Password } from '../../models/common-use-case-models/password';

@Component({
  selector: 'app-password-info',
  templateUrl: './password-info.component.html',
  styleUrls: ['./password-info.component.css']
})
export class PasswordInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  password: Password;

  shouldStartWithMsg = 'Should start with: ';
  shouldStartWithData = ['Anything', 'Digit', 'Letter', 'Letter or digit', 'Lowercase letter', 'Uppercase letter'];

  shouldContainMsg = 'Should contain: ';
  shouldContainData = ['Bracket', 'Digit', 'Lowercase letter', 'Minus', 'Whitespace', 'Special character', 'Underline', 'Uppercase letter'];

  minimumLengthMsg = 'Minimum length (inclusive): ';
  minimumLengthData = ['4', '5', '6', '7', '8', 'Custom length'];
  minLengthIsCustom: boolean;

  maximumLengthMsg = 'Maximum length (inclusive): ';
  maximumLengthData = ['9', '10', '11', '12', '13', 'Custom length', 'No maximum length required'];
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
    this.password = {
      shouldStartWith: '',
      shouldContain  : [],
      minimumLength  : '',
      maximumLength  : ''
    };
  }

  shouldStartWithChange(choice: string) {
    this.password.shouldStartWith = choice;
    this.shouldStartWithMsg = `Should start with: ${choice}`;
  }

  addToShouldContain(event: any, choice: string) {
    if (event.target.checked && this.password.shouldContain.indexOf(choice) === -1) {
      this.password.shouldContain.push(choice);
    } else {
      this.password.shouldContain = this.password.shouldContain.filter(u => u !== choice);
    }

    const newMsg = ['Should contain: '];
    if (this.password.shouldContain.length > 0) {
      newMsg.push('[');
      this.password.shouldContain.forEach((u, index) => {
        index === this.password.shouldContain.length - 1 ? newMsg.push(`${u}]`) : newMsg.push(`${u}, `);
      });
    }
    this.shouldContainMsg = newMsg.join('');
  }

  changeMinData(choice: string) {
    this.minLengthIsCustom = choice === 'Custom length';
    if (!this.minLengthIsCustom) {
      this.password.minimumLength = choice;
      this.minimumLengthMsg = `Minimum length (inclusive): ${choice}`;
      // TODO update max length options
    }
  }

  minCustomChange() {
    this.minimumLengthMsg = `Minimum length (inclusive): ${this.password.minimumLength}`;
    // TODO update max length options
  }

  changeMaxData(choice: string) {
    if (this.password.maximumLength !== 'No maximum length required') {
      this.maxLengthIsCustom = choice === 'Custom length';
      if (!this.maxLengthIsCustom) {
        this.password.maximumLength = choice;
        this.maximumLengthMsg = `Maximum length (exclusive): ${choice}`;
        // TODO update min values
      }
    }
  }

  maxCustomChange() {
    this.maximumLengthMsg = `Maximum length (exclusive): ${this.password.maximumLength}`;
    // TODO update min length options
  }

  minRangeIsValid(): boolean {
    return this.validLength.test(this.password.minimumLength) &&
      Number.parseInt(this.password.minimumLength) <  Number.parseInt(this.password.maximumLength);
  }

  maxRangeIsValid(): boolean {
    return this.validLength.test(this.password.maximumLength) &&
      Number.parseInt(this.password.maximumLength) >  Number.parseInt(this.password.minimumLength);
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Password',
      information     : this.password,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    if (this.isValidPasswordInfo()) {
      this.callService();
    } else {
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

  isValidPasswordInfo(): boolean {
    const validLength = /^[1-9]\d*$/;

    this.password.minimumLength += '';
    this.password.maximumLength += '';

    this.shouldStartWithIsValid = this.password.shouldStartWith.trim() !== '';
    this.minLengthIsValid = this.password.minimumLength.trim() !== '' && validLength.test(this.password.minimumLength);

    const noMaxLength = this.password.maximumLength === 'No maximum length required';
    if (noMaxLength) {
      this.maxLengthIsValid = true;
    } else {
      this.maxLengthIsValid = this.password.maximumLength.trim() !== '' && validLength.test(this.password.maximumLength);
    }

    if (!noMaxLength) {
      if (this.minLengthIsValid && this.maxLengthIsValid) {
        this.minRangeIsLess = Number.parseInt(this.password.minimumLength) < Number.parseInt(this.password.maximumLength);
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