# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to run the program
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: main.py
#
#
# To run: python main.py
# ------------------------------------------------------------


from program import Program
from config import Configuration

# This is to run the program with main.py
if __name__ == "__main__":
    program = Program(Configuration)
    program.run()