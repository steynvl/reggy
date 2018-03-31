import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { PayloadCommon } from '../models/payload/payload-common';

@Injectable()
export class GenerateCommonService {

  constructor(private http: HttpClient) { }

  generateRegex(payload: PayloadCommon): Observable<string> {
    const serializedPayload = JSON.stringify(payload);

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<string>('api/generate/common', {
      headers: httpHeaders,
      params : serializedPayload
    });
  }

}
