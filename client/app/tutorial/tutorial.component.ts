import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Title } from '@angular/platform-browser';

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

  containers: Array<Container> = [
    new Container(1, [new Marker(1, '#FFAEB9')]),
    new Container(2, [new Marker(2, '#B0C4DE')]),
    new Container(3, [new Marker(3, '#63B8FF')]),
    new Container(4, [new Marker(4, '#EE7AE9')]),
    new Container(5, [new Marker(5, '#00FA9A')])
  ];

}

class Container {

  constructor(public id: number,
              public markers: Array<Marker>) { }

}

class Marker {

  constructor(public id: number,
              public color: string) {  }

}


