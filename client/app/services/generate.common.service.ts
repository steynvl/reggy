import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { PayloadCommon } from '../models/payload/payload-common';
import { ServerResponse } from '../models/server-response/server-response';

@Injectable()
export class GenerateCommonService {

  constructor(private http: HttpClient) { }

  generateRegex(payload: PayloadCommon): Observable<ServerResponse> {
    const serializedPayload = JSON.stringify(payload);

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<ServerResponse>('api/generate/common', {
      headers: httpHeaders,
      params : serializedPayload
    });
  }

}
