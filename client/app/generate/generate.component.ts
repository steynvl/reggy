import { Component } from '@angular/core';
import { Marker } from '../shared/models/marker';
import { colours } from '../shared/colours/colours';
import { GenerateService } from '../services/generate.service';

@Component({
  selector: 'app-generate',
  templateUrl: './generate.component.html',
  styleUrls: ['./generate.component.css']
})
export class GenerateComponent {

  textArea = '';
  selectedText = '';
  markedElements: Array<Marker> = [];
  generatedRegex: string;

  constructor(private generateService: GenerateService) {
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

  buildSampleStrings(): Array<string> {
    return this.textArea.split(/\s+/g)
      .filter(word => word.trim().length > 0);
  }

  generateRegex() {
    const sampleStrings = this.buildSampleStrings();
    this.generatedRegex = undefined;

    this.generateService.generateRegex(sampleStrings).subscribe(
      data => this.generatedRegex = data,
      error => console.log(error)
    );
  }

  mark() {
    if (this.selectedText !== '') {

      this.markedElements.push({
        id: this.markedElements.length + 1,
        colour: colours[this.markedElements.length]
      });

      this.selectedText = '';
    }
  }

  setButtonColor(index) {
    const style = {
      'background-color': this.markedElements[index].colour
    };
    return style;
  }



}
