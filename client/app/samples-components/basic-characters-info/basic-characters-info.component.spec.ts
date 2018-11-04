import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { BasicCharacterInfoComponent } from './basic-characters-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-basic-characters-info [basicCharacters]="{
                caseInsensitive        : true,
                lowerCaseLetters       : true,
                upperCaseLetters       : true,
                digits                 : true,
                punctuationAndSymbols  : true,
                matchAllExceptSpecified: true,
                whiteSpace             : true,
                lineBreaks             : true,
                individualCharacters   : ''
            }" [err]="{ msg: '' }"
  ></app-basic-characters-info>`
})
class HostComponent {
  @ViewChild(BasicCharacterInfoComponent)
  public componentUnderTest: BasicCharacterInfoComponent;
}

describe('Component: Samples and Semantics -> Basic characters', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [BasicCharacterInfoComponent, HostComponent],
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

  it('should create basic characters info component', () => {
    expect(component).toBeTruthy();
  });


  it('Should contain 8 checkboxes and 1 input field', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(9);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(8);

    const inputFields = el.filter(e => e.nativeElement.type === 'text');
    expect(inputFields.length).toEqual(1);
    expect(inputFields[0].nativeElement.placeholder).toEqual('Add characters that should also be matched...');
  });

});
