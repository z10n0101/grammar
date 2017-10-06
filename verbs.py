from grammar.basic import Word


class Verb(Word):
    """
        A word used to describe an action, state, or occurrence, and forming 
        the main part of the predicate of a sentence, such as hear, become, 
        happen.
    """

    def __init__(self, word):
       self.word = word

    @classmethod
    def plural(tense, verb):
        return tense.plural(verb)


class ActionVerb(Verb):
    """
        Action verbs express specific actions, and are used any time you want 
        to show action or discuss someone doing something. 
    """
    pass


class TransitiveVerb(ActionVerb):
    """
        Transitive verbs are action verbs that always express doable 
        activities. These verbs always have direct objects, meaning 
        someone or something receives the action of the verb.
    """
    pass


class IntransitiveVerb(ActionVerb):
    """
        Intransitive verbs are action verbs that always express doable 
        activities. No direct object follows an intransitive verb.
    """
    pass


class AuxiliaryVerb(Verb):
    """ 
        Auxiliary Verbs are the verbs be, do, have, will - when they are
        followed by another verb (the full verb) in order to form a question, 
        a negative sentence, a compound tense or the passive.
    """ 
    verbs = ['be', 'do', 'have', 'will']

    def __init__(self, verb):
        if verb not in self.verbs:
            return VerbError()
        return Verb(verb)



class ModalAuxiliaryVerb(Verb):
    """
        Modal verbs are auxiliary verbs that are used to express abilities, 
        possibilities, permissions, and obligations. 
    """
    
    verbs = ['can', 'could', 'may', 'might', 'must', 'ougth to', 'shall', 
            'should', 'will', 'would']


class StativeVerb(Verb):
    """
        Stative verbs are verbs that express a state rather than an action. 
        They usually relate to thoughts, emotions, relationships, senses, 
        states of being and measurements.
    """
    pass


class PhrasalVerb(Verb):
    """
        A phrasal verb is a combination of words 
        (a verb + a preposition or verb +adverb) that when used together, 
        usually take on a different meaning to that of the original verb.
    """
    pass


class IrregularVerb(Verb):
    """
        Irregular verbs are those that don't take on the regular spelling 
        patterns of past simple and past participle verbs. 
    """
    pass


class VerbError(Exception):
    pass


class PluralVerbRule(Rule):

    suffixes = ['o', 'ch', 'sh', 'ss', 'x', 'z']

    def rule(cls, verb):
       cls.suffix_replace(suffixes, 'es')




        
