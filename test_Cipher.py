import unittest
from Cipher import Cipher

class TestPatternCipher(unittest.TestCase):

      #--------Do nothing tests---------------
    def test_none_input(self):
        self.assertIsNone(Cipher.transform(None))

    def test_empty_string(self):
        self.assertEqual(Cipher.transform(""), "")

    def test_numeric_input(self):
        self.assertEqual(Cipher.transform("123"), "123")

    def test_special_characters(self):
        self.assertEqual(Cipher.transform("!@#"), "!@#")

  #------------------Palindrome test---------------
    def test_single_letter(self):
        self.assertEqual(Cipher.transform("a"), "a")

    def test_two_letter_palindrome(self):
        self.assertEqual(Cipher.transform("aa"), "aa")

    def test_palindrome_word(self):
        self.assertEqual(Cipher.transform("Level"), "Level")

    def test_palindrome_priority(self):
        self.assertEqual(Cipher.transform("noon"), "noon")

  #-----------------------Unique----------------------
    def test_two_letter_unique(self):
        self.assertEqual(Cipher.transform("ab"), "ba")

    def test_unique_letters(self):
        self.assertEqual(Cipher.transform("cat"), "atc")

  #--------------------Repeated----------------------
    def test_repeated_letters(self):
        self.assertEqual(Cipher.transform("hello"), "olleh")
        
  #---------------------Case preservation-----------------
    def test_case_preservation(self):
        self.assertEqual(Cipher.transform("Python"), "ythonP")


if __name__ == '__main__':
  print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
  unittest.main(argv=[''], verbosity=2, exit=False) #argv=[''] --> prevents unittest from trying to parse Colab’s notebook arguments