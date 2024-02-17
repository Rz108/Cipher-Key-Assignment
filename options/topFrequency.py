# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement top n frequency glass
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: topFrequency.py
#
# ------------------------------------------------------------

from .stack import Stack
class TopFrequency(Stack):
    def __init__(self, percentages, n):
        # Initiliase the stack adt created
        super().__init__()
        self.stack = Stack()
        self.percentages = percentages
        self.n = n
        
    
    # Getting the top n frequency
    def populate(self):
        for key, val in list(self.percentages.items())[-self.n:]:
            self.stack.push((key, val))
        return self.stack

