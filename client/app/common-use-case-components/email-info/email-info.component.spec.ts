import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { EmailInfoComponent } from "./email-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-email-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-email-info>`
})
class HostComponent {
  @ViewChild(EmailInfoComponent)
  public componentUnderTest: EmailInfoComponent;
}

describe('Component: Common -> Email', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [EmailInfoComponent, HostComponent],
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

  it('should create email info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "Email" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('Email addresses');
  });

  it('Should contain 6 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(6);
  });

  it('"User name" drop down should contain 3 options', () => {
    const el = fixture.debugElement.query(By.css('#user-names')).nativeElement;
    expect(el.options.length).toEqual(3);
  });

  it('"Domain name" drop down should contain 4 options', () => {
    const el = fixture.debugElement.query(By.css('#domain-name')).nativeElement;
    expect(el.options.length).toEqual(4);
  });

  it('"Mailto:prefix" drop down should contain 3 options', () => {
    const el = fixture.debugElement.query(By.css('#mailto-prefix')).nativeElement;
    expect(el.options.length).toEqual(3);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
