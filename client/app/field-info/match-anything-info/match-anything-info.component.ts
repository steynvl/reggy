import { Component, Input } from '@angular/core';
import { MatchAnything } from '../../models/marker-info/match-anything';

@Component({
  selector: 'app-match-anything-info',
  templateUrl: './match-anything-info.component.html',
  styleUrls: ['./match-anything-info.component.css']
})
export class MatchAnythingInfoComponent {

  @Input() matchAnything: MatchAnything;


  mmm() {
    console.log(this.matchAnything.matchAnythingExcept);
  }

}
