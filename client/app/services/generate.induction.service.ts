import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class GenerateInductionService {

  constructor(private http: HttpClient) { }

  generateRegex(sampleStrings: any): Observable<string> {

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<string>('api/generate/induction', {
      headers: httpHeaders,
      params: sampleStrings
    });
  }

}
