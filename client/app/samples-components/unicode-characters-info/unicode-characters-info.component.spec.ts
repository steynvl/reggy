import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import {UnicodeCharactersInfoComponent} from './unicode-characters-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-unicode-characters-info [unicodeCharacters]="{
      lowercaseLetters           : false,
      uppercaseLetters           : false,
      titleCaseLetters           : false,
      casedLetters               : false,
      modifierLetters            : false,
      otherLetters               : false,
      nonSpacingMarks            : false,
      spacingCombiningMarks      : false,
      enclosingMarks             : false,
      spaceSeparators            : false,
      lineSeparators             : false,
      paragraphSeparators        : false,
      mathSymbols                : false,
      currencySymbols            : false,
      modifierSymbols            : false,
      otherSymbols               : false,
      decimalDigitNumbers        : false,
      letterNumbers              : false,
      otherNumbers               : false,
      dashPunctuation            : false,
      openPunctuation            : false,
      closePunctuation           : false,
      initialPunctuation         : false,
      finalPunctuation           : false,
      connectorPunctuation       : false,
      otherPunctuation           : false,
      controlCharacters          : false,
      formatCharacters           : false,
      privateUseCharacters       : false,
      surrogateCharacters        : false,
      unassignedCharacters       : false,
      matchAllExceptSelectedOnes : false,
      individualCharacters       : ''
    }" [err]="{ msg: '' }"></app-unicode-characters-info>`
})
class HostComponent {
  @ViewChild(UnicodeCharactersInfoComponent)
  public componentUnderTest: UnicodeCharactersInfoComponent;
}

describe('Component: Samples and Semantics -> Unicode characters', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [UnicodeCharactersInfoComponent, HostComponent],
      schemas: [NO_ERRORS_SCHEMA]
    }).compileComponents();

    TestBed.overrideComponent(
      HostComponent,
      { }
    ).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create unicode characters info component', () => {
    expect(component).toBeTruthy();
  });

  it('should contain one input field of type text', () => {
    const el = fixture.debugElement.query(By.css('input')).nativeElement;
    expect(el).not.toBeNull();
    expect(el.type === 'text').toEqual(true);
  });

  it('Should contain 32 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(33);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(32);
  });

});
