import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By, Title } from '@angular/platform-browser';

import { ContactComponent } from './contact.component';
import { Router } from '@angular/router';
import { ContactService } from '../services/contact.service';
import { ToastComponent } from '../shared/toast/toast.component';
import { NO_ERRORS_SCHEMA } from '@angular/core';

class MockClass {
  setTitle(newTitle: string): void { }
}

describe('Component: Contact', () => {
  let component: ContactComponent;
  let fixture: ComponentFixture<ContactComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ContactComponent],
      schemas: [NO_ERRORS_SCHEMA]
    });

    TestBed.overrideComponent(
      ContactComponent,
      {
        set: {
          providers: [
            { provide: Router, useClass: MockClass},
            { provide: Title, useClass: MockClass},
            { provide: ContactService, useClass: MockClass},
            { provide: ToastComponent, useClass: MockClass}
          ]
        }
      }
    ).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ContactComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create contact component', () => {
    expect(component).toBeTruthy();
  });

  it('should display "CONTACT US" as a header', () => {
    const el = fixture.debugElement.query(By.css('h2')).nativeElement;
    expect(el.textContent.toLowerCase()).toContain('contact us');
  });

  it('should contain input field for name', () => {
    const el = fixture.debugElement.query(By.css('#name')).nativeElement;
    expect(el.placeholder).toEqual('Your Name');
  });

  it('should contain input field for email', () => {
    const el = fixture.debugElement.query(By.css('#email')).nativeElement;
    expect(el.placeholder).toEqual('Your Email');
  });

  it('should contain input field for category', () => {
    const el = fixture.debugElement.query(By.css('#category')).nativeElement;
    expect(el).not.toBeNull();
  });

  it('should contain input field for message', () => {
    const el = fixture.debugElement.query(By.css('#message')).nativeElement;
    expect(el.placeholder).toEqual('Your Message');
  });

  it('should contain submit button', () => {
    const el = fixture.debugElement.query(By.css('button')).nativeElement;
    expect(el).not.toBeNull();
  });

});
