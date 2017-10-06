import re


class Letter(object):

    letter_re = re.compile(r'^[a-zA-Z]$')

    def __init__(self, letter):
        if letter_re.match(letter):
            if Vowel.is_vowel(letter):
                self.letter = Vowel(letter)
            else:
                self.letter = Consonant(letter)
        else:
            raise LetterException()


class Vowel(object):
    letters = ['a', 'e', 'i', 'o', 'u']
    # TODO: 'y' is a special case

    def __init__(self, letter):
        self.value = letter

    @staticmethod
    def is_vowel(letter):
        return letter in letters


class Consonant(object):

    def __init__(self, letter):
        self.value = letter

    @staticmethod
    def is_consonant(letter):
        return not Vowel.is_vowel(letter)


class Word(object):

    def __init__(self, word):
        self.word = word

    def split_letters(self):
        pass

class Rule(object):

    @classmethod
    def suffix_replace(word, suffixes, relpace):
        for suffix in suffixes:
            if word.lower().endswith(suffix):
                return verb.__class__(word[:-len(suffix)] + 'es')
        return None




