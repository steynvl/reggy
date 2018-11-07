import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By, Title } from '@angular/platform-browser';

import { NO_ERRORS_SCHEMA } from '@angular/core';
import { HomeComponent } from './home.component';

class MockClass {
  setTitle(newTitle: string): void { }
}

describe('Component: Home', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [HomeComponent],
      schemas: [NO_ERRORS_SCHEMA]
    });

    TestBed.overrideComponent(
      HomeComponent,
      {
        set: {
          providers: [
            { provide: Title, useClass: MockClass}
          ]
        }
      }
    ).compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create home component', () => {
    expect(component).toBeTruthy();
  });

  it('should have two h2 tags with appropriate text', () => {
    const el = fixture.debugElement.queryAll(By.css('h2'));

    el.forEach(e => expect(e.nativeElement.textContent === 'What is reggy?'
      || e.nativeElement.textContent === 'Contact Us').toEqual(true));
  });

  it('Should contain two h5 tags', () => {
    const el = fixture.debugElement.queryAll(By.css('h5'));
    expect(el.length).toEqual(3);
  });

  it('should contain footer with copyright info', () => {
    const el = fixture.debugElement.query(By.css('footer')).nativeElement;
    expect(el).not.toBeNull();
  });

});
