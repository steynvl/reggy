import { Username } from '../models/common-use-case-models/username';

export class ValidateCommon {

  static validateUsername(username: Username): boolean {
    const validLength = /^[1-9]\d*$/;

    if (!username.shouldStartWith || username.shouldStartWith.trim() === ''
        || username.shouldContain || !username.minimumLength || !username.maximumLength
        || username.minimumLength.trim() === '' || username.maximumLength.trim() === '') {
      return false;
    }

    return validLength.test(username.minimumLength) && validLength.test(username.maximumLength)
      && Number.parseInt(username.minimumLength) < Number.parseInt(username.maximumLength);
  }

}
