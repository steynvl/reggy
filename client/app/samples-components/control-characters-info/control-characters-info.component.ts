import { Component, Input } from '@angular/core';
import { ControlCharacters } from '../../models/samples/control-characters';
import { ControlCharactersErr } from '../../models/samples/control-characters-err';

@Component({
  selector: 'app-control-characters-info',
  templateUrl: './control-characters-info.component.html',
  styleUrls: ['./control-characters-info.component.css']
})
export class ControlCharactersInfoComponent {

  @Input() controlCharacters: ControlCharacters;
  @Input() err: ControlCharactersErr;

}
