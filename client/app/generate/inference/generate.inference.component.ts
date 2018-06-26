import { Component, OnInit } from '@angular/core';
import { GenerateService } from '../../services/generate.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { Title } from '@angular/platform-browser';

import Viz from 'viz.js';
import { Module, render } from 'viz.js/full.render.js';

@Component({
  selector: 'app-generate-inference',
  templateUrl: './generate.inference.component.html',
  styleUrls: ['./generate.inference.component.css']
})
export class GenerateInferenceComponent implements OnInit {

  constructor(private generateService: GenerateService,
              public toast: ToastComponent,
              private titleService: Title) {
  }

  ngOnInit() {
    this.titleService.setTitle('Inference | Reggy');

    let viz = new Viz({ Module, render });

    viz.renderSVGElement('digraph { a -> b }')
      .then(function(element) {
        document.getElementById('dfa').appendChild(element);
      })
      .catch(error => {
        /* create a new Viz instance (@see Caveats page for more info) */
        viz = new Viz();

        /* possibly display the error */
        console.error(error);
      });
  }

  // generateRegex() {
  //   this.generatedRegex = undefined;
  //
  //   const payload = JSON.stringify(this.constructPayload());
  //
  //   this.generateService.generateRegex(payload).subscribe(
  //     data => this.generatedRegex = data.trim(),
  //     error => console.log(error)
  //   );
  // }


  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
