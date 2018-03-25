import { Component, OnInit } from '@angular/core';
import { Marker } from '../../models/marker';
import { colours } from '../../colours/colours';
import { GenerateSamplesService } from '../../services/generate.samples.service';
import { MarkedText } from '../../models/marker-info/marked-text';
import { BasicCharacters } from '../../models/marker-info/basic-characters';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Digits } from '../../models/marker-info/digits';
import { SampleStringsInfo } from '../../models/sample-strings-info';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadSamples } from '../../models/payload/payload-samples';
import { ControlCharacters } from '../../models/marker-info/control-characters';
import { UnicodeCharacters } from '../../models/marker-info/unicode-characters';

declare var jQuery: any;

@Component({
  selector: 'app-generate-samples',
  templateUrl: './generate.samples.component.html',
  styleUrls: ['./generate.samples.component.css']
})
export class GenerateSamplesComponent implements OnInit {

  textArea = '';
  selectedText = '';
  markedElements: Array<Marker> = [];
  generatedRegex: string;
  selectedMarkerIdx = -1;
  markedText: MarkedText;
  basicCharacters: BasicCharacters;
  digits: Digits;
  controlCharacters: ControlCharacters;
  unicodeCharacters: UnicodeCharacters;

  userHighlightStart: string;
  userHighlightEnd: string;

  generalRegexInfo: GeneralRegexInfo;

  constructor(private generateService: GenerateSamplesService,
              public toast: ToastComponent) {
  }

  ngOnInit() {
    this.generalRegexInfo = {
      startRegexMatchAt: 'Anywhere',
      endRegexMatchAt  : 'Anywhere',
      regexTarget      : 'Java'
    };
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

    this.userHighlightStart = start;
    this.userHighlightEnd = finish;
  }

  private constructPayload(): PayloadSamples {
    const sampleStringsInfo: Array<SampleStringsInfo> = [];

    this.markedElements.forEach(markedElement => {

      sampleStringsInfo.push({
        markerType: markedElement.fieldType,
        markedStrings: markedElement.markedTextInfo.map(u => u.text),
        markerInfo: markedElement.markerInfo,
        repeatInfo: markedElement.repeatInfo
      });

    });

    return {
      sampleStringsInfo: sampleStringsInfo,
      generalRegexInfo : this.generalRegexInfo,
      generateMethod   : 'samplesAndSemantics'
    };
  }

  generateRegex() {
    this.generatedRegex = undefined;

    const payload = JSON.stringify(this.constructPayload());

    this.generateService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  private markerOverlap(start: number, end: number): boolean {
    const markerTextInfo = this.markedElements[this.selectedMarkerIdx].markedTextInfo;

    return markerTextInfo.some(m => (start >= m.start && start <= m.end)
      || (end >= m.start && end <= m.end));
  }

  mark(addInfoToMarker = false) {
    const s = Number.parseInt(this.userHighlightStart);
    const e = Number.parseInt(this.userHighlightEnd);

    if (addInfoToMarker) {

      if (this.markerOverlap(s, e)) {
        this.toast.setMessage('Selected area overlaps with selections for same marker!', 'warning');
      } else {
        this.markedElements[this.selectedMarkerIdx].markedTextInfo.push({
          start: s,
          end: e,
          text: this.selectedText
        });

        this.selectedText = '';
        this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
        this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
        this.digits = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Digits;
        this.controlCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ControlCharacters;
        this.unicodeCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as UnicodeCharacters;
      }

    } else {

      if (this.selectedText !== '') {

        this.markedElements.push({
            id: this.markedElements.length + 1,
            colour: colours[this.markedElements.length],
            fieldType: 'Marked text',
            markerInfo: {
              caseInsensitive:         false,
              matchAllExceptSpecified: false
            },
            markedTextInfo: [
              {
                start: s,
                end: e,
                text: this.selectedText
              }
            ],
            repeatInfo: {
              repeat: '1',
              start: undefined,
              end: undefined
            },
            repeatInfoView: ['Custom range', 'n or more times', '0 or 1', '0 or more',
              '1 or more', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
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

  setButtonColor(index: number): any {
    return {
      'background-color': this.markedElements[index].colour
    };
  }

  markerInfoChanged(idx) {
    this.clickMarkButton(idx, false);

    switch (this.markedElements[this.selectedMarkerIdx].fieldType) {

      case 'Marked text':
        this.markedText = {
          caseInsensitive:         false,
          matchAllExceptSpecified: false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.markedText;
        break;

      case 'Basic characters':
        this.basicCharacters = {
          caseInsensitive        : false,
          lowerCaseLetters       : false,
          upperCaseLetters       : false,
          digits                 : false,
          punctuationAndSymbols  : false,
          matchAllExceptSpecified: false,
          whiteSpace             : false,
          lineBreaks             : false,
          individualCharacters   : ''
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.basicCharacters;
        break;

      case 'Digits':
        this.digits = {
          zero:  true,
          one:   true,
          two:   true,
          three: true,
          four:  true,
          five:  true,
          six:   true,
          seven: true,
          eight: true,
          nine:  true,
          minus: {
            minus:    false,
            optional: false
          }
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.digits;
        break;

      case 'Control characters':
        this.controlCharacters = new ControlCharacters();
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.controlCharacters;
        break;

      case 'Unicode characters':
        this.unicodeCharacters = new UnicodeCharacters();
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.unicodeCharacters;
        break;

      default:
        break;
    }

  }

  clickMarkButton(idx: number, addInfoToMarker: boolean) {
    this.selectedMarkerIdx = idx;

    if (addInfoToMarker && this.selectedText !== '') {
      this.mark(true);
    }

    this.markedText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MarkedText;
    this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
    this.digits = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Digits;
    this.controlCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ControlCharacters;
    this.unicodeCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as UnicodeCharacters;
    this.highlightTextArea();
  }

  highlightTextArea() {
    const options = [];

    if (this.selectedMarkerIdx !== -1) {
      this.markedElements[this.selectedMarkerIdx].markedTextInfo.forEach(markerTextInfo => {
        options.push({
          color: this.markedElements[this.selectedMarkerIdx].colour,
          start: markerTextInfo.start,
          end: markerTextInfo.end
        });
      });
    }

    jQuery('textarea').highlightTextarea('destroy').highlightTextarea({
      ranges: options
    });
  }

  changeMarkerOrder(direction: string, idx: number) {
    const el = this.markedElements[idx];

    if (direction === 'up') {
      this.markedElements[idx] = this.markedElements[idx - 1];
      this.markedElements[idx - 1] = el;
      this.markedElements[idx].colour = colours[idx];
      this.markedElements[idx - 1].colour = colours[idx - 1];

      this.markedElements[idx - 1].id--;
      this.markedElements[idx].id++;
    } else {
      this.markedElements[idx] = this.markedElements[idx + 1];
      this.markedElements[idx + 1] = el;
      this.markedElements[idx].colour = colours[idx];
      this.markedElements[idx + 1].colour = colours[idx + 1];

      this.markedElements[idx + 1].id++;
      this.markedElements[idx].id--;
    }
  }

  removeMarker(idx: number) {
    this.markedElements.splice(idx, 1);

    for (let i = idx; i < this.markedElements.length; i++) {
      this.markedElements[i].id--;
      this.markedElements[i].colour = colours[i];
    }

    this.selectedMarkerIdx = idx === 0 ? -1 : idx - 1;
    this.highlightTextArea();
  }

  repeatInfoChanged(idx) {
    this.selectedMarkerIdx = idx;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
