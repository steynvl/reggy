import { Base } from './base.po';
import { by, element } from 'protractor';

export class Contact extends Base {

  getSubmitButton() {
    return element(by.id('submit-btn'));
  }

}
