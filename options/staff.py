# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program for staff object
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: staff.py
#
# ------------------------------------------------------------

from .player import Player

class Staff(Player):
    def __init__(self, name, password, score=0, level='staff'):
        # Staff object that inherits from player but with higher level
        super().__init__(name, password, score)
        self.level = level
    
