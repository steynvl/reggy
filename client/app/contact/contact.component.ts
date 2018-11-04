import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Title } from '@angular/platform-browser';
import { PayloadContact } from '../models/payload/payload-contact';
import { ContactService } from '../services/contact.service';
import { ToastComponent } from '../shared/toast/toast.component';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent implements OnInit {

  isLoading: boolean;
  payloadContact: PayloadContact;
  form: FormGroup;

  constructor(private router: Router,
              private titleService: Title,
              private contactService: ContactService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.titleService.setTitle('Contact Us | Reggy');
    this.isLoading = false;

    this.form = new FormGroup({
      name: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required, Validators.email]),
      category: new FormControl('', [Validators.required]),
      msg: new FormControl('', [Validators.required])
    });

    this.payloadContact = {
      name    : '',
      email   : '',
      category: 'Suggestion',
      message : ''
    };
  }

  submit() {
    if (this.form.invalid) {
      this.toast.setMessage('Please fill in all of the fields!', 'warning', 5000);
    } else {
      this.callService();
    }
  }

  private callService() {
    this.isLoading = true;
    this.contactService.sendContactMessage(this.payloadContact).subscribe(
      data => {
        if (data.msg === 'success') {
          this.toast.setMessage('Your message has been sent!', 'success');
        } else {
          this.toast.setMessage('Unable to send message, server responded with an error!', 'danger');
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('Unable to send message, server responded with an error!', 'danger');
        this.isLoading = false;
      }
    );

  }

  getYear() {
    return new Date().getFullYear();
  }

}
