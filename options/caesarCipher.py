# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement Caesar Cipher class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: caesarCipher.py
#
# ------------------------------------------------------------

from .baseCipher import BaseCipher
class CaesarCipher(BaseCipher):
    def __init__(self, shift):
        super().__init__()
        # Create the inheritance with the cipher class
        self.__shift = shift 
        self._hints_given = 0

    # Define the encrpt method
    def encrypt(self, text):
        return self.__transform_text(text, self.__shift)

    # Define the decrypt method
    def decrypt(self, text):
        return self.__transform_text(text, -self.__shift)   
    
    # Define the private transform class method
    def __transform_text(self, text, value):
        trnasform_strings = ''
        for i in text:
            # Check whether it is alphabet
            if not i.isalpha():
                trnasform_strings += i
                continue
            
            # If uppercase, we take the remainder + 65
            if i.isupper():
                order_c = (ord(i) + value - 65) % 26 + 65
            
            # If lowercase, we take the remainder + 97
            else:
                order_c = (ord(i) + value - 97) % 26 + 97

            # Conert it to character and append into the string
            trnasform_strings += chr(order_c)
        return trnasform_strings
    
    # Hint option for user to get hint maximum 5
    def get_hint(self):
        self._hints_given += 1
        if self._hints_given == 1:
            return f"The Caesar Cipher shifts letters by a certain number in the alphabet.", 1
        elif self._hints_given == 2:
            return f"The shift value is between 1 and 26.", 1
        elif self._hints_given == 3:
            return f"The shift value is between {self._shift // 2} and {self._shift * 2} (not exact range).", 1
        else:
            return f"The exact shift value is {self._shift}.", 1
