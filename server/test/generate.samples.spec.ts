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
        res.body.regex.should.equals('[^a-zA-Z]');
        res.body.compiledRegex.should.equals('regex = re.compile(r\'[^a-zA-Z]\')');
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

});
