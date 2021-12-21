# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:35:32 2021

@author: MC
"""
import pandas as pd

def dict_to_df(dictionary, column_keys = 'Keys', column_values = 'Values',sort_values = False, ascend = False):
    """
    This function takes the input of a dictionary with certain parameters and returns a pandas.core.frame.DataFrame. Optional parameters for naming the columns
    and sorting the dataframe by the value column.

    Parameters
    ----------
    dictionary : dict
        Input dictionary to be turned into a dataframe
        
    column_keys : str, optional
        The desired name for the column that will contain the keys of the dictionary. The default is 'Keys'
        
    column_values : str, optional
        The desired name for the column that will contain the values of the dictionary. The default is 'Values'
        
    sort_by_values : boolean, optional 
        An option to have the resulting dataframe sorted by the values of the dictionary. The default is False
        
    ascend : boolean, optional
        An option to sort by ascending values. Default is equal to False
   

    Returns
    -------
    dict_df : pandas.core.frame.DataFrame
        Data Frame containing the dictionary keys and values as seperate columns
        
    Raises
    ------
    
    TypeError
        If the input argument data is not of type Dictionary
    TypeError
        If the input argument data is not of type str
    TypeError
        If the input argument data is not of type str
    TypeError
        If the input argument data is not of type bool
    TypeError
        If the input argument data is not of type bool
        
    Examples
    --------
    >>> dict_to_df(helper_dict,'hero','enemy_defeats',True,False)
    hero             enemy_defeats
    Thor             302
    Nick Fury        111
    Captain America  96
    ...(continued)
    """
    # Checks if a dictionary is the type of object being passed into the dictionary argument
    if not isinstance(dictionary, dict): 
        raise TypeError("The dictionary argument is not of type Dictionary")
        
    # Checks if a string is the type of object being passed into the column_keys argument
    if not isinstance(column_keys, str): 
        raise TypeError("The column_keys argument is not of type string")
        
    # Checks if a string is the type of object being passed into the column_values argument
    if not isinstance(column_values, str): 
        raise TypeError("The column_values argument is not of type string")
        
    # Checks if a boolean is the type of object being passed into the sort_values argument    
    if not isinstance(sort_values, bool):
        raise TypeError("The sort_values argument is not of type bool")
        
     # Checks if a boolean is the type of object being passed into the sort_values argument    
    if not isinstance(ascend, bool):
        raise TypeError("The ascend argument is not of type bool")
        
        
    #creates a dataframe from the dictionary
    dict_df = pd.DataFrame.from_dict(dictionary, orient = 'index')
    
    # reset the index
    dict_df = dict_df.reset_index()
    
    # assign parameter names to columns
    dict_df.columns.values[[0, 1]] = [column_keys, column_values]
    
    #Sort the dataframe by the values column
    if sort_values == True:
        dict_df = dict_df.sort_values(by = [column_values], ascending = ascend)
    
    # return the created pandas.core.frame.DataFrame
    return dict_df

