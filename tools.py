# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to define tools 
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: tools.py
#
# ------------------------------------------------------------

import os
import re
from error import Error
class Tools:
    
    # Open file tool with validation
    @staticmethod
    def open_file( path):
        # If file has a wrong type
        if not path.endswith('.txt'):
            print(f'File with ".txt" are supported only.')
            return None
        
        # If file does not exist
        if not os.path.exists(path):
            print(f'File {path} does not exist')
            return None
        
        if os.stat(path).st_size == 0:
            print('File is empty. Please try again.')
            return None
        
        # Try opening the file
        try:
            with open(path, 'r') as f:
                return f.read()
        # Unexpected error handling
        except Exception as e:
            print('Unexpected error occured')
            return None
    
    # Set a write file method
    @staticmethod
    def write_file(path, text):
        with open(path, 'w') as f:
            f.write(text)
    
    # Open frequency file
    @staticmethod
    def open_frequency_file(file_path):
        if not file_path.endswith('.txt'):
            print(f'File with ".txt" are supported only.')
            return None

        if not os.path.exists(file_path):
            print(f'File {file_path} does not exist')
            return None

        if os.stat(file_path).st_size == 0:
            print('File is empty. Please try again.')
            return None

        pattern = re.compile(r'^[A-Z],[0-9]+(\.[0-9]+)?$')
        seen_letters = set()
        letter_freq = {}

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    clean_line = line.strip()

                    # Validate line format
                    if not pattern.match(clean_line):
                        print(f"Invalid line format: {clean_line}")
                        return None

                    letter, freq = clean_line.split(',')
                    
                    # Check for duplicate letters
                    if letter in seen_letters:
                        print(f"Duplicate letter found: {letter}")
                        return None
                    else:
                        seen_letters.add(letter)
                        letter_freq[letter] = float(freq)

            # Check if all letters A to Z are present
            if seen_letters != set("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
                print("Not all letters A to Z are present in the file.")
                return None

            return letter_freq
        except Exception as e:
            print('Unexpected error occurred:', e)
            return None

    
    # Get files from fodler
    @staticmethod
    def getFiles( folder):
        current_directory = os.getcwd()
        relative_path = f'{current_directory}\\{folder}'

        # Check whether the folder exist or not
        if not os.path.exists(relative_path):
            print(f'Folder {folder} does not exist') 
            return None
        
        # List to store file names 
        files = []
        count = 0
        files_state = ''
        for f in os.listdir(relative_path):
            file_path = os.path.join(relative_path, f)
            if os.path.isfile(file_path) and 'file' not in f and 'log' not in f and '.txt' in file_path:
                # Check if file is or is not empty
                if os.path.getsize(file_path) > 0:
                    files.append(f)
                else:
                    files_state += f'{f} '
                    

        # Check if no files found
        if not files:
            print("No valid files found in the folder.")
            return []
        files_state += 'is/are empty'
        return files, files_state
    
    @staticmethod
    def get_valid_integer(prompt):
        while True:
            user_input = input(prompt)
            valid = Error.validate_integerType(user_input)
            if valid is not None:
                return valid

    @staticmethod
    def get_ngram_freq( user_choice_n):
        if user_choice_n == 1:
            return {'th': 2.71, 'he': 2.33, 'in': 2.03, 'er': 1.78, 'an': 1.61, 're': 1.41, 'nd': 1.25, 'at': 1.12, 'on': 1.09, 'nt': 1.07}
        elif user_choice_n == 2:
            return {
                    'the': 1.81, 'and': 0.73, 'ing': 0.72, 'her': 0.63, 'tha': 0.59, 
                    'ent': 0.42, 'for': 0.34, 'thi': 0.33, 'nth': 0.33, 'ion': 0.31, 
                    'tio': 0.31, 'ere': 0.31, 'ter': 0.30, 'est': 0.28, 'ers': 0.28, 
                    'ati': 0.26, 'hat': 0.26, 'ate': 0.25, 'all': 0.25, 'eth': 0.24, 
                    'his': 0.24, 'res': 0.24, 'ver': 0.24, 'ons': 0.23, 'ith': 0.21, 
                    'oft': 0.21, 'rea': 0.21, 'int': 0.21, 'hes': 0.20, 'sth': 0.20,
                    'ere': 0.19, 'ate': 0.19, 'hat': 0.19, 'ent': 0.19, 'ion': 0.19,
                    'hin': 0.18, 'ter': 0.18, 'ati': 0.18, 'for': 0.18, 'nde': 0.17
                }