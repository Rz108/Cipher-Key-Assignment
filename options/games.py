# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to create a game with caesar cipher
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: games.py
#
# ------------------------------------------------------------


from .caesarCipher import CaesarCipher
from .login import Login
from .player import Player
from .staff import Staff
from .playerMenu import PlayerMenu
from .staffMenu import StaffMenu
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'error')))
from error import Error
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'tools')))
from tools import Tools
import threading
import random
import time

class Game(CaesarCipher, Login):  
    # The cipher game with inheritance
    def __init__(self, login_system):
        CaesarCipher.__init__(self, random.randint(1, 25))
        Login.__init__(self)
        self.time_limit = 60
        self.time_left = self.time_limit
        self.over = False
        self.level = 1
        self.login_system = login_system
        
    # List all the players here but only staff can
    def list_all_players(self):
        if isinstance(self.login_system.current_player, Staff):
            self.login_system.list_players()
        else:
            print("Only staff members can view all players.")
    
    # Show the scores of the current player
    def show_score(self):
        if self.login_system.current_player:
            print(f"{self.login_system.current_player.name}'s current score: {self.login_system.current_player.get_score()}")
        else:
            print("No player is currently logged in.")

    # Select the shift
    def select(self):
        self._shift = random.randint(1, 25)  
        self.time_limit = max(60 - 5 * (self.level - 1), 10)
        self.time_left = self.time_limit
    # Counting down the clock
    def count(self):
        for i in range(self.time_limit, -1 , -1):
            self.time_left = i
            if self.over:
                return
            time.sleep(1)
        
        self.over = True
        print('\n Unfortunately, the time is up!')
        self.login_system.current_player.update(-5)
        print(f'Score will be reduced. Your current score is: {self.login_system.current_player.get_score()}')

    # Game for user to play
    def play(self):
        self.over = False
        self.select()
        while True:
            count_limit = Tools.get_valid_integer('Enter the desired number of words: ')
            min_word = Tools.get_valid_integer('\nEnter the minimum word length you want: ')        
            max_word = Tools.get_valid_integer('\nEnter the maximum word length you want: ')  

            # Original text
            original_text = self.generate_random_message(count_limit, min_word, max_word)   
            encrypt = self.encrypt(original_text)
            print(f'Encrypted text is: {encrypt}')
            print(f'\nYou have {self.time_limit} seconds to solve this.')
            self.timer_thread = threading.Thread(target = self.count)
            self.timer_thread.start()
            hint_count = 0
            # The while loop for when the game is not over
            while not self.over:
                user = input(f"Time left: {self.time_left}s. Enter your answer', 'hint' for a hint, or 'answer' to reveal the answer: ")
                # If user wants a hint
                if user == 'hint':
                    if hint_count >= 4:
                        print('Hint used up answer is:', original_text)
                        self.login_system.current_player.update(-1)
                        self.login_system.store_user()
                        self.over = True
                    else:
                        hint_message, penalty = self.get_hint()
                        print(hint_message)
                        self.login_system.current_player.update(-penalty)
                        self.login_system.store_user()
                        self.over = False
                        hint_count += 1
                        continue
                # User gives up in answeing
                elif user == 'answer':
                    print('Answer', original_text)
                    self.login_system.current_player.update(-5)
                    self.login_system.store_user()
                    self.over = True
                # If user got it correctly
                else:
                    if user == original_text.lower():
                        print(f'Correct! You solved the question in {self.time_limit - self.time_left} seconds. 10 points gained')
                        self.login_system.current_player.update(10)
                        self.login_system.store_user()
                        self.over = True

                    else:
                        print('Incorrect. Try Again!')
                        self.over = False
                        continue
                    # If time is up
                    if self.time_left <= 0:
                        print('The time is up. ')
                        self.over = True
                        break
                    
                self.timer_thread.join()
                return
        

    # Generate random count
    def generate_random_message(self, word_count, min_word_length, max_word_length):
        words = ["secret", "hidden", "encrypt", "decode", "cipher", "message", "privacy", "security", "code"]
        popssible_words = [word for word in words if min_word_length <= len(word) <= max_word_length]
        
        if not popssible_words:
            print("No words found for the given length, random selecting...")
            popssible_words = words
        
        generated_words = random.choices(popssible_words, k=word_count)
        return ' '.join(generated_words)

    # Start the menu for player
    def start(self):
        player_menu = PlayerMenu(self)
        player_menu.display_menu()
