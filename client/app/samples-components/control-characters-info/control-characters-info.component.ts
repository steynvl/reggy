import { Component, Input } from '@angular/core';
import { ControlCharacters } from '../../models/marker-info/control-characters';

@Component({
  selector: 'app-control-characters-info',
  templateUrl: './control-characters-info.component.html',
  styleUrls: ['./control-characters-info.component.css']
})
export class ControlCharactersInfoComponent {

  @Input() controlCharacters: ControlCharacters;

}
