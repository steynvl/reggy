import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { PerlComponent } from './perl.component';

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-perl-code-samples [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-perl-code-samples>`
})
class HostComponent {
  @ViewChild(PerlComponent)
  public componentUnderTest: PerlComponent;
}

describe('Component: Language Examples -> Perl', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [PerlComponent, HostComponent],
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

  it('should create perl language examples component', () => {
    expect(component).toBeTruthy();
  });

  it('should contain h4 tag with text "Examples of using the Regex in Perl"', () => {
    const el = fixture.debugElement.query(By.css('h4')).nativeElement;
    expect(el.textContent).toEqual('Examples of using the Regex in Perl');
  });

  it('Should contain 1 select field with 7 options', () => {
    const el = fixture.debugElement.query(By.css('select')).nativeElement;
    expect(el.options.length).toEqual(7);
  });

});
