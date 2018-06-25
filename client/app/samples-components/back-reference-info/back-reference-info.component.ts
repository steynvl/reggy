import { Component, Input } from '@angular/core';
import { BackReference } from '../../models/samples/back-reference';
import { Marker } from '../../models/marker';

@Component({
  selector: 'app-backreference-info',
  templateUrl: './backreference-info.component.html',
  styleUrls: ['./backreference-info.component.css']
})
export class BackreferenceInfoComponent {

  @Input() backreference: BackReference;
  @Input() options: Array<Marker>;

  setButtonColour(): any {
    return {
      'background-color': this.backreference.marker.colour
    };
  }

}
