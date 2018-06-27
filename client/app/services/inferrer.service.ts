import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { PayloadInferrer } from '../models/payload/payload-inferrer';
import { InferrerResponse } from '../models/server-response/inferrer-response';

@Injectable()
export class InferrerService {

  constructor(private http: HttpClient) { }

  inferGrammar(payload: PayloadInferrer): Observable<InferrerResponse> {

    const serializedPayload = JSON.stringify(payload);

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<InferrerResponse>('/api/inferrer', {
        headers: httpHeaders,
        params : serializedPayload
    });
  }

}
