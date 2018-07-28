import { Component, Input, OnInit } from '@angular/core';
import { BackReference } from '../../models/samples/back-reference';
import { Marker } from '../../models/marker';

@Component({
  selector: 'app-back-reference-info',
  templateUrl: './back-reference-info.component.html',
  styleUrls: ['./back-reference-info.component.css']
})
export class BackReferenceInfoComponent implements OnInit {

  @Input() backReference: BackReference;
  @Input() options: Array<Marker>;

  ngOnInit() {
    this.backReference.marker = this.options[0];
  }

  setButtonColour(): any {
    return {
      'background-color': this.backReference.marker.colour
    };
  }

}
