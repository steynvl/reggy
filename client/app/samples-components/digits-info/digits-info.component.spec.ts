import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { DigitsInfoComponent } from './digits-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-digits-info [digits]="{
        zero: true,
        one: true,
        two: true,
        three: true,
        four: true,
        five: true,
        six: true,
        seven: true,
        eight: true,
        nine: true,
        minus: {
          minus: true,
          optional: true
        }
    }" [err]="{ msg: '' }"></app-digits-info>`
})
class HostComponent {
  @ViewChild(DigitsInfoComponent)
  public componentUnderTest: DigitsInfoComponent;
}

describe('Component: Samples and Semantics -> Digits', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [DigitsInfoComponent, HostComponent],
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

  it('should create digits info component', () => {
    expect(component).toBeTruthy();
  });

  it('Should contain 12 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(12);

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(12);
  });

});
