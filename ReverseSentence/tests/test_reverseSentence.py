from unittest import TestCase
from src.ReverseSentence import ReverseSentence


class TestReverseSentence(TestCase):

    def test_splitSentence_with_single_spaces(self):
        reverse = ReverseSentence()
        self.assertEqual(reverse.splitSentence("this is a sentence"),["this","is","a","sentence"])

    def test_splitSentence_with_multiple_spaces(self):
        reverse = ReverseSentence()
        self.assertEqual(reverse.splitSentence("this  is a sentence"), ["this", "is", "a", "sentence"])

    def test_reverseList(self):
        reverse = ReverseSentence()
        self.assertEqual(reverse.reverse_list(["this", "is", "a", "sentence"]), ["sentence", "a", "is", "this"])

