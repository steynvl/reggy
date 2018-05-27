import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import { PayloadContact } from '../models/payload/payload-contact';
import { ContactResponse } from '../models/server-response/contact-response';

@Injectable()
export class ContactService {

  constructor(private http: HttpClient) { }

  sendContactMessage(payload: PayloadContact): Observable<ContactResponse> {
    const serializedPayload = JSON.stringify(payload);

    const httpHeaders = new HttpHeaders()
      .set('Content-Type', 'application/json');

    return this.http.post<ContactResponse>('api/contact', {
      headers: httpHeaders,
      params : serializedPayload
    });
  }

}
