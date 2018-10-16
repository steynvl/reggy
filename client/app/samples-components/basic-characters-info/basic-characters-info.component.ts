import { Component, Input } from '@angular/core';
import { BasicCharacters } from '../../models/samples/basic-characters';
import { BasicCharactersErr } from '../../models/samples/basic-characters-err';

@Component({
  selector: 'app-basic-characters-info',
  templateUrl: './basic-characters-info.component.html',
  styleUrls: ['./basic-characters-info.component.scss']
})
export class BasicCharacterInfoComponent {

  @Input() basicCharacters: BasicCharacters;
  @Input() err: BasicCharactersErr;

}
