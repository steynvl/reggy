import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router'

@Component({
  selector: 'app-tutorial',
  templateUrl: './tutorial.component.html'
})
export class TutorialComponent implements OnInit {

  constructor(private router: Router) { }

    ngOnInit(): void {
        // TODO remove, was just testing injecting router
        this.router.navigate(['/tutorial']);    
    }

}
