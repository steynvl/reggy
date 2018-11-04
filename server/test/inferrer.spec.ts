import * as chai from 'chai';
import { describe, it } from 'mocha';
import { app } from '../app';
import * as payloads from './inferrer.payloads';
import { HttpHeaders } from '@angular/common/http';

process.env.NODE_ENV = 'test';

chai.use(require('chai-http')).should();

const httpHeaders = new HttpHeaders()
  .set('Content-Type', 'application/json');

describe('Inferrer: Automata learning', () => {

  it('should learn grammar over binary string containing 101 as substring', done => {
    chai.request(app)
      .post('/api/inferrer/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.substring)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.contain('1');
        res.body.regex.should.contain('0');
        res.body.regex.should.contain('*');
        res.body.dot.should.contain('digraph');
        done();
      });
  });

  it('should learn grammar where every string contains an even number of a\'s and b\'s', done => {
    chai.request(app)
      .post('/api/inferrer/')
      .send({
        headers: httpHeaders,
        params: JSON.stringify(payloads.even)
      })
      .end((err, res) => {
        res.should.have.status(200);
        res.body.code.should.equals(0);
        res.body.regex.should.contain('a');
        res.body.regex.should.contain('b');
        res.body.regex.should.contain('*');
        res.body.dot.should.contain('digraph');
        done();
      });
  });

});
