import re
from collections import deque


class NumericRange:

    def __init__(self, start: int, end: int):
        self._re = None
        self._calculate_re(start, end)

    def get_re(self):
        return self._re

    def _calculate_re(self, start: int, end: int):
        regex = []
        if start >= 0 and end >= 0:
            regex.append(_NumericRangeGenerator(start, end, insert_minus=False).get_regex())

        elif start < 0 and end >= 0:
            regex.append(_NumericRangeGenerator(1, abs(start), insert_minus=True).get_regex())
            if end == 0:
                regex.append('0')
            else:
                regex.append(_NumericRangeGenerator(0, end, insert_minus=False).get_regex())

        else:
            regex.append(_NumericRangeGenerator(abs(end), abs(start), insert_minus=True).get_regex())

        if len(regex) == 1:
            self._re = '|'.join(regex)
        else:
            self._re = '(?:{})'.format('|'.join(regex))

        self._add_repetition_info()

    def _add_repetition_info(self):
        matches = list(re.finditer(r'(?:\[0-9\]){2,}', self._re))

        if len(matches) > 0:
            new_re = [self._re[:matches[0].start()]]

            for i, match in enumerate(matches):
                length = len(match.group()) // 5
                new_re.append('[0-9]{%d}' % length)

                if i == len(matches) - 1:
                    new_re.append(self._re[match.end():])
                else:
                    new_re.append(self._re[match.end():matches[i + 1].start()])

            self._re = ''.join(new_re)


class _NumericRangeGenerator:

    def __init__(self, start, end, insert_minus):
        self._re = None
        self._start = start
        self._end = end
        self._insert_minus = insert_minus
        self._gen_regex()

    def get_regex(self):
        return ''.join(self._re)

    def _gen_regex(self):
        left = self.left_bounds(self._start, self._end)
        last_left = left.pop()

        right = self.right_bounds(last_left.start, self._end)
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
        minus = '-' if self._insert_minus else ''
        if len(regex) == 1:
            self._re = '{}{}'.format(minus, regex[0])
        else:
            self._re = '{}(?:{})'.format(minus, '|'.join(regex))

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
