import { Component } from '@angular/core';
import { Marker } from '../shared/models/marker';
import { colours } from '../shared/colours/colours';
import { GenerateService } from '../services/generate.service';
import { MarkedText } from '../shared/models/marker-info/marked-text';
import { BasicCharacters } from '../shared/models/marker-info/basic-characters';
import { ToastComponent } from '../shared/toast/toast.component';

declare var jQuery: any;

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

  constructor(private generateService: GenerateService,
              public toast: ToastComponent) {
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

  mark(addInfoToMarker = false) {
    const s = this.textArea.indexOf(this.selectedText);
    const e = s + this.selectedText.length;

    if (addInfoToMarker && this.selectedText !== '') {
      this.markedElements[this.selectedMarkerIdx].markedTextInfo.push({
        start: s,
        end: e,
        text: this.selectedText
      });

      this.selectedText = '';
      this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
      this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;

    } else {

      if (this.selectedText !== '') {

        this.markedElements.push({
            id: this.markedElements.length + 1,
            colour: colours[this.markedElements.length],
            fieldType: 'Marked text',
            markerInfo: {
              caseInsensitive: false,
              matchAllExceptSpecified: false
            },
            markedTextInfo: [
              {
                start: s,
                end: e,
                text: this.selectedText
              }
            ]
          }
        );

        this.selectedText = '';
        this.selectedMarkerIdx = this.markedElements.length - 1;
        this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;

        this.highlightTextArea();
      } else {
        this.toast.setMessage('No text selected!', 'warning');
      }

    }
  }

  setButtonColor(index: number) {
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


  clickMarkButton(idx: number, addInfoToMarker: boolean) {
    this.selectedMarkerIdx = idx;

    if (addInfoToMarker) {
      this.mark(true);
    }

    this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
    this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
    this.highlightTextArea();
  }

  highlightTextArea() {
    const options = [];
    this.markedElements[this.selectedMarkerIdx].markedTextInfo.forEach(markerTextInfo => {
      options.push({
        color: this.markedElements[this.selectedMarkerIdx].colour,
        start: markerTextInfo.start,
        end: markerTextInfo.end
      });
    });

    jQuery('textarea').highlightTextarea('destroy').highlightTextarea({
      ranges: options
    });
  }

  changeMarkerOrder(direction: string, idx: number) {
    const el = this.markedElements[idx];

    if (direction === 'up') {
      this.markedElements[idx] = this.markedElements[idx - 1];
      this.markedElements[idx - 1] = el;
    } else {
      this.markedElements[idx] = this.markedElements[idx + 1];
      this.markedElements[idx + 1] = el;
    }
  }

  printStuff() { }

}
