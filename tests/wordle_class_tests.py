"""
basic unittests for wordle_class
"""
import unittest

from wordlepy.wordle_class import Word

class TestWordClass(unittest.TestCase):

    def test_init(self):
        """
        test the init constructor method length requirement of 5 characters
        """
        self.assertRaises(ValueError, Word, 'foo')


    def test_check_if_solved(self):
        """
        test the "check if solved" function
        this should always return False unless a Word object
        has been solved following the prompts.
        """
        test_word = Word(word="hired")
        result = test_word.check_if_solved()
        self.assertFalse(result)