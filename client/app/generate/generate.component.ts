import { Component } from '@angular/core';

@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html'
})
export class GenerateComponent {

  textArea: string;

  constructor() { }

  fileChange(event) {
    const fileList: FileList = event.target.files;

    if (fileList.length === 1) {
      const reader = new FileReader();
      reader.readAsText(fileList[0]);

      reader.onload = (e) => {
        this.textArea = reader.result;
      };

    }

  }

}
