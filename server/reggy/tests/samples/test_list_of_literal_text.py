import unittest
import reggy

from tests.runner import read_resources, TARGETS


class TestListOfLiteralText(unittest.TestCase):

    def setUp(self):
        self._resources = read_resources('samples', 'list_of_literal_text')

    def test_01(self):
        for info, expected in self._resources:

            for target in TARGETS:
                info['generalRegexInfo']['regexTarget'] = target
                expected_lang = expected[target]

                regex = reggy.Reggy(info).get_re()

                self.assertEqual(sorted(expected_lang['compiled']), sorted(regex['compiledRegex']))
                self.assertEqual(sorted(expected_lang['regex']), sorted(regex['regex']))
