import os
import glob
import json


TARGETS = [
    'Java',
    'Perl',
    'POSIX',
    'Python',
    'JavaScript',
    'PHP',
    'Golang',
    'Rust',
    'C#',
    'Scala',
    'Kotlin'
]


def read_resources(component: str, directory: str):
    base = os.path.dirname(os.path.realpath(__file__))

    for file in sorted(glob.glob('{}/resources/{}/{}/*.json'.format(base,
                                                                    component,
                                                                    directory))):
        with open('{}'.format(file), 'r') as f:
            info = json.load(f)

        with open(file.replace('.json', '.out'), 'r') as f:
            expected = {}
            for i, line in enumerate(f.readlines()):
                line = line.strip()

                if i == 0 or i % 3 == 0:
                    expected[line] = {}
                    lang = line
                elif (i - 1) == 0 or (i - 1) % 3 == 0:
                    expected[lang]['compiled'] = line
                else:
                    expected[lang]['regex'] = line

        yield info, expected
