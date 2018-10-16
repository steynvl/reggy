import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { Ipv4AddressInfoComponent } from "./ipv4-address-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-ipv4-address-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-ipv4-address-info>`
})
class HostComponent {
  @ViewChild(Ipv4AddressInfoComponent)
  public componentUnderTest: Ipv4AddressInfoComponent;
}

describe('Component: Common -> Ipv4', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [Ipv4AddressInfoComponent, HostComponent],
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

  it('should create ipv4 info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "IPv4 address" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('IPv4 address');
  });

  it('Should contain 5 check boxes', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(5);

    expect(el.filter(e => e.nativeElement.type === 'checkbox').length).toEqual(5);
  });

  it('Should contain 3 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(3);
  });

  it('should contain General regular expression information', () => {
    const el = fixture.debugElement.query(By.css('#gen-info')).nativeElement;
    expect(el.textContent).toEqual('General regular expression information');
  });

});
