import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NO_ERRORS_SCHEMA } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { By } from '@angular/platform-browser';
import { GenerateCommonComponent } from './generate.common.component';

class MockClass { }

describe('Component: Common ', () => {
  let component: GenerateCommonComponent;
  let fixture: ComponentFixture<GenerateCommonComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [GenerateCommonComponent],
      schemas: [NO_ERRORS_SCHEMA]
    }).compileComponents();

    TestBed.overrideComponent(
      GenerateCommonComponent,
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
    fixture = TestBed.createComponent(GenerateCommonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create common use cases component', () => {
    expect(component).toBeTruthy();
  });

  it('Should contain 1 select fields', () => {
    const el = fixture.debugElement.queryAll(By.css('select'));
    expect(el.length).toEqual(1);
  });

  it('The select field should contain 11 options', () => {
    const el = fixture.debugElement.query(By.css('select')).nativeElement;
    expect(el.options.length).toEqual(11);
  });

});
