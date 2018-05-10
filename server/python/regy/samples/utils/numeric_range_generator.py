
from collections import deque

class NumericRangeGenerator:

    def __init__(self, start, end):
        self._re = None
        self.start = start
        self.end = end
        self._gen_regex()

    def get_regex(self):
        return ''.join(self._re)

    def _gen_regex(self):
        left = self.left_bounds(self.start, self.end)
        last_left = left.pop()

        right = self.right_bounds(last_left.start, self.end)
        first_right = right.popleft()

        merged = deque()
        merged.extend(left)

        if not last_left.overlaps(first_right):
            merged.append(last_left)
            merged.append(first_right)
        else:
            merged.append(_Range.join(last_left, first_right))
        
        merged.extend(right)

        regex = [i.to_regex() for i in merged]
        self._add_alternation(regex)

    def _add_alternation(self, regex: list):
        if len(regex) == 1:
            self._re = regex[0]
        else:
            self._re = '(?:{})'.format('|'.join(regex))


    @staticmethod
    def left_bounds(start, end):
        result = deque()
        while start < end:
            _range = _Range.from_start(start)
            result.append(_range)
            start = _range.end + 1
        return result


    @staticmethod
    def right_bounds(start, end):
        result = deque()
        while start < end:
            _range = _Range.from_end(end)
            result.append(_range)
            end = _range.start - 1

        result.reverse()
        return result


class _Range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    @staticmethod
    def from_end(end):
        chars = list(str(end))
        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == '9':
                chars[i] = '0'
            else:
                chars[i] = '0'
                break

        return _Range(int(''.join(chars)), end)

    @staticmethod
    def from_start(start):
        chars = list(str(start))

        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == '0':
                chars[i] = '9'
            else:
                chars[i] = '9'
                break

        return _Range(start, int(''.join(chars)))

    @staticmethod
    def join(a, b):
        return _Range(a.start, b.end)

    def overlaps(self, r):
        return self.end > r.start and r.end > self.start

    def __str__(self):
        return 'Range(start={}, end={})'.format(self.start, self.end)

    def to_regex(self):
        start_str = str(self.start)
        end_str = str(self.end)

        result = []
        for pos in range(len(start_str)):
            if start_str[pos] == end_str[pos]:
                result.append(start_str[pos])
            else:
                result.extend(['[', start_str[pos], '-', end_str[pos], ']'])

        return ''.join(result)


if __name__ == '__main__':
    import sys
    print(NumericRangeGenerator(int(sys.argv[1]), int(sys.argv[2])).get_regex())
