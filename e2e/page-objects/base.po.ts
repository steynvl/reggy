import { browser, by, element, promise, ElementFinder, ElementArrayFinder } from 'protractor';

export class Base {

  navigateToHome(): promise.Promise<any> {
    return browser.get('/');
  }

  navigateToTutorial(): promise.Promise<any> {
    return browser.get('/tutorial');
  }

  navigateToContact(): promise.Promise<any> {
    return browser.get('/contact');
  }

  navigateToSamplesAndSemantics(): promise.Promise<any> {
    return browser.get('/generate/samples');
  }

  navigateToCommonUseCases(): promise.Promise<any> {
    return browser.get('/generate/common');
  }

  navigateToAutomataLearning(): promise.Promise<any> {
    return browser.get('/generate/inference');
  }

  isHomePage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      return title === 'Home | Reggy';
    });
  }

  isTutorialPage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      return title === 'Tutorial | Reggy';
    });
  }

  isContactPage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      return title === 'Contact Us | Reggy';
    });
  }

  isSamplesAndSemanticsPage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      console.log(title);
      return title === 'Samples and Semantics | Reggy';
    });
  }

  isCommonUseCasesPage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      return title === 'Common Use Cases | Reggy';
    });
  }

  isAutomataLearningPage(): promise.Promise<boolean> {
    return browser.getTitle().then(title => {
      return title === 'Inference | Reggy';
    });
  }

}
