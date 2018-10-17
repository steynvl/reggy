import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { Component, NO_ERRORS_SCHEMA, ViewChild } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { JavaComponent } from './java.component';

class MockClass { }

@Component({
  selector: 'app-host-component',
  template: `<app-java-code-samples [generalRegexInfo]="{
                startRegexMatchAt: 'Anywhere',
                endRegexMatchAt  : 'Anywhere',
                regexTarget      : 'Java'
            }"></app-java-code-samples>`
})
class HostComponent {
  @ViewChild(JavaComponent)
  public componentUnderTest: JavaComponent;
}

describe('Component: Language Examples -> Java', () => {
  let component: HostComponent;
  let fixture: ComponentFixture<HostComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [JavaComponent, HostComponent],
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

  it('should create java language examples component', () => {
    expect(component).toBeTruthy();
  });

  it('should contain h4 tag with text "Examples of using the Regex in Java"', () => {
    const el = fixture.debugElement.query(By.css('h4')).nativeElement;
    expect(el.textContent).toEqual('Examples of using the Regex in Java');
  });

  it('Should contain 1 select field with 18 options', () => {
    const el = fixture.debugElement.query(By.css('select')).nativeElement;
    expect(el.options.length).toEqual(18);
  });

});
