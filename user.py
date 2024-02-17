# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement User Class
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: user.py
#
# ------------------------------------------------------------


class User:
    def __init__(self):
        # Setting the name and other infomation variable for start menu
        self.__name = None
        self.__admin_no = None
        self.__module_code = None
        self.__class = None
        self.__info = None
    
    # Settting the name of the user
    def set_name(self, name):
        self.__name = name
    
    # Setting the admin number of the user
    def set_adminNo(self, admin_no):
        self.__admin_no = admin_no
    
    # Setting the module code of this project
    def set_moduleCode(self, module_code):
        self.__module_code = module_code
    
    # Setting the class
    def set_class(self, className):
        self.__class = className
    
    # Setting the infomation
    def set_info(self, info):
        self.__info = info
    
    # Get the name of ther user
    def get_name(self):
        return self.__name
    
    # Get the admin Number
    def get_adminNo(self):
        return self.__admin_no
    
    # Get the module code
    def get_moduleCode(self):
        return self.__module_code
    
    # Get the class
    def get_class(self):
        return self.__class
    
    # Get the info
    def get_info(self):
        return self.__info
    
    # Setting the overloading print function
    def __str__(self):
        return(f"\n{'*' * 57}\n* {self.get_info()}\t*\n{'*' + '-' * 55 + '*'}\n{'*' + ' ' * 55 + '*'}\n"f"*  - Done by: {self.get_name()} ({self.get_adminNo()}){' ' * 20}*\n"f"*  - Class: {self.get_class()}{' ' * 30} *\n{'*' * 57}\n")

    

    

    
    

    

