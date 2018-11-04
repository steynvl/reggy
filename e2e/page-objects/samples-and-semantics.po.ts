import { Base } from './base.po';
import { by, element } from 'protractor';

export class SamplesAndSemantics extends Base {

  getMarkButton() {
    return element(by.id('mark-btn'));
  }

  getResetButton() {
    return element(by.id('reset-btn'));
  }

}
