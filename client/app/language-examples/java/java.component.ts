import { Component, Input, OnInit } from '@angular/core';
import { examples } from './java-examples';

@Component({
  selector: 'app-java-code-samples',
  templateUrl: './java.component.html',
  styleUrls: ['./java.component.css']
})
export class JavaComponent implements OnInit {

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
