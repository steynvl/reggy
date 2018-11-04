import { Base } from './base.po';
import { by, element } from 'protractor';

export class Home extends Base {

  getTutorialButton() {
    return element(by.id('tutorial-btn'));
  }

  getSamplesAndSemanticsButton() {
    return element(by.id('samples-btn'));
  }

  getCommonUseCasesButton() {
    return element(by.id('common-btn'));
  }

  getAutomataLearningButton() {
    return element(by.id('automata-btn'));
  }

  getLinkToContactPage() {
    return element(by.id('contact-link'));
  }

}
