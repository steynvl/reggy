import { Component, Input, OnInit } from '@angular/core';
import { examples } from './perl-examples';

@Component({
  selector: 'app-perl-code-samples',
  templateUrl: './perl.component.html',
  styleUrls: ['./perl.component.css']
})
export class PerlComponent implements OnInit {

  @Input() regex: string;

  selectedExample: string;
  examples = examples;
  options: Array<string> = [];

  ngOnInit() {
    this.options = Object.keys(this.examples);
  }

  changed() {
    this.examples[this.selectedExample] = this.examples[this.selectedExample].replace('__regex__', this.regex);
  }

}
