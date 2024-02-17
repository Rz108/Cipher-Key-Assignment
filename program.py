# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement program class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: program.py
#
# ------------------------------------------------------------
from userMenu import UserMenu
from user import User
from error import Error
from options.caesarCipher import CaesarCipher
from options.graph import Graph
from options.infer import Infer
from options.letterFrequency import LetterFrequency
from options.inferSort import InferSort
from options.login import Login
from options.games import Game
from options.staff import Staff
from options.staffMenu import StaffMenu
from tools import Tools
import os

class Program(UserMenu):
    # Create the inheritance for usermenu
    def __init__(self, config):
        super().__init__()
        self.config = config
    
    # Setting the info of the user
    def set_details(self):
        users = User()
        users.set_name(self.config['name'])
        users.set_adminNo(self.config['admin_number'])
        users.set_class(self.config['class'])
        users.set_moduleCode(self.config['module_code'])
        users.set_info(self.config['welcome_message'])
        return users
    
    # Setting the run all methods
    def run(self):
        userObj = self.set_details()

        # Setting the starting page
        print(userObj)
        while True:
            # Setting the different options
            self.choices = ['Encrypt/Decrypt Message', 'Encrypt/Decrypt File',
                            'Analyze letter frequency distribution', 'Infer caesar cipher key from file', 
                            'Analyze, and sort encrypted files', 'Caesar Cipher Game', 'NGram Analysis',  'Exit']
            press_enter =   input("\nPress enter key, to continue...\n")
            if press_enter == '' or press_enter:
                # Getting the user to input their choice
                user_choice = self.get_choice()
                if user_choice == 1:
                    self.__first()
                elif user_choice == 2:
                    self.__second()
                elif user_choice == 3:
                    self.__third()
                elif user_choice == 4:
                    self.__fourth()
                elif user_choice == 5:
                    self.__fifth()
                elif user_choice == 6:
                    self.__sixth()
                elif user_choice == 7:
                    self.__seventh() 
                elif user_choice == 8:
                    print(f'\nBye, thanks for using {userObj.get_moduleCode()} DSAA: Caesar Cipher Encrypted Message Analyzer')
                    return
        
    # Setting the funtionality of the first option
    def __first(self):
        try:
            while True:
                options = self.ask_option()
                if options == 'r':
                    return
                while not Error.validate_option(self, options, ['d','e']):
                    options = self.ask_option()            
                    if options == 'r':
                        return
                
                operation = 'encrypt' if options == 'e' else 'decrypt'

                # Ask the user to input the text
                while True:
                    text = input(f'\nPlease type text you want to {operation} ("()" to return, "**" to menu):\n')
                    # IF r is pressed
                    if text.lower() == '()':
                        break
                    if text.lower() == '**':
                        return
                    text = Error.validate_text(text)
                    if text is not None:
                        # Getting the key 
                        while True:
                            key = input(f'\nEnter the cipher key ("r" to return, "b" to menu): ')
                            if key.lower() == 'r':  
                                break
                            if text.lower() == 'b':
                                return

                            # Validation for key integer
                            key = Error.validate_integerType(key)
                            if key is not None:
                                while True:
                                    try:
                                        # Initialize the CaesarCipher with the validated key
                                        start_cipher = CaesarCipher(key)

                                        # Encrypt or decrypt based on the option selected
                                        if options == 'e':
                                            result = start_cipher.encrypt(text)
                                            message = f'Plaintext: {text}\nCiphertext: {result}'
                                        elif options == 'd':  
                                            result = start_cipher.decrypt(text)
                                            message = f'Ciphertext: {text}\nPlaintext: {result}'

                                        print(f'\n{message}')
                                        return  # Successful

                                    except Exception as e:
                                        print(f'An unexpected error occurred: {e}. Try again or enter "r" to return.')
                                        continue_choice = input("Enter any key to try again, or 'r' to return: ").lower()
                                        if continue_choice == 'r':
                                            return  # Exit the function
        except Exception as e:
            print('Error: ',e)



    # Setting the second option
    def __second(self):
        try:
            while True:
                options = self.ask_option()
                if options == 'r':
                    return
                while not Error.validate_option(self, options, ['d','e']):
                    options = self.ask_option()
                    if options == 'r':
                        return
                
                operation = 'encrypt' if options == 'e' else 'decrypt'
                
                # Ask the user to input the file
                while True:
                    file = input(f'\nPlease enter the file you want to {operation} ("r" to return, "b" to menu): ')
                    # IF r is pressed
                    if file.lower() == 'r':
                        break
                
                    if file.lower() == 'b':
                        return
                    
                    
                    # file opening
                    while Tools.open_file(file):
                        text = Tools.open_file(file)
                        # Getting the key 
                        key = ''
                        while True:
                            key = input(f'\nEnter the cipher key ("r" to return, "b" to menu): ')
                            if key.lower() == 'r':  
                                break
                            if key.lower() == 'b':
                                return
                            key = Error.validate_integerType(key)
                            if key is not None:
                                key = Error.validate_integerType(key)   
                                result = ''              
                                try:
                                    # Getting the encrytped or decrypted text
                                    start_cipher = CaesarCipher(key)
                                    # If encrypt
                                    if options == 'e':
                                        result = start_cipher.encrypt(text)
                                    # If decrypt
                                    elif options == 'd':
                                        result = start_cipher.decrypt(text)     
                                            
                                # Unexpected error handling
                                except Exception as e:
                                    print(f'An unexpected error occured {e}. Try again.')
                                
                                file = ''
                                # Writing file
                                while True:
                                    if file == 'r':
                                        break
                                    file = input(f'\nPlease enter a output file ("r" to return, "b" to menu): ')
                                    if file.lower() == 'r':
                                        break
                                    if file.lower() == 'b':
                                        return
                                    try:
                                        # Check if file path exist
                                        if os.path.exists(file):
                                            # Ask if user wants to continue
                                            while True:
                                                if file[-4:] !=  '.txt'  and file[-3:] != '.md':
                                                    print('File type not supported ')
                                                    break
                                                question = input(f'Filename {file} already exists. Do you want to overwrite it? (y/n, "r" to return, "b" to menu): ')
                                                # Return to previous input
                                                if question.lower() == 'r':
                                                    break 
                                                # Back to menu
                                                if question.lower() == 'b':
                                                    return
                                                elif question.lower() == 'n':
                                                    print("Operation cancelled.")
                                                    break   
                                                # Overwrite file
                                                elif question.lower() == 'y':
                                                    Tools.write_file(file , result)
                                                    print("File overwritten successfully.")
                                                    return  
                                                else:
                                                    print('Invalid Option')
                                                    continue
                                        # Write file
                                        else:
                                            while True:
                                                if file[-4:] !=  '.txt'  and file[-3:] != '.md':
                                                    print('File type not supported ')
                                                    break
                                                else:
                                                    Tools.write_file(file , result)
                                                    return
                                    except Exception as e:
                                        print(f"An error occurred while writing to the file: {e}")
                                        return   

                        if key == 'r':
                            break
        except Exception as e:
            print('Error: ',e)

    
    # Setting the third option here
    def __third(self):
        try: 
            while True:
                file = input(f'\nPlease enter the file you want to analyze ("r" to return): ')
                # IF r is pressed
                if file.lower() == 'r':
                    break
                # file opening
                while Tools.open_file(file):
                    text = Tools.open_file(file)
                    # Frequency analysis
                    graph_class = Graph(text)
                    graph_class.graph_outer()
                    return
        except Exception as e:
            print('Error: ',e)
    
    # Setting the fourth option here
    def __fourth(self):
        try:
            while True:
                path = input(f'\nPlease enter the file to analyze ("r" to return): ')
                # IF r is pressed
                if path.lower() == 'r':
                    break
                
                # file opening
                while Tools.open_file(path):
                    text = Tools.open_file(path)

                    # Setting the reference frequency file path
                    reference_path = input('\nPlease enter the reference frequencies file  ("r" to return, "b" to menu): ')
                    if reference_path.lower() == 'r':
                        break
                    if reference_path.lower() == 'b':
                        return
                    # References frequency file
                    file_bool = ''
                    while Tools.open_frequency_file(reference_path):
                        reference_dicts = Tools.open_frequency_file(reference_path)

                        # inference here
                        try: 
                            # Start the inference process
                            infer_class = Infer(text, reference_dicts)
                            key = infer_class.infer()
                            # Infered key produce
                            print(f'The inferred Caesar cipher key is: {key}')
                            # Ask whether user wants to decrpyt the file
                            while True:
                                file_bool = input('Would you want to decrypt this file using this key? y/n ("r" to return, "b" to menu): ')
                                if file_bool.lower() == 'r':
                                    break
                                if file_bool.lower() == 'b':
                                    return
                                elif file_bool.lower() == 'y':
                                    # Decrypt the file
                                    cipher_class = CaesarCipher(key)
                                    result = cipher_class.decrypt(text)
                                    second_res = ''
                                    for i in result:
                                        if i.lower() != 't':
                                            second_res += i
                                        else:
                                            second_res += '*'
                                    # Frequency analysis
                                    print(LetterFrequency(second_res.upper()).get_frequencies())

                                    # Getting the output file
                                    while True:
                                        file_output = input('\nPlease enter an output file ("r" to return, "b" to menu): ')
                                        if file_output.lower() == 'r':
                                            break
                                        if file_output.lower() == 'b':
                                            return
                                        # If file exist
                                        if os.path.exists(file_output):
                                            # Ask if user wants to continue
                                            while True:
                                                if file_output[-4:] !=  '.txt'  and file_output[-3:] != '.md':
                                                    print('File type not supported ')
                                                    break
                                                question = input(f'Filename {file_output} already exists. Do you want to overwrite it? (y/n, "r" to return, "b" to menu): ')
                                                if question.lower() == 'r':
                                                    break 
                                                # Back to menu
                                                if question.lower() == 'b':
                                                    return 
                                                elif question.lower() == 'n':
                                                    print("Operation cancelled.")
                                                    break   
                                                # Overwrite file
                                                elif question.lower() == 'y':
                                                    Tools.write_file(file_output , result)
                                                    print("File overwritten successfully.")
                                                    return  
                                                else:
                                                    print('Invalid Option')
                                        else:
                                            while True:
                                                if file_output[-4:] !=  '.txt'  and file_output[-3:] != '.md':
                                                    print('File type not supported ')
                                                    break
                                                else:
                                                    Tools.write_file(file_output , result)
                                                    return
                                # If user does not want to save in the file
                                elif file_bool.lower() == 'n':
                                    return

                        except Exception as e:
                            print('An unexpected error occured',e)
                            break
                        if file_bool == 'r':
                            print(file_bool)
                            break
        except Exception as e:
            print('Error: ',e)

    # Setting the method for the fifth option
    def __fifth(self):
        try: 
            while True:
                folder = input('\nPlease enter the folder name "() to return": ')
                
                if folder == '()':
                    return
                second = ''
                # Check if directory exist
                reference_path = 'englishtext.txt'
                while Tools.getFiles(folder) and folder != '':
                    x = Tools.getFiles(folder)
                    if len(x) == 0: break
                    # Validate the input freqeucny
                    while True:
                        if Tools.open_frequency_file(reference_path):
                            reference_dicts = Tools.open_frequency_file(reference_path)
                            break
                        else:
                            reference_path = input("Enter the new path of the frequency file: ")
                            continue
                    # Get the files from the folder
                    fodler = folder.lower()
                    
                    # Decrypt batch files
                    file_decrypt = InferSort(fodler, reference_dicts)
                    file_decrypt.process_files()
                    # Get the statements and key

                    sorted_dict = file_decrypt.get_statements()
                    texts = file_decrypt.get_text()
                    index = 1
                    overall = ''
                    # Define the statement for each file 
                    for key, value in sorted_dict.items():
                        statement = (key + ' as: '+f'file{index}.txt\n')
                        overall += statement
                        print(statement)

                        files = f'{folder}/file{index}.txt'
                        if os.path.exists(files):
                            # check whether filename exst
                            while True:
                                question = input(f'Filename {files} already exists. Do you want to overwrite it? (y/n, "r" to return, "b" to menu): ').lower()
                                # Back to input of question
                                if question == 'r':
                                    overall = 'r'
                                    second = 'r'
                                    break
                                # Back to menu
                                elif question == 'b':
                                    return
                                # Operation stop
                                elif question == 'n':
                                    return
                                elif question == 'y':
                                    # Writing to file
                                    Tools.write_file(files, texts[index - 1])
                                    print("File overwritten successfully.")
                                    if index >= len(list(sorted_dict.items())): break
                                    break
                                else:
                                    print('Invalid Option. Please enter y, n, or r.')
                        else:
                            Tools.write_file(files , texts[index - 1])
                            if index >= len(list(sorted_dict.items())): break
                            index += 1
                            continue
                        if overall == 'r':
                            break
                        index += 1
                    if second == 'r':
                        break
                        
                    
                    # Define the path for log txt file
                    log_path = f'{folder}/log.txt'
                    if os.path.exists(log_path):
                        # check whether filename exst
                        while True:
                            question = input(f'Filename {log_path} already exists. Do you want to overwrite it? (y/n, "r" to return, "b" to menu): ')
                            if question.lower() == 'r':
                                break 
                            if question.lower() == 'b':
                                return 
                            elif question.lower() == 'n':
                                print("Operation cancelled.")
                                break   
                            # Overwrite file
                            elif question.lower() == 'y':
                                Tools.write_file(log_path , overall)
                                return  
                            else:
                                print('Invalid Option')
                                continue
                        
                    else: 
                        Tools.write_file(log_path , overall) 
                        return
        except Exception as e:
            print('Error: ',e)

    # Set the option 6 advanced features
    def __sixth(self):
        try: 
            # Login system
            login_system = Login()
            # Create the game and staff menu
            game = Game(login_system)
            staff_menu = StaffMenu(login_system)
            # Inner menu
            while True:
                print(f"\n{'*' * 33}\n* {self.config['Game']}\t*\n{'*' + ' ' * 31 +'*'}"f"\n{'*' * 33}")
                
                # Options provided
                print("\t1. Register as Player")
                print("\t2. Login as Player")
                print("\t3. Login as Staff")
                print("\t4. Quit")

                # Input choice for user
                choice = input("\nEnter your choice : ")

                # Choice options
                if choice == '1':
                    login_system.register(staff=False)
                elif choice == '2':
                    if login_system.login(staff=False):
                        game.start() # Starting the game

                elif choice == '3':
                    if login_system.login(staff=True):
                        staff_menu.display_menu()

                elif choice == '4':
                    print("Goodbye!")
                    break
                else:
                    print("Only values between 1 to 4 are available, please try again:")
        except Exception as e:
            print('Error: ',e)

    # Set the option for the second advacned feature
    def __seventh(self):
        try: 
            while True:
                print("\nInfer Caesar Cipher Key using N-gram Analysis")
                print('Select the ways you want to analysis')

                # Getting the option from the user
                self.choices = (['file', 'text', 'return (return to main menu)'])
                user_choice_text = self.get_choice()
                if user_choice_text == 'back':
                    return 
                elif user_choice_text == 1:
                    while True:
                        # Enter the path
                        path = input('\nPlease enter the file that you want to analyse ("b" to menu): ')
                        if path.lower() == 'b':
                            return
                        # Open the file
                        while Tools.open_file(path):
                            text = Tools.open_file(path)

                            # Getting the ngram choice
                            self.choices = ['two','three']
                            print('\n')
                            user_choice_n = self.get_choice()     
                            # NGram choice 

                            # Infer the chocie
                            infer = Infer(text, Tools.get_ngram_freq(user_choice_n), user_choice_n + 1)
                            inferred_key = infer.infer(method='ngram', n = user_choice_n + 1)

                            print(f"The inferred Caesar cipher key is: {inferred_key}")

                            return
                    
                elif user_choice_text == 2:
                    while True: 
                        text = input("\nEnter the text for N-Gram Analysis: ")
                        text = Error.validate_text(text)

                        if text is not None:
                            # Getting the ngram choice
                            self.choices = ['two','three']
                            print('\n')
                            user_choice_n = self.get_choice()     
                            # Infer the chocie
                            infer = Infer(text, Tools.get_ngram_freq(user_choice_n), user_choice_n + 1)
                            inferred_key = infer.infer(method='ngram', n = user_choice_n + 1)

                            print(f"The inferred Caesar cipher key is: {inferred_key}")
                            return

                elif user_choice_text == 3:
                    return
        except Exception as e:
            print('Error: ',e)


                        
                

        





