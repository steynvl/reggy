import { Pipe, PipeTransform } from '@angular/core';
import { MarkedTextInfo } from '../shared/models/marked-text-info';

@Pipe({
  name: 'markedTextToView',
  pure: false
})
export class MarkedTextToView implements PipeTransform {

  transform(value: Array<MarkedTextInfo>): string {
    const markedText: Array<string> = [];
    value.forEach(u => markedText.push(u.text));
    return markedText.join(' | ');
  }

}
