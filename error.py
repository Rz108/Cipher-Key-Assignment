# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement error class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: error.py
#
# ------------------------------------------------------------

class Error:

    # Validate the choices
    @staticmethod
    def validate_integer(inputs, minimum, maximum):
        try:
            value = int(inputs)
            # Check whether value input is within the range
            if not int(minimum) <= int(value) <= int(maximum):
                print(f'\nOnly values between {minimum} to {maximum} are available, please try again:\n')
                return None
            return value
        # Print other errors
        except Exception as e:
            print(f'\nOnly values between {minimum} to {maximum} are available, please try again:\n')
            return None
        
    # Validate whether the encrypt or decrypt option is press
    @staticmethod
    def validate_option(self, option, valid):
        if option.lower() not in valid:
            print('Invalid option.')
            return False
        return True

    # Set the option to validate whether integer is press
    @staticmethod
    def validate_integerType(num):
        try:
            num = int(num)
            return num
        except Exception as e:
            print("Invalid input. Please enter a valid integer.")
            return None
    
    # Check text input
    @staticmethod
    def validate_text(text):
        if len(text) == 0:
            return None
        else:
            return text


