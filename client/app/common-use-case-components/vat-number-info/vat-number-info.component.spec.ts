import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { VatNumberInfoComponent } from "./vat-number-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-vat-number-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-vat-number-info>`
})
class HostComponent {
  @ViewChild(VatNumberInfoComponent)
  public componentUnderTest: VatNumberInfoComponent;
}

describe('Component: Common -> VAT numbers', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [VatNumberInfoComponent, HostComponent],
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

  it('should create vat numbers info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "VAT numbers" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('VAT numbers');
  });

  it('Should contain 29 check boxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));

    expect(el.length).toEqual(29);
    expect(el.filter(e => e.nativeElement.type === 'checkbox').length).toEqual(29);
  });

  it('Should contain 5 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(5);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
