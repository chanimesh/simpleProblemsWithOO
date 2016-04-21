from unittest import TestCase
from src.ReverseSentence import ReverseSentence


class TestReverseSentence(TestCase):
    def setUp(self):
        self.reverse = ReverseSentence()

    # def test_splitSentence_with_single_spaces(self):
    #     self.assertEqual(self.reverse.splitSentence("this is a sentence"),["this","is","a","sentence"])
    #
    # def test_splitSentence_with_multiple_spaces(self):
    #     self.assertEqual(self.reverse.splitSentence("this  is a sentence"), ["this", "is", "a", "sentence"])
    #
    # def test_reverseList(self):
    #     self.assertEqual(self.reverse.reverse_list(["this", "is", "a", "sentence"]), ["sentence", "a", "is", "this"])
    #
    # def test_joinList(self):
    #     self.assertEqual(self.reverse.join_list(["this", "is", "a", "sentence"]), "this is a sentence")

    def test_reverseSentence_singlespaces(self):
        self.assertEqual(self.reverse.reverseSentence("this is a sentence"),"sentence a is this")

    def test_reverseSentence_multiplespaces(self):
        self.assertEqual(self.reverse.reverseSentence("this   is a sentence"),"sentence a is this")

    def test_reverseSentence_spaces_begining(self):
        self.assertEqual(self.reverse.reverseSentence(" this is a sentence"), "sentence a is this")

    def test_reverseSentence_spaces_end(self):
        self.assertEqual(self.reverse.reverseSentence("this is a sentence  "), "sentence a is this")
