import { Component, Input, OnInit } from '@angular/core';
import { examples } from './java-examples';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-java-code-samples',
  templateUrl: './java.component.html',
  styleUrls: ['./java.component.scss']
})
export class JavaComponent implements OnInit {

  @Input() generatedRegex: GeneratedRegex;

  selectedExample: string;
  examples = examples;
  options: Array<string> = [];

  ngOnInit() {
    this.options = Object.keys(this.examples);
  }

  changed() {
    const example = this.examples[this.selectedExample];

    if (example.includes('__compile__')) {
      this.examples[this.selectedExample] = this.examples[this.selectedExample].replace('__compile__', this.generatedRegex.compiledRegex);
    } else {
      this.examples[this.selectedExample] = this.examples[this.selectedExample].replace('__regex__', this.generatedRegex.regex);
    }
  }

}
