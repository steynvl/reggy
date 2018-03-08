import { Component, Input } from '@angular/core';
import { Numbers } from '../../models/marker-info/numbers';

@Component({
  selector: 'app-numbers-info',
  templateUrl: './numbers-info.component.html',
  styleUrls: ['./numbers-info.component.css']
})
export class NumbersInfoComponent {

  @Input() numbers: Numbers;

  ticked(type: string) {
    if (type === 'minus' && this.numbers.minus.optional) {
      this.numbers.minus.optional = false;
    } else if (type === 'optionalMinus' && this.numbers.minus.minus) {
      this.numbers.minus.minus = false;
    }
  }

}
