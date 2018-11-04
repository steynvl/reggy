import * as chai from 'chai';
import { describe, it } from 'mocha';
import { app } from '../app';
import * as payloads from './generate.samples.payloads';
import { HttpHeaders } from '@angular/common/http';

process.env.NODE_ENV = 'test';

chai.use(require('chai-http')).should();

const httpHeaders = new HttpHeaders()
  .set('Content-Type', 'application/json');

describe('Generate: Sample-based generation', () => {

  it('should generate regex for basic characters', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.basicCharacters)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('[A-Za-z]');
        res.body.compiledRegex.should.equals('Pattern regex = Pattern.compile("[A-Za-z]");');
        done();
      });
  });

  it('should generate regex for control characters', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.controlCharacters)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.contain('[');
        res.body.compiledRegex.should.contain('regex = re.compile(r\'');
        done();
      });
  });

  it('should generate regex for digits', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.digits)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('[0-46-9]');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'[0-46-9]\')');
        done();
      });
  });

  it('should generate regex for list of literal text', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.listOfLiteralText),
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('(?:a|b)');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'(?:a|b)\')');
        done();
      });
  });

  it('should generate regex for literal text', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.literalText)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('(?i)asdsa');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'asdsa\', re.IGNORECASE)');
        done();
      });
  });

  it('should generate regex for match anything', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.matchAnything)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.contain('[^');
        res.body.compiledRegex.should.contain('regex = re.compile(r\'[^');
        done();
      });
  });

  it('should generate regex for numbers', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.numbers)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('(?:[0-9]|[1-9][0-9]|100)');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'(?:[0-9]|[1-9][0-9]|100)\')');
        done();
      });
  });

  it('should generate regex for unicode characters', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.unicodeCharacters)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.contain('[');
        res.body.compiledRegex.should.contain('regex = re.compile(r\'');
        done();
      });
  });

  it('should not be able to process request (1)', done => {
    const payload = payloads.basicCharacters;
    payload.generalRegexInfo.regexTarget = '';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payload)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(1);
        done();
      });
  });

  it('should not be able to process request (2)', done => {
    const payload = payloads.basicCharacters;
    payload.generalRegexInfo.startRegexMatchAt = '';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payload)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(1);
        done();
      });
  });

  it('should not be able to process request (3)', done => {
    const payload = payloads.basicCharacters;
    payload.generalRegexInfo.endRegexMatchAt = '';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payload)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(1);
        done();
      });
  });

  it('should not be able to process request (4)', done => {
    const payload = payloads.numbers;
    payload.sampleStringsInfo = null;
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payload)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(1);
        done();
      });
  });

  it('should not be able to process request (5)', done => {
    const payload = payloads.matchAnything;
    payload.sampleStringsInfo.map(_ => '');
    payload.generalRegexInfo.endRegexMatchAt = '';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payload)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(1);
        done();
      });
  });

  it('should factorise prefixes and suffixes from literal text', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.literalTextFactorise)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('abc(?:qqq|rrr)mlk');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'abc(?:qqq|rrr)mlk\')');
        done();
      });
  });

  it('should generate regex with appropriate repetition information (1)', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.repetition)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'[0-46-9]{1,3}\')');
        done();
      });
  });

  it('should generate regex with appropriate repetition information (2)', done => {
    const repetition = payloads.repetition;
    repetition.sampleStringsInfo[0][0].repeatInfo.repeat = '0 or 1';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(repetition)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('[0-46-9]?');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'[0-46-9]?\')');
        done();
      });
  });

  it('should generate regex with appropriate repetition information (3)', done => {
    const repetition = payloads.repetition;
    repetition.sampleStringsInfo[0][0].repeatInfo.repeat = '7';
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(repetition)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('[0-46-9]{7}');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'[0-46-9]{7}\')');
        done();
      });
  });

  it('should make two markers an alternating group', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.alternation)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('(?:dsa|[0-46-9])');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'(?:dsa|[0-46-9])\')');
        done();
      });
  });

  it('should back reference match of previous marker', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params : JSON.stringify(payloads.backReference)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.equals('([0-24-9])\\1');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'([0-24-9])\\1\')');
        done();
      });
  });

});
