import unittest
from Cipher import Cipher

class TestPatternCipher(unittest.TestCase):


    # CLASS 1 — None Input
    def test_none_input(self):
        self.assertIsNone(Cipher.transform(None))

    # CLASS 2 — Empty String
    def test_empty_string(self):
        self.assertEqual(Cipher.transform(""), "")

    # CLASS 3 — Numbers
    def test_numeric_input(self):
        self.assertEqual(Cipher.transform("123"), "123")

    # CLASS 4 — Special Characters
    def test_special_characters(self):
        self.assertEqual(Cipher.transform("!@#"), "!@#")

    # CLASS 5 — Single Letter (Palindrome Boundary)
    def test_single_letter(self):
        self.assertEqual(Cipher.transform("a"), "a")

    # CLASS 6 — Two-Letter Palindrome
    def test_two_letter_palindrome(self):
        self.assertEqual(Cipher.transform("aa"), "aa")

    # CLASS 7 — Two-Letter Unique
    def test_two_letter_unique(self):
        self.assertEqual(Cipher.transform("ab"), "ba")

    # CLASS 8 — Multi-Letter Palindrome
    def test_palindrome_word(self):
        self.assertEqual(Cipher.transform("level"), "level")

    # Conflict Case: Palindrome + Repeated Letters
    def test_palindrome_priority_over_repeated(self):
        self.assertEqual(Cipher.transform("noon"), "noon")

    # CLASS 9 — Repeated Letters (Not Palindrome)
    def test_repeated_letters(self):
        self.assertEqual(Cipher.transform("hello"), "olleh")

    # CLASS 10 — Unique Letters
    def test_unique_letters(self):
        self.assertEqual(Cipher.transform("cat"), "atc")

    # CLASS 11 — Case Preservation
    def test_case_preservation(self):
        self.assertEqual(Cipher.transform("Python"), "ythonP")


if __name__ == '__main__':
  print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
  unittest.main(argv=[''], verbosity=2, exit=False) #argv=[''] --> prevents unittest from trying to parse Colab’s notebook arguments