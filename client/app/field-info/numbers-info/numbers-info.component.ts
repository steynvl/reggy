import {Component, Input, OnInit} from '@angular/core';
import { Numbers } from '../../models/marker-info/numbers';

@Component({
  selector: 'app-numbers-info',
  templateUrl: './numbers-info.component.html',
  styleUrls: ['./numbers-info.component.css']
})
export class NumbersInfoComponent implements OnInit {

  ngOnInit(): void {
    console.log(this.numbers);
  }

  @Input() numbers: Numbers;

}
