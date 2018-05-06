import { Component, Input } from '@angular/core';
import { Digits } from '../../models/marker-info/digits';

@Component({
  selector: 'app-digits-info',
  templateUrl: './digits-info.component.html',
  styleUrls: ['./digits-info.component.css']
})
export class DigitsInfoComponent {

  @Input() digits: Digits;

  ticked(type: string) {
    if (type === 'minus' && this.digits.minus.optional) {
      this.digits.minus.optional = false;
    } else if (type === 'optionalMinus' && this.digits.minus.minus) {
      this.digits.minus.minus = false;
    }
  }

}
