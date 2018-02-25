import { Component } from '@angular/core';
import { Marker } from '../shared/models/marker';

@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html',
  styleUrls: ['./generate.component.css']
})
export class GenerateComponent {

  textArea: string;
  selectedText = '';
  markedElements: Array<Marker> = [];

  constructor() {
  }

  fileChange(event) {
    const fileList: FileList = event.target.files;

    if (fileList.length === 1) {
      const reader = new FileReader();
      reader.readAsText(fileList[0]);

      reader.onload = () => {
        this.textArea = reader.result;
      };
    }

  }

  showSelectedText() {
    const txtArea = document.getElementById('text-area');

    const start = (txtArea as any).selectionStart;

    const finish = (txtArea as any).selectionEnd;

    this.selectedText = (txtArea as any).value.substring(start, finish);
  }

  mark() {
    if (this.selectedText !== '') {

      this.markedElements.push({
        id: this.markedElements.length + 1,
        color: 'red'
      });

      this.selectedText = '';
    }
  }

  setButtonColor(index) {
    const style = {
      'background-color': this.markedElements[index].color
    };
    return style;
  }



}
