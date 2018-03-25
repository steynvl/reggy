import { Component, Input, OnInit } from '@angular/core';
import { Username } from '../../models/common-use-case-models/username';

@Component({
  selector: 'app-username-info',
  templateUrl: './username-info.component.html',
  styleUrls: ['./username-info.component.css']
})
export class UsernameComponent implements OnInit {

  @Input() username: Username;

  shouldStartWithMsg = 'Should start with: ';
  shouldStartWithData = ['Letter', 'Uppercase letter', 'Lowercase letter', 'Letter or number'];

  shouldContainMsg = 'Should contain: ';
  shouldContainData = ['Uppercase letter', 'Lowercase letter', 'Number', 'Special character'];

  minimumLengthMsg = 'Minimum length (inclusive): ';
  minimumLengthData = ['1', '2', '3', '4', '5', 'Custom length'];
  minLengthIsCustom: boolean;

  maximumLengthMsg = 'Maximum length (inclusive): ';
  maximumLengthData = ['6', '7', '8', '9', '10', 'Custom length'];
  maxLengthIsCustom: boolean;

  validLength = /^[1-9]\d*$/;

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

    const newMsg = ['Should contain: ['];
    this.username.shouldContain.forEach((u, index) => {
      index === this.username.shouldContain.length - 1 ? newMsg.push(`${u}]`) : newMsg.push(`${u}, `);
    });
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
  }

  minRangeIsValid(): boolean {
    return this.validLength.test(this.username.minimumLength) &&
      Number.parseInt(this.username.minimumLength) <  Number.parseInt(this.username.maximumLength);
  }

  minRangeIsInvalid(): boolean {
    return !this.minRangeIsValid();
  }

  maxRangeIsValid(): boolean {
    return this.validLength.test(this.username.maximumLength) &&
      Number.parseInt(this.username.maximumLength) >  Number.parseInt(this.username.minimumLength);
  }

  maxRangeIsInvalid(): boolean {
    return !this.maxRangeIsValid();
  }

}
