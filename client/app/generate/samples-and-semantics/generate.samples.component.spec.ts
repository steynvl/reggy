import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By, Title } from '@angular/platform-browser';

import { NO_ERRORS_SCHEMA } from '@angular/core';
import { GenerateSamplesComponent } from './generate.samples.component';
import { VerificationService } from '../../services/verification.service';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';

class MockClass {
  setTitle(newTitle: string): void { }
}

describe('Component: Samples and Semantics', () => {
  let component: GenerateSamplesComponent;
  let fixture: ComponentFixture<GenerateSamplesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [GenerateSamplesComponent],
      schemas: [NO_ERRORS_SCHEMA]
    });

    TestBed.overrideComponent(
      GenerateSamplesComponent,
      {
        set: {
          providers: [
            { provide: GenerateService, useClass: MockClass},
            { provide: ToastComponent, useClass: MockClass},
            { provide: Title, useClass: MockClass},
            { provide: VerificationService, useClass: MockClass}
          ]
        }
      }
    ).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GenerateSamplesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create samples and semantics component', () => {
    expect(component).toBeTruthy();
  });

  it('should have a button with the text "Mark"', () => {
    const el = fixture.debugElement.query(By.css('button')).nativeElement;
    expect(el.textContent).toEqual('Mark');
  });

  it('Should contain text area for sample strings', () => {
    const el = fixture.debugElement.query(By.css('textarea')).nativeElement;
    expect(el.placeholder).toEqual('Sample text...');
  });

  it('should contain button to upload file, which only accepts .txt files', () => {
    const el = fixture.debugElement.query(By.css('input')).nativeElement;
    expect(el.accept).toEqual('.txt');
  });

});
