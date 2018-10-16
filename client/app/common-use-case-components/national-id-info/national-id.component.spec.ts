import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { NationalIdInfoComponent } from "./national-id-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-national-id-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-national-id-info>`
})
class HostComponent {
  @ViewChild(NationalIdInfoComponent)
  public componentUnderTest: NationalIdInfoComponent;
}

describe('Component: Common -> National ID', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [NationalIdInfoComponent, HostComponent],
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

  it('should create national id info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "National ID" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('National ID');
  });

  it('Should contain 4 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(4);
  });

  it('Should contain 18 national id options', () => {
    const el = fixture.debugElement.query(By.css('#kind-of-id'));
    expect(el.nativeElement.options.length).toEqual(18);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
