import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { DateAndTimeInfoComponent } from "./date-and-time-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-date-and-time-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-date-and-time-info>`
})
class HostComponent {
  @ViewChild(DateAndTimeInfoComponent)
  public componentUnderTest: DateAndTimeInfoComponent;
}

describe('Component: Common -> Date and Time', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [DateAndTimeInfoComponent, HostComponent],
      schemas: [NO_ERRORS_SCHEMA]
    }).compileComponents();

    TestBed.overrideComponent(
      HostComponent,
      {
        set: {
          providers: [
            { provide: GenerateService, useClass: MockClass},
            { provide: ToastComponent, useClass: MockClass}
          ]
        }
      }
    ).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create date and time info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "Date and time" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('Date and time');
  });

  it('Should contain 7 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(7);
  });

  it('Should contain text area for specifying time and date formats', () => {
    const el = fixture.debugElement.query(By.css('textarea')).nativeElement;
    expect(el.placeholder).toEqual("Specify date and format(s)...");
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
