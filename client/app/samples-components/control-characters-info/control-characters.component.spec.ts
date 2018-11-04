import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { ControlCharactersInfoComponent } from './control-characters-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-control-characters-info [controlCharacters]="{
              nul                        : false,
              startOfHeading             : false,
              startOfText                : false,
              endOfText                  : false,
              endOfTransmission          : false,
              enquiry                    : false,
              acknowledge                : false,
              bell                       : false,
              backspace                  : false,
              horizontalTab              : false,
              newLine                    : false,
              verticalTab                : false,
              formFeed                   : false,
              carriageReturn             : false,
              shiftOut                   : false,
              shiftIn                    : false,
              dataLinkEscape             : false,
              deviceControlOne           : false,
              deviceControlTwo           : false,
              deviceControlThree         : false,
              deviceControlFour          : false,
              negativeAcknowledge        : false,
              synchronousIdle            : false,
              endOfTransBlock            : false,
              cancel                     : false,
              endOfMedium                : false,
              substitute                 : false,
              escape                     : false,
              fileSeparator              : false,
              groupSeparator             : false,
              recordSeparator            : false,
              unitSeparator              : false,
              matchAllExceptSelectedOnes : false}" [err]="{ msg: '' }"></app-control-characters-info>`
})
class HostComponent {
  @ViewChild(ControlCharactersInfoComponent)
  public componentUnderTest: ControlCharactersInfoComponent;
}

describe('Component: Samples and Semantics -> Control characters', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ControlCharactersInfoComponent, HostComponent],
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

  it('should create control characters info component', () => {
    expect(component).toBeTruthy();
  });

  it('Should contain 33 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(33);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(33);
  });

});
