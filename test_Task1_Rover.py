'''
    Student shall write their names here
        1. Student 1
        2. Student 2
'''

import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfghjklmnpqrstvwxz" #missing g
        _UPPER_CONSTANTS = "BCDFGHJKLMNPQRSTVWXZ" #missing D
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    def setUp(self):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        self.rv = rovar()

        self.lower_consonants = "bcdfghjklmnpqrstvwxz"
        self.encode_lower = "bobcocdodfofgoghohjojkoklolmomnonpopqoqrorsostotvovwowxoxzoz"

        self.upper_consonants = "BCDFGHJKLMNPQRSTVWXZ"
        self.encode_upper = "BOBCOCDODFOFGOGHOHJOJKOKLOLMOMNONPOPQOQRORSOSTOTVOVWOWXOXZOZ"

        self.swedish_vowels_lower ="aeiouyåäö"
        self.swedish_vowels_upper ="AEIOUYÅÄÖ"

        self.numbers = "0123456789"
        self.special = "!\"#€%&/(),."

    # Example test case to check lower case rover
    def test_enrove_small(self):
      self.assertEqual(self.rv.enrove('b'), 'bob')

    # You can continue writing your test cases here based on the assignment description 

    #--------------------------Null input---------------------------------
    def test_enrove_null_input(self): #null input raises bug
      # None should raise TypeError 
      with self.assertRaises(TypeError):
        self.rv.enrove(None)
    
    def test_derove_null_input(self):
      with self.assertRaises(TypeError):
          self.rv.derove(None)

    #--------------------------Empty string---------------------------------
    def test_enrove_empty_string(self):
       #input "" --> should return ""
      self.assertEqual(self.rv.enrove(""), "")
    
    def test_derove_empty_string(self):
      self.assertEqual(self.rv.derove(""), "")

    #--------------------------Non-empty Strings---------------------------------
    #consonants sets triggered bugs as both sets missed g respective d
    #Consonants
    def test_enrove_lower_consotants(self):  
      self.assertEqual(self.rv.enrove(self.lower_consonants),self.encode_lower)
    
    def test_derove_lower_consotants(self):  
      self.assertEqual(self.rv.derove(self.encode_lower),self.lower_consonants)

    def test_enrove_upper_consotants(self):  
      self.assertEqual(self.rv.enrove(self.upper_consonants),self.encode_upper)
    
    def test_derove_upper_consotants(self):  
      self.assertEqual(self.rv.derove(self.encode_upper),self.upper_consonants)

    #Vowels
    def test_enrove_lower_vowels(self):  
      self.assertEqual(self.rv.enrove(self.swedish_vowels_lower),self.swedish_vowels_lower)

    def test_derove_lower_vowels(self):  
      self.assertEqual(self.rv.derove(self.swedish_vowels_lower),self.swedish_vowels_lower)

    def test_enrove_upper_vowels(self):  
      self.assertEqual(self.rv.enrove(self.swedish_vowels_upper),self.swedish_vowels_upper)

    def test_derove_upper_vowels(self):  
      self.assertEqual(self.rv.derove(self.swedish_vowels_upper),self.swedish_vowels_upper)

    #Numbers
    def test_enrove_numbers(self):
      self.assertEqual(self.rv.enrove(self.numbers),self.numbers)

    def test_derove_numbers(self):
      self.assertEqual(self.rv.derove(self.numbers),self.numbers)

    #Special char
    def test_enrove_special_char(self):
      self.assertEqual(self.rv.enrove(self.special),self.special)

    def test_derove_special_char(self):
      self.assertEqual(self.rv.derove(self.special),self.special)








#if __name__ == '__main__':
    #print("***********START OF All TEST CASES RESULTS SHOWN BELOW**************")
    #unittest.main(argv=[''], verbosity=2, exit=False) #argv=[''] --> prevents unittest from trying to parse Colab’s notebook arguments