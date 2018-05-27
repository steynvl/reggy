import { Component, Input } from '@angular/core';
import { UnicodeCharacters } from '../../models/samples/unicode-characters';
import { UnicodeCharactersErr } from '../../models/samples/unicode-characters-err';

@Component({
  selector: 'app-unicode-characters-info',
  templateUrl: './unicode-characters-info.component.html',
  styleUrls: ['./unicode-characters-info.component.css']
})
export class UnicodeCharactersInfoComponent {

  @Input() unicodeCharacters: UnicodeCharacters;
  @Input() err: UnicodeCharactersErr;

}
