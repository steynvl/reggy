import { Pipe, PipeTransform } from '@angular/core';
import { MarkedTextInfo } from '../models/marked-text-info';

@Pipe({
  name: 'markedTextToView',
  pure: false
})
export class MarkedTextToView implements PipeTransform {

  /**
   * Transforms an array of markers to a string 
   * separating them by the word "OR".
   * 
   * @param value text that was marked
   */
  transform(value: Array<MarkedTextInfo>): string {
    return value.map(u => u.text).join(' OR ');
  }

}
