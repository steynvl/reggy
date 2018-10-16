import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';

import { HomeComponent } from './home.component';

describe('Component: Home', () => {
  // let component: HomeComponent;
  // let fixture: ComponentFixture<HomeComponent>;

  beforeEach(async(() => {
    // TestBed.configureTestingModule({
    //   declarations: [ HomeComponent ]
    // })
    // .compileComponents();
  }));

  beforeEach(() => {
    // fixture = TestBed.createComponent(HomeComponent);
    // component = fixture.componentInstance;
    // fixture.detectChanges();
  });

  it('hello1', () => {
    expect('ja').toContain('ja');
  });

  it('hello2', () => {
    expect('ja').toContain('ja');
  });

  it('hello3', () => {
    expect('ja').toContain('ja');
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
  //
  // it('should display the string "Contact us" in h2', () => {
  //   const el = fixture.debugElement.query(By.css('h2')).nativeElement;
  //   expect(el.textContent).toContain('Contact us');
  // });

});
