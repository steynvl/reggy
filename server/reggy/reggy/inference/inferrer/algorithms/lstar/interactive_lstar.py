import copy
from inferrer import utils, automaton
from typing import Tuple, List


class InteractiveLstar:

    def __init__(self, user_info):
        self._user_info = user_info
        self._alphabet = set(user_info['alphabet'])
        stage = user_info['stage']

        if stage == 'start':
            self._ot = self._initialise()
        else:
            self._blue = set(self._user_info['blue'])
            self._red = set(self._user_info['red'])

            self._ot = utils.ObservationTable(self._blue,
                                              self._red,
                                              self._alphabet)
            self._ot.ot = self._user_info['observationTable']
            self._ot.exp = set(self._user_info['exp'])
            self._ot.sta = set(self._user_info['sta'])

        if stage == 'equivalenceQueries':
            self._use_eq()
            self._check_consistency_and_closure()
        elif stage == 'start' or stage == 'membershipQueries':
            self._check_consistency_and_closure()
        elif stage == 'counterExample':
            self._get_eq_membership_queries()

    def get_new_queries(self):
        return self._answer

    def _initialise(self) -> utils.ObservationTable:
        self._red = {''}
        self._blue = copy.deepcopy(self._alphabet)

        ot = utils.ObservationTable(self._blue, self._red, self._alphabet)

        ot.sta = self._red.union(self._blue)
        ot.exp = {''}

        query_answers = self._user_info['queryAnswers']

        ot.put('', '', query_answers[''])
        for a in sorted(self._alphabet):
            ot.put(a, '', query_answers[a])

        return ot

    def _check_consistency_and_closure(self):
        if self._user_info['closedMembershipQueries']:
            self._close_table()
        if self._user_info['consistentMembershipQueries']:
            self._make_table_consistent()

        is_closed, is_consistent = self._ot.is_closed_and_consistent()
        if is_closed and is_consistent:
            self._answer = {
                'stage': 'eq',
                'dot': self._get_dot_code(self._ot)
            }
        elif not is_closed:
            queries = self._get_closed_membership_queries()

            if len(queries) == 0:
                if not is_consistent:
                    consistent_queries = self._get_consistent_membership_queries()
                    if len(consistent_queries) == 0:
                        self._make_equivalence_query()
                    else:
                        self._answer = {
                            'stage': 'consistentMembershipQueries',
                            'mq': consistent_queries
                        }
                else:
                    self._make_equivalence_query()
            else:
                self._answer = {
                    'stage': 'closedMembershipQueries',
                    'mq': queries
                }
        elif not is_consistent:
            queries = self._get_consistent_membership_queries()

            if len(queries) == 0:
                if not is_closed:
                    closed_queries = self._get_closed_membership_queries()
                    if len(closed_queries) == 0:
                        self._make_equivalence_query()
                    else:
                        self._answer = {
                            'stage': 'closedMembershipQueries',
                            'mq': closed_queries
                        }
                else:
                    self._make_equivalence_query()
            else:
                self._answer = {
                    'stage': 'consistentMembershipQueries',
                    'mq': self._get_consistent_membership_queries()
                }

        self._answer['blue'] = list(self._blue)
        self._answer['red'] = list(self._red)
        self._answer['alphabet'] = list(self._alphabet)
        self._answer['observationTable'] = self._ot.ot
        self._answer['exp'] = list(self._ot.exp)
        self._answer['sta'] = list(self._ot.sta)

    def _make_equivalence_query(self):
        self._answer = {
            'stage': 'eq',
            'dot': self._get_dot_code(self._ot)
        }

    def _close_table(self):
        """
        Closes the observation table by
        adding an extra row.
        """
        query_answers = self._user_info['queryAnswers']
        for s in sorted(self._blue.copy()):
            if not all([self._ot.get_row(s) != self._ot.get_row(u) for u in self._red]):
                continue

            self._red.add(s)
            self._blue.remove(s)

            for a in sorted(self._alphabet):
                sa = s + a
                if sa not in sorted(self._blue):
                    self._blue.add(sa)
                    self._ot.add_row(sa)

            for u, e in sorted(self._ot.find_holes()):
                self._ot.put(u, e, query_answers[u + e])

    def _make_table_consistent(self):
        """
        Makes the observation table consistent by
        adding an extra column.
        """
        s1, s2, a, e = self._find_inconsistent(self._ot)
        query_answers = self._user_info['queryAnswers']

        ae = a + e
        self._ot.exp.add(ae)
        self._ot.add_column_to_table(ae)

        for u, e in sorted(self._ot.find_holes()):
            self._ot.put(u, e, query_answers[u + e])

    def _use_eq(self):
        """
        This method is called when the table is closed and complete.
        The algorithm then makes an equivalence query to the oracle,
        if the oracle is not satisfied and provides us with a
        counterexample, then this method is called with that counterexample.
        The method adds new rows to the observation table, to account
        for the new counterexample.
        """
        query_answers = self._user_info['queryAnswers']
        prefix_set = sorted(set(utils.prefix_set({self._user_info['counterExample']}, self._alphabet)))

        for p in prefix_set:

            if p not in sorted(self._red):
                if p not in sorted(self._blue):
                    self._ot.add_row(p)
                self._red.add(p)
                self._blue.discard(p)

            for a in sorted(self._alphabet):
                pa = p + a
                if pa not in prefix_set:
                    if pa not in self._blue:
                        if pa not in self._red:
                            self._ot.add_row(pa)
                        self._blue.add(pa)
                        self._red.discard(pa)

        for u, e in sorted(self._ot.find_holes()):
            self._ot.put(u, e, query_answers[u + e])

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
        for s1 in sorted(self._red):
            for s2 in sorted(self._red):
                if s1 == s2:
                    continue
                for a in sorted(self._alphabet):
                    for e in sorted(ot.exp):
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

    def _get_eq_membership_queries(self):
        ot = self._ot.copy()
        red = self._red.copy()
        blue = self._blue.copy()

        prefix_set = sorted(set(utils.prefix_set({self._user_info['counterExample']}, self._alphabet)))

        for p in prefix_set:

            if p not in red:
                if p not in blue:
                    ot.add_row(p)
                red.add(p)
                blue.discard(p)

            for a in sorted(self._alphabet):
                pa = p + a
                if pa not in prefix_set:
                    if pa not in blue:
                        if pa not in red:
                            ot.add_row(pa)
                        blue.add(pa)
                        red.discard(pa)

        queries = [u + e for u, e in sorted(ot.find_holes())]

        self._answer = {
            'stage': 'equivalenceMembershipQueries',
            'mq': queries,
            'blue': list(self._blue),
            'red': list(self._red),
            'alphabet': list(self._alphabet),
            'observationTable': self._ot.ot,
            'exp': list(self._ot.exp),
            'sta': list(self._ot.sta)
        }

    def _get_closed_membership_queries(self) -> List[str]:
        ot = self._ot.copy()
        red = self._red.copy()
        blue = self._blue.copy()

        queries = []
        for s in sorted(blue.copy()):
            if not all([ot.get_row(s) != ot.get_row(u) for u in red]):
                continue

            red.add(s)
            blue.remove(s)

            for a in sorted(self._alphabet):
                sa = s + a
                if sa not in blue:
                    blue.add(sa)
                    ot.add_row(sa)

            for u, e in sorted(ot.find_holes()):
                queries.append(u + e)

        return queries

    def _get_consistent_membership_queries(self) -> List[str]:
        ot = self._ot.copy()
        s1, s2, a, e = self._find_inconsistent(ot)

        ae = a + e
        ot.exp.add(ae)
        ot.add_column_to_table(ae)

        return [u + e for u, e in sorted(ot.find_holes())]
