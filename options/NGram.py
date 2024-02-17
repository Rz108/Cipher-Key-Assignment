# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to ngram for analysis
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: NGram.py
#
# ------------------------------------------------------------

from .sortedDict import SortedDict
class NGramFrequency(SortedDict):
    def __init__(self, text, n):
        # Create the inheritance for sorted dictionary
        super().__init__()
        self.text = text
        self.n = n
        if text:
            self.analyse(text)
    
    # The analyse portion for the text
    def analyse(self, text):
        filtered_text = ''.join([char.upper() for char in text if char.isalpha()])  # Keep only alphabetic characters
        for i in range(len(filtered_text) - self.n + 1):
            ngram = filtered_text[i:i+self.n]
            if len(ngram) == self.n:
                if ngram in self:
                    self[ngram] += 1
                else:
                    self[ngram] = 1

    # Getting the frequency for the ngrams
    def _get_frequency(self, ngrams):
        for ngram in ngrams:
            if ngram in self:
                self[ngram] += 1
            else:
                self[ngram] = 1
        return self
    
    # Getting the ngrams base on n
    def _get_ngrams(self, text, n):
        return [text[i:i+n] for i in range(len(text)-n+1)]