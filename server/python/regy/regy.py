from regy.common import CommonUseCases
from regy.generate_method import GenerateMethod
from regy.induction import Induction
from regy.samples import SamplesAndSemantics


class Regy:

    def __init__(self, samples, gen_method):
        self._samples = samples
        self._gen_method = gen_method
        self._re = None
        self._calculate_regex()

    def get_re(self):
        return self._re

    def _calculate_regex(self):
        if self._gen_method == GenerateMethod.SAMPLES_AND_SEMANTICS:
            self._re =  SamplesAndSemantics(self._samples).get_re()
        elif self._gen_method == GenerateMethod.COMMON_USE_CASES:
            self._re = CommonUseCases(self._samples).get_re()
        elif self._gen_method == GenerateMethod.INDUCTION:
            self._re = Induction(self._samples).get_re()
