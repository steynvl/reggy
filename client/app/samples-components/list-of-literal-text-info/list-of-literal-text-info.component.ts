import { Component, Input } from '@angular/core';
import { ListOfLiteralText } from '../../models/samples/list-of-literal-text';
import { ListOfLiteralTextErr } from '../../models/samples/list-of-literal-text-err';

@Component({
  selector: 'app-list-of-literal-text-info',
  templateUrl: './list-of-literal-text-info.component.html',
  styleUrls: ['./list-of-literal-text-info.component.scss']
})
export class ListOfLiteralTextInfoComponent {

  @Input() listOfLiteralText: ListOfLiteralText;
  @Input() err: ListOfLiteralTextErr;

  inputFields = [0];

  addLiteralTextToList() {
    this.inputFields.push(this.inputFields[this.inputFields.length - 1] + 1);
    this.listOfLiteralText.literalText.push('');
  }
}
