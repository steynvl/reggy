import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { CreditCardInfoComponent } from './credit-card-info.component';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-credit-card-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-credit-card-info>`
})
class HostComponent {
  @ViewChild(CreditCardInfoComponent)
  public componentUnderTest: CreditCardInfoComponent;
}

describe('Component: Common -> Credit Card', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [CreditCardInfoComponent, HostComponent],
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

  it('should create credit card info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "Credit card numbers" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('Credit card numbers');
  });

  it('Should contain 6 checkboxes and 3 radio buttons', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));

    expect(el.length).toEqual(9);

    expect(el.filter(e => e.nativeElement.type === 'checkbox').length).toEqual(6);
    expect(el.filter(e => e.nativeElement.type === 'radio').length).toEqual(3);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
