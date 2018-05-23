import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html'
})
export class ContactComponent implements OnInit {

  constructor(private router: Router,
              private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('Contact Us | Reggy');
  }

}
