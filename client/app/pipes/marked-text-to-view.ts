import { Pipe, PipeTransform } from '@angular/core';
import { MarkedTextInfo } from '../models/marked-text-info';

@Pipe({
  name: 'markedTextToView',
  pure: false
})
export class MarkedTextToView implements PipeTransform {

  transform(value: Array<MarkedTextInfo>): string {
    return value.map(u => u.text).join(' | ');
  }

}
