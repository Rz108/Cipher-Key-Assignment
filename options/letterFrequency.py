# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement class for letter frequency with inheritance
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: letterFrequency.py
#
# ------------------------------------------------------------

from .sortedDict import SortedDict
''' Create a letter frequency class '''
class LetterFrequency(SortedDict):
    def __init__(self, text=None):
        # Create the inheritance with the sorted dictionary
        super().__init__()
        # Create the letters 
        self.letters = [letter.upper() for letter in 'abcdefghijklmnopqrstuvwxyz']
        
        for letter in self.letters:
            self[letter] = 0
        
        if text:
            self._analyse(text)

    def _analyse(self, text):
        for letter in text:
            if letter.isalpha():
                letter = letter.upper()
                if letter in self:
                    self[letter] += 1
    
    # Get the sorted percentage here
    def get_percentage(self):
        total_count = sum(self.values())
        # Initialise the sorted Dict
        percentage_dict = SortedDict()
        for letter, freq in self.items():
            percentage = (freq / total_count) * 100 if total_count > 0 else 0
            percentage_dict[letter] = percentage
        return percentage_dict

    # Get the data suitable for the graph frequency analysis
    def getGraphData(self):
        graph_dicts = SortedDict()
        for letter, frequency in self.get_percentage().items():
            graph_dicts[letter] = int(frequency*(26/100)) + ((frequency * (26/100)) % 1 > 0)
        return graph_dicts

    # Get the frequency
    def get_frequencies(self):
        return dict(self)