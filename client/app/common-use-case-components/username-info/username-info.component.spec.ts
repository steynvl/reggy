import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { UsernameInfoComponent } from "./username-info.component";

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-username-info [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-username-info>`
})
class HostComponent {
  @ViewChild(UsernameInfoComponent)
  public componentUnderTest: UsernameInfoComponent;
}

describe('Component: Common -> Username', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [UsernameInfoComponent, HostComponent],
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

  it('should create username info component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "Username" as a header', () => {
    const el = fixture.debugElement.query(By.css('#page-header')).nativeElement;
    expect(el.textContent).toEqual('Username');
  });

  it('Should contain 26 input fields', () => {
    const el = fixture.debugElement.queryAll(By.css('input'));
    expect(el.length).toEqual(26);
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
