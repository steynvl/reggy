import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class GenerateService {

  constructor(private http: HttpClient) { }

  generateRegex(sampleStrings: any): Observable<string> {
    return this.http.get<string>('api/generate', {params: sampleStrings});
  }

}
