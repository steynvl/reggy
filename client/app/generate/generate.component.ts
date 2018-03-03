import { Component, ViewEncapsulation } from '@angular/core';
import { Marker } from '../shared/models/marker';
import { colours } from '../shared/colours/colours';
import { GenerateService } from '../services/generate.service';
import { MarkedText } from '../shared/models/marker-info/marked-text';
import { BasicCharacters } from '../shared/models/marker-info/basic-characters';

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
  selectedMarkerIdx = -1;
  markedText: MarkedText;
  basicCharacters: BasicCharacters;

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
          colour: colours[this.markedElements.length],
          fieldType: 'Marked text',
          markerInfo: {
            caseInsensitive: false,
            matchAllExceptSpecified: false
          }
        }
      );

      this.selectedText = '';
      this.selectedMarkerIdx = this.markedElements.length - 1;
      this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
    }
  }

  setButtonColor(index) {
    const style = {
      'background-color': this.markedElements[index].colour
    };
    return style;
  }


  markerInfoChanged() {

    switch (this.markedElements[this.selectedMarkerIdx].fieldType) {

      case 'Marked text':
        this.markedText = {
          caseInsensitive: false,
          matchAllExceptSpecified: false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.markedText;
        break;

      case 'Basic characters':
        this.basicCharacters = {
          lowerCaseLetters: false,
          upperCaseLetters: false,
          containsDigits: false,
          matchAllExceptSpecified: false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.basicCharacters;
        break;

      case 'Numbers':
        this.markedElements[this.selectedMarkerIdx].markerInfo = {};
        break;

      default:
        break;
    }

  }

  repeatInfoChanged() {

  }

  clickMarkButton(idx) {
    this.selectedMarkerIdx = idx;
    this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
  }


  printStuff() {
    console.log(this.markedText.caseInsensitive);
    console.log(this.markedText.matchAllExceptSpecified);
  }

}
