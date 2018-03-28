import { Username } from '../models/common-use-case-models/username';

export class ValidateCommon {

  static isValidUsernameInfo(username: Username): boolean {
    const validLength = /^[1-9]\d*$/;

    username.minimumLength += '';
    username.maximumLength += '';

    if (username.shouldStartWith === undefined || username.shouldStartWith.trim() === ''
        || username.shouldContain === undefined || username.minimumLength === undefined ||
        username.maximumLength === undefined || username.minimumLength.trim() === '' || username.maximumLength.trim() === '') {
      return false;
    }

    return validLength.test(username.minimumLength) && validLength.test(username.maximumLength)
      && Number.parseInt(username.minimumLength) < Number.parseInt(username.maximumLength);
  }

}
