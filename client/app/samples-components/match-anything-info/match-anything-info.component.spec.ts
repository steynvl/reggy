import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { MatchAnythingInfoComponent } from './match-anything-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-match-anything-info [matchAnything]="{
      matchAnythingExcept: '',
      specificCharacters : '',
      specificCharacter  : '',
      canSpanAcrossLines : true,
      caseInsensitive    : true,
      basicCharacters: {
        lowerCaseLetters       : true,
        upperCaseLetters       : true,
        digits                 : true,
        punctuationAndSymbols  : true,
        whiteSpace             : true,
        lineBreaks             : true
      }
    }" [err]="{ msg: '' }"></app-match-anything-info>`
})
class HostComponent {
  @ViewChild(MatchAnythingInfoComponent)
  public componentUnderTest: MatchAnythingInfoComponent;
}

describe('Component: Samples and Semantics -> Match anything', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [MatchAnythingInfoComponent, HostComponent],
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

  it('should create match anything info component', () => {
    expect(component).toBeTruthy();
  });

  it('should contain 2 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(2);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(2);
  });

  it('should contain select field with 4 options', () => {
    const el = fixture.debugElement.query(By.css('select')).nativeElement;
    expect(el).not.toBeNull();
    expect(el.options.length).toEqual(4);
  });

});
