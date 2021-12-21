# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:30:55 2021

@author: MC
"""


def add_value_to_dict(a_dict,a_list):
    """
    This function takes the input of a dictionary in which all keys have an integer value, and a list of strings. 
    It then iterates over the dictionary checking for each time the name of a specific key is mentioned in every item in the list
    If the key is found it adds 1 to the value of the key. Then returns the updated dictionary

    Parameters
    ----------
    a_dict : Dictionary
        A dictionary in which each key's value is an integer.
    a_list : List
        A list of strings

    Returns
    -------
    a_dict : Dictionary
        An updated dictionary.

    """
    # Checks if a dictionary is the type of object being passed into the a_dict argument
    if not isinstance(a_dict, dict): 
        raise TypeError("The a_dict argument is not of type Dictionary")
        
    # Checks if a list is the type of object being passed into the a_list argument
    if not isinstance(a_list, list): 
        raise TypeError("The a_list argument is not of type list")
        
    # Tests that every value in the dictionary is of the type int    
    for key in a_dict:
        if not isinstance(a_dict[key], int):
            raise TypeError("Not all key values are integers")
            
    # Tests that every item in the list is of the type str
    for item in a_list:
        if not isinstance(item, str):
            raise TypeError("Not all items in list are strings")
            
            
    #Through nested 'for' loops we can count the mentions. 
    for key in a_dict:
       #for every dictionary key iterate through the list
            for item in a_list:  
          #for every item if the key is present in it, add 1 to the value of the key
          #important to use ' '+key+' ' to avoid words like Scary counting for the name Scar!
                if (' '+key+' ') in item:
                    a_dict[key]+=1
    
    #returns dictionary with updated values
    return a_dict