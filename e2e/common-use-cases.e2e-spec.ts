import { browser } from 'protractor';
import { CommonUseCases } from './page-objects/common-use-cases.po';

describe('Reggy: Common use cases', () => {
  const NR_OF_COMMON_USE_CASES = 11;
  let page: CommonUseCases;

  beforeEach(() => {
    browser.manage().window().setSize(1600, 900);
    page = new CommonUseCases();
    page.navigateToCommonUseCases();
  });

  it('Page title should be "Common Use Cases | Reggy"', () => {
    page.isCommonUseCasesPage().then(val => expect(val).toBe(true));
  });

  it('Page should have one select field', () => {
    const select = page.getCommonUseCaseSelectField();
    expect(select).not.toBeNull();
  });

  it(`Page should have ${NR_OF_COMMON_USE_CASES} common use cases`, () => {
    page.getNumberOfCommonUseCases()
      .then(n => expect(n).toEqual(NR_OF_COMMON_USE_CASES));
  });

  it('Selecting specific common use case should display appropriate information', () => {
    for (let i = 0; i < NR_OF_COMMON_USE_CASES; i++) {
      const option = page.getCommonUseCaseByIndex(i);

      option.getText().then(text => {
        option.click();
        browser.waitForAngular();

        switch (text) {
          case 'Credit card number':
            page.isDisplayingCreditCardInformation().then(val => expect(val).toBe(true));
            break;
          case 'Currency':
            page.isDisplayingCurrencyInformation().then(val => expect(val).toBe(true));
            break;
          case 'Date and time':
            page.isDisplayingDateAndTimeeInformation().then(val => expect(val).toBe(true));
            break;
          case 'Email address':
            page.isDisplayingEmailAddressInformation().then(val => expect(val).toBe(true));
            break;
          case 'GUID':
            page.isDisplayingGUIDInformation().then(val => expect(val).toBe(true));
            break;
          case 'IPv4 address':
            page.isDisplayingIpv4Information().then(val => expect(val).toBe(true));
            break;
          case 'National ID':
            page.isDisplayingNationalIDInformation().then(val => expect(val).toBe(true));
            break;
          case 'Password':
            page.isDisplayingPasswordInformation().then(val => expect(val).toBe(true));
            break;
          case 'URL':
            page.isDisplayingURLInformation().then(val => expect(val).toBe(true));
            break;
          case 'Username':
            page.isDisplayingUsernameInformation().then(val => expect(val).toBe(true));
            break;
          case 'VAT number':
            page.isDisplayingVATNumberInformation().then(val => expect(val).toBe(true));
            break;
          default:
            expect(true).toEqual(false);
        }
      });
    }

  });

});
