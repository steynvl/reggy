#!/usr/bin/env python3

import sys
import json
import inferrer


def deserialize(samples):
    return json.loads(samples)


def serialize(re):
    return json.dumps(re)


def main():
    payload = deserialize(sys.argv[1])

    algorithm = payload['algorithm']
    
    if algorithm == 'interactive lstar':
        output = inferrer.InteractiveLstar(payload).get_new_queries()
    else:
        pos_examples = set(payload['positiveExamples'])
        neg_examples = set(payload['negativeExamples'])
        alphabet = inferrer.utils.determine_alphabet(pos_examples.union(neg_examples))

        if algorithm in ['rpni', 'gold']:
            learner = inferrer.Learner(alphabet=alphabet,
                                       pos_examples=pos_examples,
                                       neg_examples=neg_examples,
                                       algorithm=algorithm)
        elif algorithm in ['lstar', 'nlstar']:
            learner = inferrer.Learner(alphabet=alphabet,
                                       oracle=inferrer.oracle.PassiveOracle(pos_examples,
                                                                            neg_examples),
                                       algorithm=algorithm)
        
        dfa = learner.learn_grammar()
        output = {
            'regex': dfa.to_regex(),
            'dot': dfa.create_graphviz_object().source
        }

    sys.stdout.write(serialize(output))
    sys.stdout.flush()
        

if __name__ == '__main__':
    main()
