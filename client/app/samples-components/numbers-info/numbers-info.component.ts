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
    const min = this.numbers.minNrOfDecimals;
    const max = this.numbers.maxNrOfDecimals;

    if (min === 0 && max === 0) {
      return true;
    } else {
      return min > 0 && max > 0 && min <= max;
    }
  }

  isValidIntegerParts(): boolean {
    const min = this.numbers.minValOfIntPart;
    const max = this.numbers.maxValOfIntPart;

    if (min === 0 && max === 0) {
      return true;
    } else {
      return min < max;
    }
  }

}
