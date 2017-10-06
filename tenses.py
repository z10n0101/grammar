import re

from basic import Vowel
from verbs import *



class State(object):
   # Infinitive, Negative, Question
   pass


class Tense(object):

    aux_verb = None

    def __init__(self):
        pass

    def third_person_verb(self):
        return self.verb



class PresentSimple(object):

    auxiliary_verb = AuxiliaryVerb('do')

    def third_person_verb(self):
        if self.verb.endiwth('y'):
            if not Vowel.is_vowel(self.verb[-2]):
                self.verb = re.sub(self.verb, 'y$', 'ies')

    def plural(self, verb):
        for suffix in ['o', 'ch', 'sh', 'ss', 'x', 'z']:
            if verb.word.lower().endswith(suffix):
                return verb.__class__(verb.word[:-len(suffix)] + 'es')



class PresentProgressive(object):
    pass

class SimplePast(object):
    pass
class PastProgressive(object):
    pass
class PresentPerfectProgressive(object):
    pass
class PastPerfectSimple(object):
    pass
class PastPerfectProgressive(object):
    pass
class FutureISimple(object):
    pass
class FutureIProgressive(object):
    pass
class FutureIISimple(object):
    pass
class FutureIIProgressive(object):
    pass
class ConditionalISimple(object):
    pass
class ConditionalIProgressive(object):
    pass
class ConditionalIISimple(object):
    pass
class ConditionalIIProgressive(object):
    pass
