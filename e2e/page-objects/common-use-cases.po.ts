import { Base } from './base.po';
import { by, element, ElementFinder, promise } from 'protractor';

export class CommonUseCases extends Base {

  getCommonUseCaseSelectField(): ElementFinder {
    return element(by.id('use-case'));
  }

  getNumberOfCommonUseCases(): promise.Promise<number> {
    return element.all(by.tagName('option'))
      .then(items => items.length);
  }

  getCommonUseCaseByIndex(idx: number) {
    return element.all(by.tagName('option')).get(idx);
  }

  isDisplayingCreditCardInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Credit card numbers');
  }

  isDisplayingCurrencyInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Currency');
  }

  isDisplayingDateAndTimeeInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Date and time');
  }

  isDisplayingEmailAddressInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Email addresses');
  }

  isDisplayingGUIDInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'GUID (Globally Unique Identifier)');
  }

  isDisplayingIpv4Information(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'IPv4 address');
  }

  isDisplayingNationalIDInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'National ID');
  }

  isDisplayingPasswordInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Password');
  }

  isDisplayingURLInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Uniform Resource Locator (URL)');
  }

  isDisplayingUsernameInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'Username');
  }

  isDisplayingVATNumberInformation(): promise.Promise<boolean> {
    return element(by.id('page-header'))
      .getText().then(text => text === 'VAT numbers');
  }

}
