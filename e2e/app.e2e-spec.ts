import { browser, by, element } from 'protractor';
import { Base } from './page-objects/base.po';

describe('Reggy: App', () => {
  let page: Base;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new Base();
    page.navigateToHome();
  });

  it('Page title should be "Home | Reggy"', () => {
    page.isHomePage().then(val => expect(val).toBe(true));
  });

  it('should collapse the navbar for low resolutions', () => {
    browser.manage().window().setSize(640, 480);
    const el = element(by.tagName('button'));
    el.getText().then(text => expect(text).toEqual(''));
  });

  it('Home link on navbar should take us to same page', () => {
    const el = element(by.id('to-home'));

    el.click();
    browser.waitForAngular();
    page.isHomePage().then(val => expect(val).toBe(true));
  });

  // it('Tutorial link on navbar should navigate to correct page', () => {
  //   const el = element(by.id('to-tutorial'));

  //   el.click();
  //   browser.waitForAngular();
  //   page.isTutorialPage().then(val => expect(val).toBe(true));
  // });

  it('Generate -> via sample-based generation link on navbar should navigate to correct page', () => {
    element(by.id('themes')).click();
    browser.waitForAngular();
    const el = element(by.id('to-samples'));

    el.click();
    browser.waitForAngular();
    page.isSamplesAndSemanticsPage().then(val => expect(val).toBe(true));
  });

  it('Generate -> via common use cases link on navbar should navigate to correct page', () => {
    element(by.id('themes')).click();
    browser.waitForAngular();
    const el = element(by.id('to-common'));

    el.click();
    browser.waitForAngular();
    page.isCommonUseCasesPage().then(val => expect(val).toBe(true));
  });

  it('Generate -> via learning link on navbar should navigate to correct page', () => {
    element(by.id('themes')).click();
    browser.waitForAngular();
    const el = element(by.id('to-gram-inf'));

    el.click();
    browser.waitForAngular();
    page.isAutomataLearningPage().then(val => expect(val).toBe(true));
  });

  it('Contact Us link on navbar should navigate to correct page', () => {
    const el = element(by.id('to-contact'));

    el.click();
    browser.waitForAngular();
    page.isContactPage().then(val => expect(val).toBe(true));
  });

});
