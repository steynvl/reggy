import { Component } from '@angular/core';
import { examples } from './java-examples';

@Component({
  selector: 'app-java-code-samples',
  templateUrl: './java.component.html',
  styleUrls: ['./java.component.css']
})
export class JavaComponent {

  selectedExample: string;
  examples = examples;
  regex: string;

  changed() {
    this.regex = '^[2-9]version\\d*$';
    examples[this.selectedExample] = examples[this.selectedExample].replace('__regex__', this.regex);
  }

}
