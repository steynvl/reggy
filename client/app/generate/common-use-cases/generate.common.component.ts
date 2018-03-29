import { Component, OnInit } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';
import { GeneralRegexInfo } from '../../models/general-regex-info';

@Component({
  selector: 'app-generate-common',
  templateUrl: './generate.common.component.html',
  styleUrls: ['./generate.common.component.css']
})
export class GenerateCommonComponent implements OnInit {

  type: string;
  generalRegexInfo: GeneralRegexInfo;

  constructor(public toast: ToastComponent) { }

  ngOnInit(): void {
    this.generalRegexInfo = {
      startRegexMatchAt: 'Anywhere',
      endRegexMatchAt  : 'Anywhere',
      regexTarget      : 'Java'
    };
  }

}
