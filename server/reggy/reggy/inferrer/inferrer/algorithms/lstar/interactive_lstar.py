import copy
from inferrer import utils, automaton
from typing import Tuple, Dict


class InteractiveLstar:

    def __init__(self, user_info):
        self._user_info = user_info
        self._alphabet = user_info['alphabet']
        stage = user_info['stage']

        if stage == 'start':
            self._ot = self._initialise()
        else:
            pass # TODO build observation table from user_info

        self._check_consistency_and_closure()

    def _initialise(self):
        self._red = {''}
        self._blue = copy.deepcopy(self._alphabet)

        ot = utils.ObservationTable(self._blue, self._red, self._alphabet)

        ot.sta = self._red.union(self._blue)
        ot.exp = {''}

        membership_queries = self._user_info['membershipQueries']

        ot.put('', '', membership_queries[''])
        for a in self._alphabet:
            ot.put(a, '', membership_queries[a])

        return ot

    def _check_consistency_and_closure(self):
        is_closed, is_consistent = self._ot.is_closed_and_consistent()

        if self._user_info['closedMembershipQueries']:
            pass
        elif self._user_info['consistentMembershipQueries']:
            pass
        elif is_closed and is_consistent:
            self._answer = {
                'stage': 'eq',
                'dot': self._get_dot_code(self._ot)
            }
        elif not is_closed:
            self._answer = {
                'stage': 'closedMembershipQueries',
                'mq': self._get_closed_membership_queries()
            }
        elif not is_consistent:
            self._answer = {
                'stage': 'consistentMembershipQueries',
                'mq': self._get_consistent_membership_queries()
            }

    def _get_closed_membership_queries(self) -> Dict[Tuple[str, str], str]:
        ot = self._ot.copy()
        red = self._red.copy()
        blue = self._blue.copy()

        queries = {}
        for s in self._blue:
            if not all([ot.get_row(s) != ot.get_row(u) for u in red]):
                continue

            red.add(s)
            blue.remove(s)

            for a in self._alphabet:
                sa = s + a
                if sa not in blue:
                    blue.add(sa)
                    ot.add_row(sa)

            for u, e in ot.find_holes():
                queries[(u, e)] = u + e

        return queries

    def _get_consistent_membership_queries(self) -> Dict[Tuple[str, str], str]:
        ot = self._ot.copy()
        s1, s2, a, e = self._find_inconsistent(ot)

        ae = a + e
        ot.exp.add(ae)
        ot.add_column_to_table(ae)

        queries = {(u, e): u + e for u, e in ot.find_holes()}
        return queries

    def _find_inconsistent(self, ot: utils.ObservationTable) -> Tuple[str, str, str, str]:
        """
        Tries to find two inconsistent rows s1 and s2 in the
        observation table. s1 and s2 are elements of red.
        OT[s1] == OT[s2] and OT[s1.a][e] != OT[s2.a][e] where
        a is an element in the alphabet and e is an
        experiment (element in the set ot.exp)

        :param ot: The observation table to find two inconsistent
                   red states.
        :type ot: ObservationTable
        :return: Inconsistent row
        :rtype: Tuple[str, str, str, str]
        """
        for s1 in self._red:
            for s2 in self._red:
                if s1 == s2:
                    continue
                for a in self._alphabet:
                    for e in ot.exp:
                        if ot.get_row(s1) == ot.get_row(s2) and \
                            ot.entry_exists(s1 + a, e) and ot.entry_exists(s2 + a, e) \
                                and ot.get(s1 + a, e) != ot.get(s2 + a, e):
                            return s1, s2, a, e
        return '', '', '', ''

    def _get_dot_code(self, ot: utils.ObservationTable) -> str:
        """
        Builds an automaton from the observation table.

        :param ot: The data to build the dfa from.
        :type ot: ObservationTable
        :return: The dfa built from the observation table.
        :rtype: Automaton
        """
        dfa = automaton.Automaton(self._alphabet)

        for u in self._red:
            for v in ot.ot.keys():
                if u == v:
                    continue

                if len(v) < len(u) and ot.get_row(v) != ot.get_row(u):
                    dfa.states.add(automaton.State(u))

        for u in dfa.states:
            if ot.entry_exists(u.name, ''):
                if ot.get(u.name, '') == 1:
                    dfa.accept_states.add(u)
                elif ot.get(u.name, '') == 0:
                    dfa.reject_states.add(u)

            for a in self._alphabet:
                for w in dfa.states:
                    if ot.get_row(u.name + a) == ot.get_row(w.name):
                        dfa.add_transition(u, w, a)

        return dfa.minimize().create_graphviz_object().source
