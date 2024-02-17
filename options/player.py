# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to create player object
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: player.py
#
# ------------------------------------------------------------

class Player:
    def __init__(self, name, password, score = 0):
        # Player info with setting of name password and score
        self._name = name
        self.__password = password # Private variable
        self._score = score
    
    def update(self, points):
        self._score += points

    # Get password
    def get_password(self):
        return self.__password

    def get_score(self):
        return self._score
    
    def get_name(self):
        return self._name