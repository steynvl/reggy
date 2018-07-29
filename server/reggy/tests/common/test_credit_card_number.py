import unittest
import reggy

from tests.runner import read_resources, TARGETS


class TestCreditCardNumber(unittest.TestCase):

    def setUp(self):
        self._resources = read_resources('common', 'credit_card_numbers')

    def test_01(self):
        for info, expected in self._resources:

            for target in TARGETS:
                info['generalRegexInfo']['regexTarget'] = target
                expected_lang = expected[target]

                regex = reggy.Reggy(info).get_re()

                self.assertEqual(sorted(expected_lang['compiled']), sorted(regex['compiledRegex']))
                self.assertEqual(sorted(expected_lang['regex']), sorted(regex['regex']))
