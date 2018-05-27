import { Component, OnInit } from '@angular/core';
import { Marker } from '../../models/marker';
import { colours } from '../../colours/colours';
import { GenerateSamplesService } from '../../services/generate.samples.service';
import { LiteralText } from '../../models/samples/literal-text';
import { BasicCharacters } from '../../models/samples/basic-characters';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Digits } from '../../models/samples/digits';
import { SampleStringsInfo } from '../../models/sample-strings-info';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadSamples } from '../../models/payload/payload-samples';
import { ControlCharacters } from '../../models/samples/control-characters';
import { UnicodeCharacters } from '../../models/samples/unicode-characters';
import { MatchAnything } from '../../models/samples/match-anything';
import { ListOfLiteralText } from '../../models/samples/list-of-literal-text';
import { Numbers } from '../../models/samples/numbers';
import { GeneratedRegex } from '../../models/generated-regex';
import { Title } from '@angular/platform-browser';
import { VerificationService } from '../../services/verification.service';
import { BasicCharactersErr } from '../../models/samples/basic-characters-err';
import { ControlCharactersErr } from '../../models/samples/control-characters-err';
import { DigitsErr } from '../../models/samples/digits-err';
import { ListOfLiteralTextErr } from '../../models/samples/list-of-literal-text-err';
import { MatchAnythingErr } from '../../models/samples/match-anything-err';
import { UnicodeCharactersErr } from '../../models/samples/unicode-characters-err';
import { NumbersErr } from '../../models/samples/numbers-err';

declare var jQuery: any;

@Component({
  selector: 'app-generate-samples',
  templateUrl: './generate.samples.component.html',
  styleUrls: ['./generate.samples.component.css']
})
export class GenerateSamplesComponent implements OnInit {

  isLoading = false;

  generatedRegex: GeneratedRegex;

  textArea = '';
  selectedText = '';
  markedElements: Array<Marker> = [];
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
              public toast: ToastComponent,
              private titleService: Title,
              private verificationService: VerificationService) { }

  ngOnInit() {
    this.titleService.setTitle('Samples and Semantics | Reggy');

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
        this.markedElements = [];
        jQuery('textarea').highlightTextarea('destroy');
        this.textArea = reader.result;
      };
    }

  }

  reset() {
    this.markedElements = [];
    jQuery('textarea').highlightTextarea('destroy');
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
          this.generatedRegex = {
            regex        : response.regex,
            compiledRegex: response.compiledRegex
          };
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
            error: {
              msg: undefined
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
        this.markedElements[this.selectedMarkerIdx].error = { msg: undefined };
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
        this.markedElements[this.selectedMarkerIdx].error = { msg: undefined };
        break;

      case 'Control characters':
        this.controlCharacters = new ControlCharacters();
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.controlCharacters;
        this.markedElements[this.selectedMarkerIdx].error = { msg: undefined };
        break;

      case 'Unicode characters':
        this.unicodeCharacters = new UnicodeCharacters();
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.unicodeCharacters;
        this.markedElements[this.selectedMarkerIdx].error = { msg: undefined };
        break;

      case 'Match anything':
        this.matchAnything = {
          matchAnythingExcept: 'Basic characters',
          specificCharacters : '',
          specificCharacter  : '',
          canSpanAcrossLines : false,
          caseInsensitive    : false,
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
        this.markedElements[this.selectedMarkerIdx].error = {
          basicCharactersMsg: undefined,
          specCharactersMsg : undefined,
          specCharacterMsg  : undefined
        };
        break;

      case 'List of literal text':
        this.listOfLiteralText = {
          literalText                 : [''],
          matchAnythingExceptSpecified: false,
          caseInsensitive             : false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.listOfLiteralText;
        this.markedElements[this.selectedMarkerIdx].error = { msg: undefined };
        break;

      case 'Numbers':
        this.numbers = {
          minValOfIntPart              : 0,
          maxValOfIntPart              : 0,
          decimalSeparator             : 'Any',
          minNrOfDecimals              : 0,
          maxNrOfDecimals              : 0,
          thousandSeparator            : 'None',
          codePosition                 : 'Before only',
          currencySign                 : 'None',
          currencyCodes                : '',
          limitIntegerPart             : false,
          allowPlusSign                : false,
          allowMinusSign               : false,
          signIsRequired               : false,
          whitespaceAllowedAfterSign   : false,
          thousandSeparatorsAreRequired: false,
          allowLeadingZeros            : false,
          requireIntegerPart           : false,
          allowExponent                : false,
          currencySignOrCodeRequired   : false
        };
        this.markedElements[this.selectedMarkerIdx].markerInfo = this.numbers;
        this.markedElements[this.selectedMarkerIdx].error = {
          integerPart       : undefined,
          decimalPart       : undefined,
          currencyCodes     : undefined,
          thousandSeparator : undefined,
          currencySignOrCode: undefined
        };
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

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

  validateStartRepeatInfo(idx: number): boolean {
    const repeatInfo = this.markedElements[idx].repeatInfo;
    return repeatInfo.start < repeatInfo.end && /^\d*$/.test(repeatInfo.start.toString());
  }

  validateEndRepeatInfo(idx: number): boolean {
    const repeatInfo = this.markedElements[idx].repeatInfo;
    return repeatInfo.end > repeatInfo.start && /^\d*$/.test(repeatInfo.end.toString());
  }

  validateMinNrOfTimes(idx: number): boolean {
    const repeatInfo = this.markedElements[idx].repeatInfo;
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
    let isValid = true;

    for (const marker of this.markedElements) {

      if (!this.verificationService.isValidRepeatInfo(marker.repeatInfo)) {
        isValid = false;
      }

      switch (marker.fieldType) {

        case 'Basic characters':
          if (!this.verificationService.isValidBasicCharactersInfo(marker.markerInfo as BasicCharacters)) {
            isValid = false;
            (marker.error as BasicCharactersErr).msg = 'Please select an option(s) above or add characters to the input field!';
          } else {
            (marker.error as BasicCharactersErr).msg = undefined;
          }
          break;
        case 'Control characters':
          if (!this.verificationService.isValidControlCharactersInfo(marker.markerInfo as ControlCharacters)) {
            isValid = false;
            (marker.error as ControlCharactersErr).msg = 'Please select one or more of the options above!';
          } else {
            (marker.error as ControlCharactersErr).msg = undefined;
          }
          break;
        case 'Digits':
          if (!this.verificationService.isValidDigitsInfo(marker.markerInfo as Digits)) {
            isValid = false;
            (marker.error as DigitsErr).msg = 'Please select at least one digit!';
          } else {
            (marker.error as DigitsErr).msg = undefined;
          }
          break;
        case 'List of literal text':
          if (!this.verificationService.isValidListOfLiteralTextInfo(marker.markerInfo as ListOfLiteralText)) {
            isValid = false;
            (marker.error as ListOfLiteralTextErr).msg = 'Please specify the literal text to match in the input field below!';
          } else {
            (marker.error as ListOfLiteralTextErr).msg = undefined;
          }
          break;
        case 'Match anything':
          (marker.error as MatchAnythingErr) = {
            basicCharactersMsg: undefined,
            specCharactersMsg : undefined,
            specCharacterMsg  : undefined
          };
          if (!this.verificationService.isValidMatchAnythingInfo(marker.markerInfo as MatchAnything, (marker.error as MatchAnythingErr))) {
            isValid = false;
          } else {
            (marker.error as MatchAnythingErr) = undefined;
          }
          break;
        case 'Numbers':
          (marker.error as NumbersErr) = {
            integerPart       : undefined,
            decimalPart       : undefined,
            currencyCodes     : undefined,
            thousandSeparator : undefined,
            currencySignOrCode: undefined
          };
          if (!this.verificationService.isValidNumbersInfo(marker.markerInfo as Numbers, (marker.error as NumbersErr))) {
            isValid = false;
          } else {
            (marker.error as NumbersErr) = undefined;
          }
          break;
        case 'Unicode characters':
          if (!this.verificationService.isValidUnicodeCharactersInfo(marker.markerInfo as UnicodeCharacters)) {
            isValid = false;
            (marker.error as UnicodeCharactersErr).msg = 'Please select one or more of the options above!';
          } else {
            (marker.error as UnicodeCharactersErr).msg = undefined;
          }
          break;
        default:
          break;

      }

    }

    return isValid;
  }

}
