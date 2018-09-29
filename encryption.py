import numpy as np
from nltk.corpus import words
class Cipher():
    def __init__(self):
        '''this method initializes the Ciher class with only alphabet field'''
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.specials = ['.',',','?','!',';',':']
    
    def encrypt(self, message, key=0):
        '''this method encrypts the message using the key as caesar cipher'''
        message = message.lower()
        words = message.split()
        new_sentence = ''
        # here the message was split into words an a new_sentence variable was created
        for word in words:
            new_word = ''
            word_array = np.arange(0,len(word))
            # this makes a new_word variable and an array containing the indices of the word's characters
            for letter in word_array:
                # this finds the index of each character in the alphabet and subtracts the key from it.
                # Then the new letter is added to the new word
                if word[letter] in self.specials:
                    new_word += word[letter]
                    continue
                ind = self.alphabet.index(word[letter])
                ind += key
                if ind > len(self.alphabet)-1:
                    ind -= len(self.alphabet)
                new_word += self.alphabet[ind]
            new_sentence += new_word + ' '
        return new_sentence
    
    def decrypt(self, message, key):
        '''this method decrypts the message using the key as caesar cipher'''
        message = message.lower()
        words = message.split()
        new_sentence = ''
        for word in words:
            new_word = ''
            word_array = np.arange(0,len(word))
            for letter in word_array:
                if word[letter] in self.specials:
                    new_word += word[letter]
                    continue
                ind = self.alphabet.index(word[letter])
                ind -= key
                if ind > len(self.alphabet)-1:
                    ind -= len(self.alphabet)
                new_word += self.alphabet[ind]
            new_sentence += new_word + ' '
        return new_sentence
    
    
class Breaker():
    def __init__(self):
        self.vowels = "aeiouy"
        
    def brute_force(self, message, use_dict=True): 
        message = message.lower()
        '''this method tries every key to find the most likely sentences 
        and then it returns them'''
        # this lowers the message and creates an list of the possible keys
        message = message.lower()
        possible_keys = np.arange(1,26)
        possible_messages = []
        cipher = Cipher()
        for key in possible_keys:
            # this creates a decrypted message for each key and if self.is_real_sentence returns true the decryption
            #  is added to the possible translations list
            dec_mess = cipher.decrypt(message,key)
            if self.is_real_sentence(dec_mess,use_dict):
                possible_messages.append(dec_mess)    
        return possible_messages
    
    
    def is_real_sentence(self, sentence, use_dict=True):
        sentence = sentence.lower()
        '''this method will return trues if it is likely that the passed 
        sentence is most likely a real english sentence'''
        words = sentence.split()
        real_words = 0
        for word in words:
            if self.is_real_word(word,use_dict):
                real_words += 1
        percent_real = float(real_words / len(words))
        if percent_real >= 0.8:
            return True
        else:
            return False
        
        
    def is_real_word(self, word, use_dict=True):
        if use_dict:
            if word in words.words():
                return True
            else:
                return False
        word = word.lower()
        letters = list(word)
        for letter in letters:
            ind = letters.index(letter)
            tests = [ind-2,ind-1,ind]
            if tests[0] < 0:
                tests.pop(0)
            if tests[1] < 0:
                tests.pop(1)
            num_vowels = 0
            for test in tests:
                if letters[test] in self.vowels:
                    num_vowels += 1
            if num_vowels > 2:
                return False
        return True
