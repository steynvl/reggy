import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Title } from '@angular/platform-browser'


@Component({
  selector: 'app-tutorial',
  templateUrl: './tutorial.component.html',
  styleUrls: ['./tutorial.component.css']
})
export class TutorialComponent implements OnInit {

  constructor(private router: Router,
              private titleService: Title) { }

  ngOnInit(): void {
    this.titleService.setTitle('Tutorial | Reggy');

    // TODO remove, was just testing injecting router
    this.router.navigate(['/tutorial']);
  }

}


