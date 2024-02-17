# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement User Menu Class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: userMenu.py
#
# ------------------------------------------------------------

from user import User
from error import Error
class UserMenu:
    def __int__(self, choices):
        self.choices = choices
    
    # Set the choices 
    def display_choices(self):
        # Looping through to display the different options
        statements = ''
        for index, choice in enumerate(self.choices, start = 1):
            statements += (f'\t{index}. {choice}\n')
        return statements[:-1]

    # Get the choice from the user
    def get_choice(self):
        minimum, maximum = 1, len(self.choices)  
        
        # Getting the user input
        while True:
            user_input = input(f"Please select your choice: {str(tuple(range(1,len(self.choices)+1))).replace(' ', '') }\n" + self.display_choices() + '\nEnter choice: ' ).strip()

            # Validate selected option
            choice = Error.validate_integer(user_input, minimum, maximum)
            if choice is not None:
                return choice
    
    # Set the ask encrypt or decrypt option
    def ask_option(self):
        question = input('\nEnter "E" for Encrypt or "D" for Decript ("r" to return): ')
        return question

    
