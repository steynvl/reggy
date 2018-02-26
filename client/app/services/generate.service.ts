import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class GenerateService {

  constructor(private http: HttpClient) { }

  generateRegex(sampleStrings: any): Observable<Array<string>> {
    return this.http.get<Array<string>>('api/generate', {params: sampleStrings});
  }

}
