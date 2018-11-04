import * as chai from 'chai';
import { describe, it } from 'mocha';

process.env.NODE_ENV = 'test';

chai.use(require('chai-http')).should();

describe('Contact Us', () => {

  it('should send email', done => {
    done();
  });

});
