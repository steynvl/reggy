import { Component, OnInit } from '@angular/core';
import { Marker } from '../../models/marker';
import { colours } from '../../colours/colours';
import { GenerateSamplesService } from '../../services/generate.samples.service';
import { LiteralText } from '../../models/marker-info/literal-text';
import { BasicCharacters } from '../../models/marker-info/basic-characters';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Digits } from '../../models/marker-info/digits';
import { SampleStringsInfo } from '../../models/sample-strings-info';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadSamples } from '../../models/payload/payload-samples';
import { ControlCharacters } from '../../models/marker-info/control-characters';
import { UnicodeCharacters } from '../../models/marker-info/unicode-characters';
import { MatchAnything } from '../../models/marker-info/match-anything';
import { ListOfLiteralText } from '../../models/marker-info/list-of-literal-text';
import { Numbers } from '../../models/marker-info/numbers';

declare var jQuery: any;

@Component({
  selector: 'app-generate-samples',
  templateUrl: './generate.samples.component.html',
  styleUrls: ['./generate.samples.component.css']
})
export class GenerateSamplesComponent implements OnInit {

  isLoading = false;

  textArea = '';
  selectedText = '';
  markedElements: Array<Marker> = [];
  generatedRegex: string;
  selectedMarkerIdx = -1;
  literalText: LiteralText;
  basicCharacters: BasicCharacters;
  digits: Digits;
  controlCharacters: ControlCharacters;
  unicodeCharacters: UnicodeCharacters;
  matchAnything: MatchAnything;
  listOfLiteralText: ListOfLiteralText;
  numbers: Numbers;

  userHighlightStart: string;
  userHighlightEnd: string;

  generalRegexInfo: GeneralRegexInfo;

  markersIsCollapsed = false;
  markerTabIndex = 0;

  constructor(private generateService: GenerateSamplesService,
              public toast: ToastComponent) { }

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
    if (this.isValidUserInput()) {
      this.callService();
    } else {
      this.toast.setMessage('Invalid input information, please check all your marked components!', 'warning');
    }
  }

  private callService() {
    this.isLoading = true;

    this.generatedRegex = undefined;
    const payload = this.constructPayload();
    this.generateService.generateRegex(payload).subscribe(
      data => {
        const response = data;
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = response.regex.trim();
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        this.isLoading = false;
      }
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
        this.literalText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as LiteralText;
        this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
        this.digits = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Digits;
        this.controlCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ControlCharacters;
        this.unicodeCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as UnicodeCharacters;
        this.matchAnything = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MatchAnything;
        this.listOfLiteralText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ListOfLiteralText;
        this.numbers = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Numbers;
      }

    } else {

      if (this.selectedText !== '') {

        this.markedElements.push({
            id: this.markedElements.length + 1,
            colour: colours[this.markedElements.length],
            fieldType: 'Literal text',
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
        this.literalText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as LiteralText;

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

      case 'Literal text':
        this.literalText = {
          caseInsensitive:         false,
          matchAllExceptSpecified: false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.literalText;
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

      case 'Match anything':
        this.matchAnything = {
          matchAnythingExcept: 'Basic characters',
          specificCharacters : '',
          specificCharacter  : '',
          canSpanAcrossLines : false,
          basicCharacters: {
            lowerCaseLetters     : false,
            upperCaseLetters     : false,
            digits               : false,
            punctuationAndSymbols: false,
            whiteSpace           : false,
            lineBreaks           : false
          }
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.matchAnything;
        break;

      case 'List of literal text':
        this.listOfLiteralText = {
          literalText                 : [''],
          matchAnythingExceptSpecified: false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.listOfLiteralText;
        break;

      case 'Numbers':
        this.numbers = {
          minValOfIntPart              : '',
          maxValOfIntPart              : '',
          decimalSeparator             : '',
          minNrOfDecimals              : '',
          maxNrOfDecimals              : '',
          thousandSeparator            : '',
          codePosition                 : '',
          currencySign                 : '',
          currencyCodes                : '',
          limitIntegerPart             : false,
          allowPlusSign                : false,
          allowMinusSign               : false,
          allowParentheses             : false,
          signIsRequired               : false,
          whitespaceAllowedAfterSign   : false,
          thousandSeparatorsAreRequired: false,
          allowLeadingZeros            : false,
          requireIntegerPart           : false,
          allowExponent                : false,
          currencySignOrCodeRequired   : false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.numbers;
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

    this.literalText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as LiteralText;
    this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
    this.digits = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Digits;
    this.controlCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ControlCharacters;
    this.unicodeCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as UnicodeCharacters;
    this.matchAnything = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MatchAnything;
    this.listOfLiteralText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ListOfLiteralText;
    this.numbers = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Numbers;
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
    if (this.markedElements.length > 1) {
      this.markerTabIndex = this.selectedMarkerIdx;
    } else {
      if (this.markersIsCollapsed) {
        this.markersIsCollapsed = !this.markersIsCollapsed;
        this.markerTabIndex = -1;
      }
    }
    this.highlightTextArea();
  }

  repeatInfoChanged(idx) {
    this.selectedMarkerIdx = idx;
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

  validateStartRepeatInfo(): boolean {
    const repeatInfo = this.markedElements[this.selectedMarkerIdx].repeatInfo;
    return repeatInfo.start < repeatInfo.end && /^\d*$/.test(repeatInfo.start.toString());
  }

  validateEndRepeatInfo(): boolean {
    const repeatInfo = this.markedElements[this.selectedMarkerIdx].repeatInfo;
    return repeatInfo.end > repeatInfo.start && /^\d*$/.test(repeatInfo.end.toString());
  }

  validateMinNrOfTimes(): boolean {
    const repeatInfo = this.markedElements[this.selectedMarkerIdx].repeatInfo;
    return repeatInfo.start !== undefined && /^\d*$/.test(repeatInfo.start.toString());
  }

  tabClicked(idx: number) {
    this.markerTabIndex = idx;
    this.selectedMarkerIdx = idx;

    this.literalText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as LiteralText;
    this.basicCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as BasicCharacters;
    this.digits = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Digits;
    this.controlCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ControlCharacters;
    this.unicodeCharacters = (this.markedElements[this.selectedMarkerIdx].markerInfo) as UnicodeCharacters;
    this.matchAnything = (this.markedElements[this.selectedMarkerIdx].markerInfo) as MatchAnything;
    this.listOfLiteralText = (this.markedElements[this.selectedMarkerIdx].markerInfo) as ListOfLiteralText;
    this.numbers = (this.markedElements[this.selectedMarkerIdx].markerInfo) as Numbers;
    this.highlightTextArea();
  }

  collapseMarkers() {
    this.markersIsCollapsed = !this.markersIsCollapsed;
    this.markerTabIndex = this.selectedMarkerIdx;
  }

  isValidUserInput(): boolean {

    for (const marker of this.markedElements) {

      switch (marker.fieldType) {

        case 'Basic characters':
          if (!this.isValidBasicCharactersInfo(marker.markerInfo as BasicCharacters)) {
            return false;
          }
          break;
        case 'Control characters':
          if (!this.isValidControlCharactersInfo(marker.markerInfo as ControlCharacters)) {
            return false;
          }
          break;
        case 'Digits':
          if (!this.isValidDigitsInfo(marker.markerInfo as Digits)) {
            return false;
          }
          break;
        case 'List of literal text':
          if (!this.isValidListOfLiteralTextInfo(marker.markerInfo as ListOfLiteralText)) {
            return false;
          }
          break;
        case 'Match anything':
          if (!this.isValidMatchAnythingInfo(marker.markerInfo as MatchAnything)) {
            return false;
          }
          break;
        case 'Numbers':
          if (!this.isValidNumbersInfo(marker.markerInfo as Numbers)) {
            return false;
          }
          break;
        case 'Unicode characters':
          if (!this.isValidUnicodeCharactersInfo(marker.markerInfo as UnicodeCharacters)) {
            return false;
          }
          break;
        default:
          break;

      }

    }

    return true;
  }

  isValidBasicCharactersInfo(info: BasicCharacters): boolean {
    if (info.individualCharacters !== undefined && info.individualCharacters.trim() !== '') {
      return true;
    }

    if (info.matchAllExceptSpecified) {
      return info.individualCharacters.trim() !== '';
    }

    return !(!info.digits && !info.whiteSpace && !info.lowerCaseLetters
      && !info.punctuationAndSymbols && !info.lineBreaks
      && !info.upperCaseLetters);
  }

  isValidControlCharactersInfo(info: ControlCharacters): boolean {
    return Object.keys(info).filter(cc => cc !== 'matchAllExceptSelectedOnes')
                            .some(cc => info[cc]);
  }

  isValidDigitsInfo(info: Digits): boolean {
    const props = [];
    Object.values(info).forEach(prop => {
      if (typeof prop === 'object') {
        props.push(prop.minus);
        props.push(prop.optional);
      } else {
        props.push(prop);
      }
    });

    return props.some(d => d);
  }

  isValidListOfLiteralTextInfo(info: ListOfLiteralText): boolean {
    return info.literalText.every(llt => llt !== undefined && llt !== '');
  }

  isValidMatchAnythingInfo(info: MatchAnything): boolean {

    switch (info.matchAnythingExcept) {

      case 'Basic characters':
        const bc = info.basicCharacters;
        return !(!bc.lowerCaseLetters && !bc.digits && !bc.whiteSpace
                  && !bc.upperCaseLetters && !bc.punctuationAndSymbols
                  && !bc.lineBreaks);
      case 'Specific characters':
        return info.specificCharacters !== undefined && info.specificCharacters !== '';
      case 'Specific character':
        return info.specificCharacter !== undefined && /^.$/.test(info.specificCharacter);
      default:
        break;

    }

    return true;
  }

  isValidNumbersInfo(info: Numbers): boolean {
    return true;
  }

  isValidUnicodeCharactersInfo(info: UnicodeCharacters): boolean {
    const unicode = /^U\+[A-Z\d]{2,5}(?:-U\+[A-Z\d]{2,5})?(?: U\+[A-Z\d]{2,5}(?:-U\+[A-Z\d]{2,5})?)*$/;

    const validInput = info.individualCharacters === '' || unicode.test(info.individualCharacters);

    return validInput || Object.keys(info)
          .filter(cc => cc !== 'matchAllExceptSelectedOnes' && cc !== 'individualCharacters')
          .some(cc => info[cc]);
  }

}
