import { Component, Input } from '@angular/core';
import { Numbers } from '../../models/samples/numbers';
import { NumbersErr } from '../../models/samples/numbers-err';

@Component({
  selector: 'app-numbers-info',
  templateUrl: './numbers-info.component.html',
  styleUrls: ['./numbers-info.component.scss']
})
export class NumbersInfoComponent {

  @Input() numbers: Numbers;
  @Input() err: NumbersErr;

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
