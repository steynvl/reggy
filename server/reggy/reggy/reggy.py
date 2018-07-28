from reggy.common import CommonUseCases
from reggy.samples import SamplesAndSemantics


class Reggy:

    def __init__(self, samples):
        self._samples = samples
        self._re = None
        self._calculate_regex()

    def get_re(self):
        return self._re

    def _calculate_regex(self):
        gen_method = self._samples['generateMethod']

        if gen_method == 'samplesAndSemantics':
            self._re = SamplesAndSemantics(self._samples).get_re()
        elif gen_method == 'commonUseCases':
            self._re = CommonUseCases(self._samples).get_re()
