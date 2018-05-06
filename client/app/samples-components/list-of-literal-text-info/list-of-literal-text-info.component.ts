import { Component, Input } from '@angular/core';
import { ListOfLiteralText } from '../../models/marker-info/list-of-literal-text';

@Component({
  selector: 'app-list-of-literal-text-info',
  templateUrl: './list-of-literal-text-info.component.html',
  styleUrls: ['./list-of-literal-text-info.component.css']
})
export class ListOfLiteralTextInfoComponent {

  @Input() listOfLiteralText: ListOfLiteralText;
  inputFields = [0];

  addLiteralTextToList() {
    this.inputFields.push(this.inputFields[this.inputFields.length - 1] + 1);
    this.listOfLiteralText.literalText.push('');
  }
}
