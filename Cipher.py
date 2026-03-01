
class Cipher:

    @staticmethod
    def transform(word): 

        #None case
        if word is None:
          return None
        #Empty case
        if word =="":
          return ""
        #if word includes none alpabetic characters
        if not word.isalpha():
          return word

        word_lowercase = word.lower()

        #palindrome
        if word_lowercase == word_lowercase[::-1]:
          return word

        #Reverse repeated 
        if len(set(word_lowercase)) < len(word_lowercase):
          return word[::-1]

        #else return unique 
        return word[1:] + word[0]

        
        





