import { Component, Input, OnInit } from '@angular/core';
import { examples } from './perl-examples';
import { GeneratedRegex } from '../../models/generated-regex';

@Component({
  selector: 'app-perl-code-samples',
  templateUrl: './perl.component.html',
  styleUrls: ['./perl.component.scss']
})
export class PerlComponent implements OnInit {

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
