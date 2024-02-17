# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement class to generate graph
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: graph.py
#
# ------------------------------------------------------------

from .baseGraph import BaseGraph
from .sortedDict import SortedDict
from .letterFrequency import LetterFrequency
from .stack import Stack
from .topFrequency import TopFrequency
class Graph(BaseGraph):
    def __init__(self, data):
        # Create the inehritance for the text data
        super().__init__(data)
        self.data = LetterFrequency(data)

        self.data.sort()

        self.percentage_dict = LetterFrequency(data).get_percentage()
        
        self.graph_dict = self.data.getGraphData()
        
    
    # Setting the graph outer function
    def graph_outer(self):
        print('\n')
        # Setting the characters
        letters = [letter.upper() for letter in 'abcdefghijklmnopqrstuvwxyz']

        index = 0
        # Set those letters that has top 5 freq beside it
        letters_noticed = [i.upper() for i in 'klmnopq']

        # Get the top 5 frequency and put it into a stack
        top5_frequency = TopFrequency(self.percentage_dict, 5)
        top5_frequency = top5_frequency.populate()
        top5_frequency.push('-'*10)
        top5_frequency.push('top 5 freq'.upper())

        # Getting the graph, starting with total length of letters
        for i in range(len(letters) , 0 ,-1):
            row = ' '
            count = 0
            # Looping through each letters and getting their frequencies
            for letter in letters:
                frequency = self.graph_dict.get(letter, 0)
                # If frequency is more than the i index
                if int(frequency) >= i:
                    row += '*  ' # Append the star
                else:
                    row += '   ' # Append empty space
                # Increment the count
                count += 1
                # After the main graph
                if count >= len(letters):
                    # Getting the values percentage behind
                    row += f'| {letters[index]}- {self.percentage_dict[letters[index]]:.2f}%'
                    # Part of the letters that have top 5 frequency beside it\
                    if letters[index] in letters_noticed:
                        values = top5_frequency.pop()
                        # If text
                        if type(values) == str:
                            if len(row) == 88:
                                row += f'    {values}'
                                continue
                            else: 
                                row += f'   {values}' 
                                continue
                        # Add the values behind
                        if len(row) == 88: 
                            row += f'    | {values[0]}'
                            if values[1] >= 10:
                               row+= f'-{values[1]:.2f}%'
                            else: row+= f'- {values[1]:.2f}%'
                        else: 
                            row += f'   | {values[0]}'
                            if values[1] >= 10:
                               row+= f'-{values[1]:.2f}%'
                            else: row+= f'- {values[1]:.2f}%'
                        
            # Increment the index
            index += 1
            print(row)
        print('_'*79 + '|')
        print(' '+'  '.join(letters))



