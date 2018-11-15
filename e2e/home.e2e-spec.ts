import { browser } from 'protractor';
import { Home } from './page-objects/home.po';

describe('Reggy: Home page', () => {
  let page: Home;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new Home();
    page.navigateToHome();
  });

  it('Page title should be "Home | Reggy"', () => {
    page.isHomePage().then(val => expect(val).toBe(true));
  });

  // it('Should be a button that takes us to the tutorial page', () => {
  //   const el = page.getTutorialButton();

  //   el.click();
  //   browser.waitForAngular();
  //   page.isTutorialPage().then(val => expect(val).toBe(true));
  // });

  it('Should be a text link that takes us to the contact us page', () => {
    const el = page.getLinkToContactPage();

    el.click();
    browser.waitForAngular();
    page.isContactPage().then(val => expect(val).toBe(true));
  });

  it('Should be a button that takes us to the samples and semantics page', () => {
    const el = page.getSamplesAndSemanticsButton();

    el.click();
    browser.waitForAngular();
    page.isSamplesAndSemanticsPage().then(val => expect(val).toBe(true));
  });

  it('Should be a button that takes us to the common use cases page', () => {
    const el = page.getCommonUseCasesButton();

    el.click();
    browser.waitForAngular();
    page.isCommonUseCasesPage().then(val => expect(val).toBe(true));
  });

  it('Should be a button that takes us to the automata learning page', () => {
    const el = page.getAutomataLearningButton();

    el.click();
    browser.waitForAngular();
    page.isAutomataLearningPage().then(val => expect(val).toBe(true));
  });

});
