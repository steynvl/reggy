import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { GuidInfoComponent } from "./guid-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-guid-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-guid-info>`
})
class HostComponent {
  @ViewChild(GuidInfoComponent)
  public componentUnderTest: GuidInfoComponent;
}

describe('Component: Common -> GUID', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [GuidInfoComponent, HostComponent],
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

  it('should create guid info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "GUID (Globally Unique Identifier)" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('GUID (Globally Unique Identifier)');
  });

  it('Should contain 6 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(6);
  });

  it('"Braces around the GUID" drop down should contain 3 options', () => {
    const el = fixture.debugElement.query(By.css('#braces-around')).nativeElement;
    expect(el.options.length).toEqual(3);
  });

  it('"Hyphens in the GUID" drop down should contain 3 options', () => {
    const el = fixture.debugElement.query(By.css('#hyphens-in')).nativeElement;
    expect(el.options.length).toEqual(3);
  });

  it('"Case" drop down should contain 3 options', () => {
    const el = fixture.debugElement.query(By.css('#case')).nativeElement;
    expect(el.options.length).toEqual(3);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
