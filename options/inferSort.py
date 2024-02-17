# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to infer for sorting
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: inferSort.py
#
# ------------------------------------------------------------

'''Create a infer sort class to sort the class'''
from .infer import Infer
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'tools')))
from tools import Tools
from .sortedDict import SortedDict
from .caesarCipher import CaesarCipher
import os

class InferSort:
    def __init__(self, folder, letter_freq):
        # Create the variables
        self.letter_freq = letter_freq
        self.folder = folder
        self.relative_path = os.path.join(os.getcwd(), folder)
        self.statement_dict = SortedDict()
        self.texts = []

    # Process the files
    def process_files(self):
        overall = Tools.getFiles(self.folder)
        files = overall[0]
        if len(files) == 0: return None
        if len(overall[1]) >= 1: print(overall[1])

        # For each file
        for file in files:
            # Get the file contents
            file_path = os.path.join(self.relative_path, file)
            file_contents = Tools.open_file(file_path)
            # Store it into the statement
            if file_contents:
                self._decrypt_and_store(file, file_contents)
            else: break
    
    # Decrypt and store the file
    def _decrypt_and_store(self, file_name, file_contents):
        
        # Starting the infer class
        infer_class = Infer(file_contents, self.letter_freq)
        key = infer_class.infer()
        # Producing the result after inference
        cipher_class = CaesarCipher(key)
        result = cipher_class.decrypt(file_contents)

        # Append the results
        self.texts.append(result)
        statement = f'Decrypting: {file_name} with key: {key}'
        self.statement_dict[statement] = key
        
    # Get the statements
    def get_statements(self):
        return self.statement_dict
    
    # Get the text
    def get_text(self):
        return self.texts


