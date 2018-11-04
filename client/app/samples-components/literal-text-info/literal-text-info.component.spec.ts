import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { LiteralTextInfoComponent } from './literal-text-info.component';
import { MarkedTextToView } from '../../pipes/marked-text-to-view';

@Component({
  selector: 'app-host-component',
  template: `<app-literal-text-info [literalText]="{
          caseInsensitive: true,
          matchAllExceptSpecified: true
    }" [possibleMatches]="[{ start: 0, end: 0, text: '' }]"></app-literal-text-info>`
})
class HostComponent {
  @ViewChild(LiteralTextInfoComponent)
  public componentUnderTest: LiteralTextInfoComponent;
}

describe('Component: Samples and Semantics -> Literal text', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [LiteralTextInfoComponent, HostComponent, MarkedTextToView],
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

  it('should create literal text info component', () => {
    expect(component).toBeTruthy();
  });

  it('Should contain 2 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(2);
  });

  it('Should contain p tag that contains the text "Possible matches:"', () => {
    const el = fixture.debugElement.query(By.css('p')).nativeElement;
    expect(el.textContent).toContain('Possible matches:');
  });

});
