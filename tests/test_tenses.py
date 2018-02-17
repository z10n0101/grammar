import unittest

from tenses import *
from verbs import *


class TestPresentSimpleTense(unittest.TestCase):

    def test_third_person_verb(self):
        words = {
            'go': 'goes',
            'do': 'does',
            'teach': 'teaches',
            'wash': 'washes',
            'kiss': 'kisses',
            'fix': 'fixes',
            'cry': 'cries',
            'fly': 'flies',
            'play': 'plays',
            'stay': 'stays',
            'have': 'has'
         }
        for a, b in words.items():
            tense = PresentSimpleTense()
            self.assertEqual(str(tense.third_person_verb(Verb(a))), b)

