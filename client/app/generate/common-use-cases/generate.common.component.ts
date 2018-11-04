import { Component, OnInit } from '@angular/core';
import { ToastComponent } from '../../shared/toast/toast.component';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-generate-common',
  templateUrl: './generate.common.component.html',
  styleUrls: ['./generate.common.component.scss']
})
export class GenerateCommonComponent implements OnInit {

  type: string;
  generalRegexInfo: GeneralRegexInfo;

  constructor(public toast: ToastComponent,
              private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle('Common Use Cases | Reggy');

    this.generalRegexInfo = {
      startRegexMatchAt: 'Anywhere',
      endRegexMatchAt  : 'Anywhere',
      regexTarget      : 'Java'
    };
  }

}
