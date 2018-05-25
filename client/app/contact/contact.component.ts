import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Title } from '@angular/platform-browser';
import { PayloadContact } from '../models/payload/payload-contact';
import { ContactService } from '../services/contact.service';
import { ToastComponent } from '../shared/toast/toast.component';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  payloadContact: PayloadContact;

  constructor(private router: Router,
              private titleService: Title,
              private contactService: ContactService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.titleService.setTitle('Contact Us | Reggy');
    this.payloadContact = {
      name    : '',
      email   : '',
      category: '',
      message : ''
    };
  }

  submit() {
    this.callService();
  }

  private callService() {
    this.contactService.sendContactMessage(this.payloadContact).subscribe(
      data => {
        console.log(`Data = ${data}`);
      },
      _ => {
        console.log('error');
      }

    );

  }

  getYear() {
    return new Date().getFullYear();
  }

}
