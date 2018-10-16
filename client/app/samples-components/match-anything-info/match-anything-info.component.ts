import { Component, Input } from '@angular/core';
import { MatchAnything } from '../../models/samples/match-anything';
import { MatchAnythingErr } from '../../models/samples/match-anything-err';

@Component({
  selector: 'app-match-anything-info',
  templateUrl: './match-anything-info.component.html',
  styleUrls: ['./match-anything-info.component.scss']
})
export class MatchAnythingInfoComponent {

  @Input() matchAnything: MatchAnything;
  @Input() err: MatchAnythingErr;

}
