"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def sublist(list_one, list_two):
    """Determine whether two given lists, A and B, are equal, whether one is a sublist of the other (B contains A), whether one is a superlist of the other (A contains B), or whether they are unequal.

    Args:
        list_one (list): A random list.
        list_two (list): A random list.

    Returns:
        str: The result of analyze.
    """
    # Equal 
    if list_one == list_two:
        return EQUAL
    list_one_len = len(list_one)
    list_two_len = len(list_two)
    # Sublist
    if list_two_len > list_one_len:
        for index in range(list_two_len-list_one_len+1):
            if list_two[index:index+list_one_len] == list_one:
                return SUBLIST
    # Superlist
    if list_one_len > list_two_len:
        for index in range(list_one_len-list_two_len+1):
            if list_one[index:index+list_two_len] == list_two:
                return SUPERLIST
    return UNEQUAL
                
            
        
    