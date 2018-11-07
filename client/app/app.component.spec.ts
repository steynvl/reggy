import { NO_ERRORS_SCHEMA } from '@angular/core';
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';

import { AppComponent } from './app.component';

describe('Component: App', () => {
  let component: AppComponent;
  let fixture: ComponentFixture<AppComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AppComponent ],
      schemas: [ NO_ERRORS_SCHEMA ]
    })
      .compileComponents().then(() => {
      fixture = TestBed.createComponent(AppComponent);
      component = fixture.componentInstance;
      fixture.detectChanges();
    });
  }));

  it('should create the app', async(() => {
    expect(component).toBeTruthy();
  }));

  it('should display the navigation bar correctly', () => {
    const de = fixture.debugElement.queryAll(By.css('a'));

    const navItems = [
      '', 'HOME', 'GENERATE REGEX',
      'via sample-based generation', 'via common use cases',
      'via learning', 'CONTACT US'
    ];

    expect(de.length).toBe(navItems.length);
    expect(de[0].nativeElement.textContent).toEqual(navItems[0]);

    for (let i = 1; i < de.length; i++) {
      expect(de[i].nativeElement.textContent).toContain(navItems[i]);
    }
  });

});
