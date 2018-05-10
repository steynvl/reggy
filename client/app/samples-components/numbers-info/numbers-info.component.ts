import { Component, Input } from '@angular/core';
import { Numbers } from '../../models/marker-info/numbers';

@Component({
  selector: 'app-numbers-info',
  templateUrl: './numbers-info.component.html',
  styleUrls: ['./numbers-info.component.css']
})
export class NumbersInfoComponent {

  @Input() numbers: Numbers;

  isValidNrOfDecimals(): boolean {
    const validInput = /^[1-9]+$/;
    const min = this.numbers.minNrOfDecimals;
    const max = this.numbers.maxNrOfDecimals;

    if (min === '' && max === '') {
      return true;
    } else {
      return validInput.test(min) && validInput.test(max)
        && Number.parseInt(min) <= Number.parseInt(max);
    }
  }

  isValidIntegerParts(): boolean {
    const validInput = /^-?\d+$/;
    const min = this.numbers.minValOfIntPart;
    const max = this.numbers.maxValOfIntPart;

    if (min === '' && max === '') {
      return true;
    } else {
      return validInput.test(min) && validInput.test(max)
        && Number.parseInt(min) <= Number.parseInt(max);
    }
  }

}
