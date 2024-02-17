# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to create the staff menu
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: staffMenu.py
#
# ------------------------------------------------------------


class StaffMenu:
    def __init__(self, login_system):
        # Login system defined
        self.login_system = login_system

    # Display menu for staff
    def display_menu(self):
        while True:
            print("\nStaff Menu:")
            print("1. List All Players")
            print("2. Logout")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.login_system.list_players()
            elif choice == '2':
                self.login_system.logout()
                break
            else:
                print("Invalid choice. Please try again.")