import { Component } from '@angular/core';
import { examples } from './perl-examples';

@Component({
  selector: 'app-perl-code-samples',
  templateUrl: './perl.component.html',
  styleUrls: ['./perl.component.css']
})
export class PerlComponent {

  selectedExample: string;
  examples = examples;
  regex: string;

  changed() {
    this.regex = '^[2-9]version\\d*$';
    examples[this.selectedExample] = examples[this.selectedExample].replace('__regex__', this.regex);
  }

}
