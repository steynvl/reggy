import { Component, Input } from '@angular/core';
import { LiteralText } from '../../models/samples/literal-text';
import { MarkedTextInfo } from '../../models/marked-text-info';

@Component({
  selector: 'app-literal-text-info',
  templateUrl: './literal-text-info.component.html',
  styleUrls: ['./literal-text-info.component.scss']
})
export class LiteralTextInfoComponent {

  @Input() literalText: LiteralText;
  @Input() possibleMatches: Array<MarkedTextInfo>;

}
