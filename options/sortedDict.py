# ------------------------------------------------------------
# ST1507 DSAA
# CA1 Assignment
#
# Write a Python program to implement abstract data type for dictionairy that sorts itself
# 
# ------------------------------------------------------------
#
# Author: Goh Rui Zhuo
# StudentID: 2222329
# Class: DAAA/FT/2B/05
# Date: 18-Nov-2023
# Filename: sortedDict.py
#
# ------------------------------------------------------------

class SortedDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the items to be sorted
        self.sort()
    
    # Overload the set item so that the items set is sorted
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.sort()
    
    # Comparing dictionary and overloading the functions
    def __lt__(self, other):
        return self.sorted_items < other.sorted_items

    def __gt__(self, other):
        return self.sorted_items > other.sorted_items

    def __le__(self, other):
        return self.sorted_items <= other.sorted_items

    def __ge__(self, other):
        return self.sorted_items >= other.sorted_items

    def __eq__(self, other):
        return self.sorted_items == other.sorted_items

    def __ne__(self, other):
        return self.sorted_items != other.sorted_items
    
    # Set the sort function that sorts both the items and updates dicionary and local sorted items
    def sort(self):
        self.sorted_items = sorted(self.items(), key=lambda kv: (kv[1], kv[0])) # Sort by value first then key
        super().clear()
        for key, value in self.sorted_items:
            super().__setitem__(key, value)


