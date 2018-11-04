import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { NumbersInfoComponent } from './numbers-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-numbers-info [numbers]="{
      minValOfIntPart              : 0,
      maxValOfIntPart              : 100,
      decimalSeparator             : '',
      minNrOfDecimals              : 1,
      maxNrOfDecimals              : 3,
      thousandSeparator            : '',
      codePosition                 : '',
      currencySign                 : '',
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
    }" [err]="{ msg: '' }"></app-numbers-info>`
})
class HostComponent {
  @ViewChild(NumbersInfoComponent)
  public componentUnderTest: NumbersInfoComponent;
}

describe('Component: Samples and Semantics -> Numbers', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [NumbersInfoComponent, HostComponent],
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

  it('should create numbers info component', () => {
    expect(component).toBeTruthy();
  });

  it('should contain 10 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(15);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(10);
  });

  it('should contain select 4 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(4);
  });

});
