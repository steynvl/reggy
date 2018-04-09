import {Component, Input, OnInit, ViewChild} from '@angular/core';;
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { currencies } from './currencies';
import { DataTable, DataTableTranslations, DataTableResource } from 'angular5-data-table';

@Component({
  selector: 'app-currency-info',
  templateUrl: './currency-info.component.html',
  styleUrls: ['./currency-info.component.css']
})
export class CurrencyInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  generatedRegex: string;

  currencyResource = new DataTableResource(currencies);
  currencies = [];
  currencyCount = 0;
  selectedItems = new Set();

  /* special params */
  translations = <DataTableTranslations>{
    indexColumn    : 'Index column',
    expandColumn   : 'Expand column',
    selectColumn   : 'Select column',
    paginationLimit: 'Max results',
    paginationRange: 'Result range'
  };

  @ViewChild(DataTable) currenciesTable;

  constructor(private generateCommonService: GenerateCommonService,
              public toast: ToastComponent) { }

  ngOnInit() {
    this.currencies = currencies;
    this.currencyResource.count().then(count => this.currencyCount = count);
  }

  reloadCurrencies(params) {
    this.currencyResource.query(params).then(_currencies => this.currencies = _currencies);
  }

  selectedCurrencies() {
    const selectedCurrencies = new Set();
    this.currenciesTable.selectedRows.forEach(u => selectedCurrencies.add(u.item.currency));
    return Array.from(selectedCurrencies).join(', ');
  }

  clickedRow(rowEvent) {
    // TODO
    // console.log('Country = ' + rowEvent.row.item.country);
    // console.log('Currency= ' + rowEvent.row.item.currency);
  }

  private constructPayload(): PayloadCommon {
    return {
      type            : 'Currency',
      information     : undefined,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  generateRegex() {
    this.generatedRegex = undefined;
    this.callService();
  }

  private callService() {
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
      data => this.generatedRegex = data.trim(),
      error => console.log(error)
    );
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
