import { browser } from 'protractor';
import { Contact } from './page-objects/contact.po';

describe('Reggy: Contact page', () => {
  let page: Contact;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new Contact();
    page.navigateToContact();
  });

  it('Page title should be "Contact Us | Reggy"', () => {
    page.isContactPage().then(val => expect(val).toBe(true));
  });

  it('Pressing submit button should stay on same page', () => {
    const el = page.getSubmitButton();
    el.click();
    browser.waitForAngular();
    page.isContactPage().then(val => expect(val).toBe(true));
  });

});
