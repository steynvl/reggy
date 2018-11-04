import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { By } from '@angular/platform-browser';
import { ListOfLiteralTextInfoComponent } from './list-of-literal-text-info.component';

@Component({
  selector: 'app-host-component',
  template: `<app-list-of-literal-text-info [listOfLiteralText]="{
        literalText: [''],
        matchAnythingExceptSpecified: true,
        caseInsensitive: true
    }" [err]="{ msg: '' }"></app-list-of-literal-text-info>`
})
class HostComponent {
  @ViewChild(ListOfLiteralTextInfoComponent)
  public componentUnderTest: ListOfLiteralTextInfoComponent;
}

describe('Component: Samples and Semantics -> List of literal text', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ListOfLiteralTextInfoComponent, HostComponent],
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

  it('should create list of literal text info component', () => {
    expect(component).toBeTruthy();
  });

  it('Should contain 2 checkboxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));

    const checkboxes = el.filter(e => e.nativeElement.type === 'checkbox');
    expect(checkboxes.length).toEqual(2);
  });

  it('Should contain 1 button', () => {
    const el = fixture.debugElement.query(By.css('button')).nativeElement;
    expect(el).not.toBeNull();
  });

  it('Should contain 1 input field', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));

    const inputFields = el.filter(e => e.nativeElement.type === 'text');
    expect(inputFields.length).toEqual(1);
  });

});
