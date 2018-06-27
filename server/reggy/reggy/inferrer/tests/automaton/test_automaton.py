import unittest
from collections import OrderedDict
from inferrer import automaton


class TestAutomaton(unittest.TestCase):

    def test_automaton_01(self):
        dfa = automaton.Automaton({'a', 'b'})

        self.assertTrue(automaton.State('') in dfa.states)
        dfa.add_transition(automaton.State(''), automaton.State('a'), 'a')
        self.assertTrue(dfa.transition_exists(automaton.State(''), 'a'))
        self.assertEqual(automaton.State('a'), dfa.transition(automaton.State(''), 'a'))

        try:
            dfa.add_transition(automaton.State(''), automaton.State('a'), 'c')
            self.fail('Automaton should throw ValueError when trying to add'
                      'transition with letter that is not in the alphabet!')
        except ValueError:
            self.assertTrue(True)

    def test_automaton_02(self):
        start_state = automaton.State('')
        q1 = automaton.State('1')
        q2 = automaton.State('2')
        dfa = automaton.Automaton({'a', 'b'}, start_state)

        dfa.add_transition(start_state, start_state, 'a')
        dfa.add_transition(start_state, q1, 'b')
        dfa.add_transition(q1, q2, 'a')
        dfa.add_transition(q1, q2, 'b')

        self.assertEqual(3, len(dfa.states))
        self.assertEqual(2, len(dfa._transitions.keys()))
        self.assertTrue(dfa.transition_exists(start_state, 'a'))
        self.assertTrue(dfa.transition_exists(start_state, 'b'))
        self.assertTrue(dfa.transition_exists(q1, 'a'))

        self.assertFalse(dfa.transition_exists(q2, 'a'))
        self.assertFalse(dfa.transition_exists(q2, 'b'))

        q, a = dfa.find_transition_to_q(start_state)
        self.assertEqual('a', a)
        self.assertEqual(start_state, q)

        q, a = dfa.find_transition_to_q(q2)
        self.assertEqual('a', a)
        self.assertEqual(q1, q)

    def test_build_pta_01(self):
        positive_examples = {'aa', 'aba', 'bba'}
        negative_examples = {'ab', 'abab'}

        pta = automaton.build_pta(positive_examples, negative_examples)
        accept_states = {automaton.State('aa'), automaton.State('aba'), automaton.State('bba')}
        reject_states = {automaton.State('ab'), automaton.State('abab')}

        self.assertSetEqual(accept_states, pta.accept_states)
        self.assertSetEqual(reject_states, pta.reject_states)

        q, accepted = pta.parse_string('aba')
        self.assertTrue(accepted)
        self.assertEqual(automaton.State('aba'), q)

        q, accepted = pta.parse_string('abab')
        self.assertFalse(accepted)
        self.assertEqual(automaton.State('abab'), q)

    def test_build_pta_02(self):
        positive_examples = {'aa', 'aba', 'bba'}

        pta = automaton.build_pta(positive_examples)
        accept_states = {automaton.State('aa'), automaton.State('aba'), automaton.State('bba')}

        self.assertSetEqual(accept_states, pta.accept_states)
        self.assertTrue(len(pta.reject_states) == 0)

        q, accepted = pta.parse_string('aba')
        self.assertTrue(accepted)
        self.assertEqual(automaton.State('aba'), q)

        q, accepted = pta.parse_string('a')
        self.assertFalse(accepted)
        self.assertEqual(automaton.State('a'), q)

        q, accepted = pta.parse_string('')
        self.assertFalse(accepted)
        self.assertEqual(automaton.State(''), q)

    def test_build_pta_04(self):
        positive_examples = {'aaaa', 'aaba', 'bba', 'bbaba'}
        negative_examples = {'a', 'bb', 'aab', 'aba'}

        pta = automaton.build_pta(positive_examples, negative_examples)

        self.assertEqual(4, len(pta.accept_states))
        self.assertEqual(4, len(pta.reject_states))

        for s in positive_examples:
            self.assertTrue(pta.parse_string(s)[1])
        for s in negative_examples:
            self.assertFalse(pta.parse_string(s)[1])

    def test_minimize_01(self):
        alphabet = {'a', 'b', 'c'}
        dfa = automaton.Automaton(alphabet)

        dfa.add_transition(automaton.State(''), automaton.State('2'), 'a')

        dfa.add_transition(automaton.State(''), automaton.State('3'), 'b')
        dfa.add_transition(automaton.State(''), automaton.State('3'), 'c')

        dfa.add_transition(automaton.State('3'), automaton.State('3'), 'a')
        dfa.add_transition(automaton.State('3'), automaton.State('3'), 'b')
        dfa.add_transition(automaton.State('3'), automaton.State(''), 'c')

        dfa.add_transition(automaton.State('2'), automaton.State('4'), 'a')
        dfa.add_transition(automaton.State('2'), automaton.State('4'), 'b')
        dfa.add_transition(automaton.State('2'), automaton.State('4'), 'c')

        dfa.add_transition(automaton.State('4'), automaton.State('2'), 'a')
        dfa.add_transition(automaton.State('4'), automaton.State('2'), 'b')
        dfa.add_transition(automaton.State('4'), automaton.State('2'), 'c')

        dfa.add_transition(automaton.State('5'), automaton.State('4'), 'a')
        dfa.add_transition(automaton.State('5'), automaton.State('4'), 'b')
        dfa.add_transition(automaton.State('5'), automaton.State('6'), 'c')

        dfa.states.add(automaton.State('7'))

        dfa.accept_states.update({automaton.State(''), automaton.State('6')})
        dfa.reject_states.update({automaton.State('3'), automaton.State('4'), automaton.State('7')})

        minimized_dfa = dfa.minimize()

        self.assertEqual(4, len(minimized_dfa.states))
        self.assertSetEqual({automaton.State('')}, minimized_dfa.accept_states)
        self.assertSetEqual({automaton.State('3'), automaton.State('4')}, minimized_dfa.reject_states)

        expected_transition_table = {
            automaton.State(''): OrderedDict({
                'a': automaton.State('2'),
                'b': automaton.State('3'),
                'c': automaton.State('3')
            }),
            automaton.State('3'): OrderedDict({
                'a': automaton.State('3'),
                'b': automaton.State('3'),
                'c': automaton.State('')
            }),
            automaton.State('2'): OrderedDict({
                'a': automaton.State('4'),
                'b': automaton.State('4'),
                'c': automaton.State('4')
            }),
            automaton.State('4'): OrderedDict({
                'a': automaton.State('2'),
                'b': automaton.State('2'),
                'c': automaton.State('2')
            })
        }
        transitions = minimized_dfa._transitions

        self.assertSetEqual(set(map(str, expected_transition_table.keys())),
                                set(map(str, transitions.keys())))

        for k in expected_transition_table.keys():
            for a in expected_transition_table[k].keys():
                self.assertEqual(expected_transition_table[k][a],
                                 transitions[k][a])


if __name__ == '__main__':
    unittest.main()
