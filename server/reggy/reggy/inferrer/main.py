#!/usr/bin/env python3

import sys
import json
import inferrer


def deserialize(samples):
    return json.loads(samples)


def serialize(re):
    return json.dumps(re)


def perform_interactive_lstar(info):
    return {}


def main():
    payload = deserialize(sys.argv[1])
    algorithm = payload['algorithm']
    
    if algorithm == 'interactive lstar':
        output = perform_interactive_lstar(payload)
    else:
        learner = inferrer.Learner(pos_examples=set(payload['positiveExamples']),
                                   neg_examples=set(payload['negativeExamples']),
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
