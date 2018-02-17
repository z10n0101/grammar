import re

from basic import Vowel
from verbs import *



class State(object):
   # Infinitive, Negative, Question
   pass


class Tense(object):

    auxiliary_verb = None
    exceptions = {}

    def __init__(self):
        pass

    def third_person_verb(self):
        return self.verb


class PresentSimpleTense(object):

    auxiliary_verb = AuxiliaryVerb('do')
    exceptions = {
        'have': 'has'
    }

    def third_person_verb(self, verb):
        _verb = str(verb)
        if _verb in self.exceptions:
            _verb = self.exceptions[_verb]
        elif _verb.endswith('y'):
            if not Vowel.is_vowel(_verb[-2]):
                _verb = re.sub('y$', 'ies', _verb
                               )
            else:
                _verb += 's'
        else:
            for suffix in ['o', 'ch', 'sh', 'ss', 'x', 'z']:
                if _verb.lower().endswith(suffix):
                    _verb += 'es'
                    break
        return verb.__class__(_verb)


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
