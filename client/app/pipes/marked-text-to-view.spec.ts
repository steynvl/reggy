import { MarkedTextToView } from './marked-text-to-view';
import { MarkedTextInfo } from '../models/marked-text-info';

describe('Pipe: Literal text to view', () => {
  let pipe: MarkedTextToView;
  let markedText: Array<MarkedTextInfo> = [];

  beforeEach(() => {
    pipe = new MarkedTextToView();
  });

  it('should work for empty list', () => {
    markedText = [];

    expect(pipe.transform(markedText)).toEqual('');
  });

  it('should work for list with one item', () => {
    markedText = [
      {
        start: 0,
        end: 0,
        text: ''
      }
    ];

    expect(pipe.transform(markedText)).toEqual('');

    markedText = [
      {
        start: 0,
        end: 0,
        text: 'a'
      }
    ];

    expect(pipe.transform(markedText)).toEqual('a');
  });

  it('should work for list with multiple items', () => {
    markedText = [
      {
        start: 0,
        end: 0,
        text: 'a'
      },
      {
        start: 0,
        end: 0,
        text: 'b'
      }
    ];

    expect(pipe.transform(markedText)).toEqual('a OR b');

    markedText = [
      {
        start: 0,
        end: 0,
        text: 'a'
      },
      {
        start: 0,
        end: 0,
        text: 'b'
      },
      {
        start: 0,
        end: 0,
        text: 'casdasd'
      }
    ];

    expect(pipe.transform(markedText)).toEqual('a OR b OR casdasd');
  });

});
