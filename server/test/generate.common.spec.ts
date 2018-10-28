import * as chai from 'chai';
import { describe, it } from 'mocha';
import { app } from '../app';
import * as payloads from './generate.common.payloads';
import { HttpHeaders } from '@angular/common/http';

process.env.NODE_ENV = 'test';

chai.use(require('chai-http')).should();

const httpHeaders = new HttpHeaders()
  .set('Content-Type', 'application/json');

describe('Generate: Common use cases', () => {

  it('should generate regex for credit card numbers', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.creditCardNumbers)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b3[47]\\d{13}\\b\')');
        done();
      });
  });

  it('should generate regex for currencies', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.currencies)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b(?:ALL|USD|EUR|BTN|CVE)\\b\')');
        done();
      });
  });

  it('should generate regex for date and time', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.dateAndTime)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b[0-9]{2}/(?:1[0-2]|[1-9])/(?:[12][0-9]|[1-9]|30|[12][0-9]|[1-9]|3[01]|[12][0-9]|[1-9])\\b\')');
        done();
      });
  });

  it('should generate regex for email addresses', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.emailAddresses)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b[\\d!#$%&\\\'*+/=?_`a-z{|}~^-]+(?:\\.[\\d!#$%&\\\'*+/=?_`a-z{|}~^-]+)*@(?:[\\da-z-]+\\.)+[a-z]{2,63}\\b\')');
        done();
      });
  });

  it('should generate regex for Globally Unique Identifier (GUID)', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.GUID)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b\\{[\\dA-Fa-f]{8}-[\\dA-Fa-f]{4}-[\\dA-Fa-f]{4}-[\\dA-Fa-f]{4}-[\\dA-Fa-f]{12}}\\b\')');
        done();
      });
  });

  it('should generate regex for IPv4 addresses', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.ipv4)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\b\')');
        done();
      });
  });

  it('should generate regex for National ID', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.nationalID)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b(?!000|666)[0-8]\\d{2}-(?!00)\\d{2}-(?!0000)\\d{4}\\b\')');
        done();
      });
  });

  it('should generate regex for passwords', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.password)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{5,}$\')');
        done();
      });
  });

  it('should generate regex for URLs', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.URL)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\bhttp://(?:[\\da-z-]+\\.)+[a-z]{2,63}/?\\b\')');
        done();
      });
  });

  it('should generate regex for usernames', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.username)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'^[A-Za-z].{4,49}$\')');
        done();
      });
  });

  it('should generate regex for VAT numbers', done => {
    chai.request(app)
      .post('/api/generate/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.VAT)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.compiledRegex.should.equals('regex = re.compile(r\'\\b(?:U\\d{8}|[\\dA-Z]\\\\d{7}[\\dA-Z]|\\d{8})\\b\')');
        done();
      });
  });

});
