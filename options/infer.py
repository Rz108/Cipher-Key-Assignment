# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to infer for inference
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: infer.py
#
# ------------------------------------------------------------

from .letterFrequency import LetterFrequency
from .caesarCipher import CaesarCipher
from .sortedDict import SortedDict
from .NGram import NGramFrequency

class Infer:
    def __init__(self, data, letter_frequency, n=None):
        # Define all the variables
        self.data = data
        self.letter_size = 26
        self.letter_frequency  = letter_frequency
        self.n = n

    # Infer method
    def infer(self, method='frequency', n = None):
        if method == 'frequency':
            return self.__infer_using_frequency()
        elif method == 'ngram':
            return self.__infer_using_ngram(n)
    
    # Infer with frequency
    def __infer_using_frequency(self):
        # Setting the lowest difference 
        lowest_dif = float('inf')
        key = 0
        for i in range(1, self.letter_size + 1):

            # Temporary word with difference
            temp_original = CaesarCipher(i).encrypt(self.data)
            temp_dif = self.__difference_frequency(temp_original)

            # Check whether is it lower than the current diference 
            if temp_dif < lowest_dif:
                lowest_dif = temp_dif
                key = i
        # Return positive key
        return self.letter_size - key

    # Infer with ngram analysis
    def __infer_using_ngram(self, n):
        key = 0
        # Define the similarity score
        max_similarity = 0
        for shift in range(26):
            # Negative shift for decoding
            temp_original = CaesarCipher(shift).encrypt(self.data) 
            similarity = self.__similarity_score_ngram(temp_original, n)
            # if similartiy is greater than what is the current similarity
            if similarity > max_similarity:
                max_similarity = similarity
                key = shift
         # Return positive key
        
        if key == 0:
            return 0
        return self.letter_size - key

    # Getting the difference here
    def __difference_frequency(self, text):
        given_frequency = LetterFrequency(text.upper()).get_percentage()
        difference = {}
        sums = 0
        for letter in self.letter_frequency:
            difference[letter] = given_frequency.get(letter, 0) - self.letter_frequency[letter]
            sums += abs(difference[letter] / 26)
        return sums

    # Extract the ngrams text
    def __get_ngrams(self,text, n):
        filtered_text = ''.join([char.lower() for char in text if char.isalpha()])
        return [filtered_text[i:i+n] for i in range(len(filtered_text)-n+1)]
    
    # Similarity score for ngram
    def __similarity_score_ngram(self, text, n):
        # Getting the shifted ngrams
        shifted_bigrams = self.__get_ngrams(text, n)
        # Getting the frequency
        shifted_freq = NGramFrequency(shifted_bigrams, self.n)._get_frequency(shifted_bigrams)
        # sum the shifted bigrams

        total_shifted_bigrams = sum(shifted_freq.values())
        # Getting the similarity score
        similarity = sum(shifted_freq[bg]  * self.letter_frequency.get(bg, 0) for bg in shifted_freq)
        return similarity
