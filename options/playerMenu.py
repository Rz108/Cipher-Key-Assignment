# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to create player menu
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: playerMenu.py
#
# ------------------------------------------------------------

class PlayerMenu:
    def __init__(self, game):
        self.game = game
    # Display the menu for players
    def display_menu(self):
        while True:
            print("\nPlayer Menu:")
            print("1. Display Points")
            print("2. Play Game")
            print("3. Logout")
            choice = input("Enter your choice: ")
            # Input options here
            if choice == '1':
                self.show_score()
            elif choice == '2':
                self.game.play()
            elif choice == '3':
                self.game.login_system.logout()
                break
            else:
                print("Invalid choice. Please try again.")
    # Show the scores of the players
    def show_score(self):
        player = self.game.login_system.current_player
        if player:
            print(f"{player.get_name()}'s current score: {player.get_score()}")
        else:
            print("No player is currently logged in.")
