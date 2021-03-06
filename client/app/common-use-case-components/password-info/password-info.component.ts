import { Component, Input, OnInit } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Password } from '../../models/common-use-cases/password';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-password-info',
  templateUrl: './password-info.component.html',
  styleUrls: ['./password-info.component.scss']
})
export class PasswordInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  password: Password;
  isLoading = false;

  shouldStartWithMsg = 'Should start with: ';
  shouldStartWithData = ['Anything', 'Digit', 'Letter', 'Letter or digit', 'Lowercase letter', 'Uppercase letter'];

  shouldContainMsg = 'Should contain: ';
  shouldContainData = ['Digit', 'Lowercase letter', 'Minus', 'Whitespace', 'Special character', 'Underline', 'Uppercase letter'];

  minimumLengthMsg = 'Minimum length (inclusive): ';
  minimumLengthData = ['4', '5', '6', '7', '8', 'Custom length'];
  minLengthIsCustom: boolean;

  maximumLengthMsg = 'Maximum length (exclusive): ';
  maximumLengthData = ['9', '10', '11', '12', '13', 'Custom length', 'No maximum length required'];
  maxLengthIsCustom: boolean;

  validLength = /^[1-9]\d*$/;

  generatedRegex: GeneratedRegex;

  shouldStartWithIsValid   = true;
  minLengthIsValid         = true;
  maxLengthIsValid         = true;
  minRangeIsLess           = true;

  constructor(private generateService: GenerateService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.password = {
      shouldStartWith: '',
      shouldContain  : [],
      minimumLength  : '',
      maximumLength  : ''
    };

    this.generalRegexInfo.startRegexMatchAt = 'Start of line';
    this.generalRegexInfo.endRegexMatchAt = 'End of line';
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
      this.updateMaxLengths();
    }
  }

  minCustomChange() {
    this.minimumLengthMsg = `Minimum length (inclusive): ${this.password.minimumLength}`;
    this.updateMaxLengths();
  }

  updateMaxLengths() {
    const minVal = Number.parseInt(this.password.minimumLength);

    this.maximumLengthData = [];
    for (let i = 1; i <= 5; i++) {
      this.maximumLengthData.push((minVal + i).toString());
    }
    this.maximumLengthData.push('Custom length');
    this.maximumLengthData.push('No maximum length required');
  }

  changeMaxData(choice: string) {
    this.password.maximumLength = choice;

    if (choice === 'No maximum length required') {
      this.maximumLengthMsg = `Maximum length (exclusive): ${choice}`;
      this.maxLengthIsCustom = false;
    } else {
      this.maxLengthIsCustom = choice === 'Custom length';
      if (!this.maxLengthIsCustom) {
        this.maximumLengthMsg = `Maximum length (exclusive): ${choice}`;
        this.updateMinLengths();
      }
    }
  }

  maxCustomChange() {
    this.maximumLengthMsg = `Maximum length (exclusive): ${this.password.maximumLength}`;
    this.updateMinLengths();
  }

  updateMinLengths() {
    const maxVal = Number.parseInt(this.password.maximumLength);

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
    if (this.password.maximumLength === 'No maximum length required') {
      return /^\d+$/.test(this.password.minimumLength);
    }

    return this.validLength.test(this.password.minimumLength) && /^\d+$/.test(this.password.minimumLength) &&
      Number.parseInt(this.password.minimumLength) <  Number.parseInt(this.password.maximumLength);
  }

  maxRangeIsValid(): boolean {
    return this.validLength.test(this.password.maximumLength) && /^\d+$/.test(this.password.maximumLength) &&
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
