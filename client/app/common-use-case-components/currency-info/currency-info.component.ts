import { Component, Input, OnInit, ViewChild } from '@angular/core';
import { GeneralRegexInfo } from '../../models/general-regex-info';
import { PayloadCommon } from '../../models/payload/payload-common';
import { GenerateCommonService } from '../../services/generate.common.service';
import { ToastComponent } from '../../shared/toast/toast.component';
import { currencies } from './currencies';
import { DataTable, DataTableTranslations, DataTableResource } from 'angular5-data-table';
import { Currency } from '../../models/common-use-case-models/currency';

@Component({
  selector: 'app-currency-info',
  templateUrl: './currency-info.component.html',
  styleUrls: ['./currency-info.component.css']
})
export class CurrencyInfoComponent implements OnInit {

  @Input() generalRegexInfo: GeneralRegexInfo;

  generatedRegex: string;
  isLoading = false;

  currencyResource = new DataTableResource(currencies);
  currencies = [];
  currencyCount = 0;
  selectedItems = new Set<any>();

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
    return Array.from(this.getCurrenciesWithDuplicates()).join(', ');
  }

  clickedRow(rowEvent) {
    const item = rowEvent.row.item;
    this.selectedItems.delete(item) ? this.selectedItems.has(item) : this.selectedItems.add(item);
  }

  private constructPayload(): PayloadCommon {
    const payloadInfo: Currency = {
      currencies: Array.from(this.getCurrenciesWithDuplicates())
    };

    return {
      type            : 'Currency',
      information     : payloadInfo,
      generalRegexInfo: this.generalRegexInfo,
      generateMethod  : 'commonUseCases'
    };
  }

  getCurrenciesWithDuplicates(): Set<string> {
    const uniqueCurrencies = new Set<string>();
    this.selectedItems.forEach(item => uniqueCurrencies.add(item.currency));
    return uniqueCurrencies;
  }

  generateRegex() {
    this.callService();
  }

  private callService() {
    if (this.generatedRegex === undefined) {
      this.isLoading = true;
    }

    this.generatedRegex = undefined;
    const payload = this.constructPayload();
    this.generateCommonService.generateRegex(payload).subscribe(
      data => {
        const response = data;
        if (response.code !== 0) {
          this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        } else {
          this.generatedRegex = response.regex;
        }
        this.isLoading = false;
      },
      _ => {
        this.toast.setMessage('Unable to generate regex, server responded with an error!', 'danger');
        this.isLoading = false;
      }
    );
  }

  clickCopyToClipboard() {
    this.toast.setMessage('Regex copied to clipboard! ', 'success');
  }

}
