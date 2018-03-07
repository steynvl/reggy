import { Component, Input } from '@angular/core';
import { MarkedText } from '../../shared/models/marker-info/marked-text';
import { MarkedTextInfo } from '../../shared/models/marked-text-info';

@Component({
  selector: 'app-marked-text-info',
  templateUrl: './marked-text-info.component.html',
  styleUrls: ['./marked-text-info.component.css']
})
export class MarkedTextInfoComponent {

  @Input() markedText: MarkedText;
  @Input() possibleMatches: Array<MarkedTextInfo>;

}
