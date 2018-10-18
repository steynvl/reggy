import { browser, by, element } from 'protractor';
import { Base } from './page-objects/base.po';

describe('Reggy: Home page', () => {
  let page: Base;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new Base();
    page.navigateToHome();
  });

  it('Page title should be "Home | Reggy"', () => {
    page.isHomePage().then(val => expect(val).toBe(true));
  });

  it('Home link on navbar should take us to same page', () => {
    const el = element(by.id('to-home'));

    el.click();
    browser.waitForAngular();
    page.isHomePage().then(val => expect(val).toBe(true));
  });

  it('Tutorial link on navbar should navigate to correct page', () => {
    const el = element(by.id('to-tutorial'));

    el.click();
    browser.waitForAngular();
    page.isTutorialPage().then(val => expect(val).toBe(true));
  });

  it('Generate -> via samples and semantics link on navbar should navigate to correct page', () => {
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

  it('Generate -> via grammatical inference link on navbar should navigate to correct page', () => {
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
