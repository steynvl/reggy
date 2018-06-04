import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { PayloadSamples } from '../models/payload/payload-samples';
import { ServerResponse } from '../models/server-response/server-response';
import { PayloadCommon } from '../models/payload/payload-common';

@Injectable()
export class GenerateService {

  constructor(private http: HttpClient) { }

  generateRegex(payload: PayloadSamples | PayloadCommon): Observable<ServerResponse> {
    const serializedPayload = JSON.stringify(payload);

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<ServerResponse>('api/generate', {
      headers: httpHeaders,
      params : serializedPayload
    });
  }

}
