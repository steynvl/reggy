import { browser } from 'protractor';
import { SamplesAndSemantics } from './page-objects/samples-and-semantics.po';

describe('Reggy: Samples and Semantics', () => {
  let page: SamplesAndSemantics;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new SamplesAndSemantics();
    page.navigateToSamplesAndSemantics();
  });

  // it('Page title should be "Samples and Semantics | Reggy"', () => {
  //   page.isSamplesAndSemanticsPage().then(val => expect(val).toBe(true));
  // });
  //
  // it('Pressing mark button should add markers', () => {
  //   const el = page.getMarkButton();
  //   el.click();
  //   browser.waitForAngular();
  //   page.isSamplesAndSemanticsPage().then(val => expect(val).toBe(true));
  // });
  //
  // it('Pressing reset button should remove all markers', () => {
  //   const el = page.getResetButton();
  //   el.click();
  //   browser.waitForAngular();
  //   page.isSamplesAndSemanticsPage().then(val => expect(val).toBe(true));
  // });

});
