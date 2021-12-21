# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 21:17:40 2021

@author: MC
"""

import pandas as pd
import altair as alt


Disney_Characters = pd.read_csv(r"C:\Users\MC\Desktop\Coding crap\UBC data science\final project\disney-characters.csv")
Disney_Reviews_df = pd.read_csv(r"C:\Users\MC\Desktop\Coding crap\UBC data science\final project\Disney_Reviews\DisneylandReviews.csv",encoding='latin-1')

Disney_head = Disney_Reviews_df.head()

Grouped_Ratings_Counts = Disney_Reviews_df.groupby('Rating').count()

Grouped_Location_Counts =  Disney_Reviews_df.groupby('Reviewer_Location', sort=False).count()

Main_Locations_500plus = Grouped_Location_Counts[Grouped_Location_Counts.values >= 500]

Main_Locations_500plus = Main_Locations_500plus.drop_duplicates()

Reviews_by_Branch = Disney_Reviews_df.groupby('Branch').count()

Grouped_Location_Counts

Disney_Reviews_df = Disney_Reviews_df.assign(Review_Text=Disney_Reviews_df['Review_Text'].str.title())

#Creating a list from the 'Review_Text' column 
Reviews_List = list(Disney_Reviews_df['Review_Text'])

Test_List = ['My name is Mickey','My name is Mickey','My Scarve is Darth Vader']

Disney_Heros_Villians = Disney_Characters.melt(id_vars= ['movie_title'],
                                               value_vars =['hero','villian'],
                                               var_name = 'allegiance',
                                               value_name = 'character')

Character_List = list(Disney_Heros_Villians['character'])

#Remove NaN value in list
Character_List = [x for x in Character_List if str(x) != 'nan']     

#Creating a dictionary from the list with each keys value set at 0
Character_Dictionary = {character:0 for character in Character_List}


Test_Dict = {' Scar ':0,
             'Mickey':0}  
Disney_Princess_dict = {'Cinderella':0,
                             'Moana':0,
                             'Aurora':0,
                             'Ariel':0,
                             'Belle':0,
                             'Jasmine':0,
                             'Pocahontas':0,
                             'Mulan':0,
                             'Tiana':0,
                             'Rapunzel':0,
                             'Merida':0,
                             'Raya':0}

Star_Wars_Dict = {'Luke Skywalker':0,
                  'Darth Vader':0,
                  'R2':0,
                  'C3':0,
                  'Han Solo':0,
                  'Rei':0,
                  'Princess Leia':0,
                  'Storm Trooper':0,
                  'Jedi':0,
                  'lightsaber':0,
                  'Star Wars':0}

    
for key in Character_Dictionary:
    for item in Reviews_List:
        if key in item:
            Character_Dictionary[key]+= 1
            

for key in Disney_Princess_dict:
    for item in Reviews_List:
        if key in item:
            Disney_Princess_dict[key]+= 1
            
Princess_Data = pd.DataFrame.from_dict(Disney_Princess_dict, orient = 'index')

Princess_Data = Princess_Data.reset_index()

Princess_Data.columns = ['Princess','Mentions']

Princess_df = Princess_Data



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


Star_Wars_Dict = add_value_to_dict(Star_Wars_Dict,Reviews_List)

def dict_to_dataframe(dictionary,column_keys = 'Keys',column_values = 'Values',sort_values = False, descending = False):
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
        
    descending : boolean, optional
        An option to sort by descending values. Default is equal to True
   

    Returns
    -------
    dict_df : pandas.core.frame.DataFrame
        Data Frame containing the dictionary keys and values as seperate columns

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
        
    if not isinstance(sort_values, bool):
        raise TypeError("The sort_values argument is not of type bool")
        
    if not isinstance(descending, bool):
        raise TypeError("The descending argument is not of type bool")
        
    #creates a dataframe from the dictionary with desired column names
    dict_df = pd.DataFrame.from_dict(dictionary, orient = 'index')
    
    # reset the index
    dict_df = dict_df.reset_index()
    
    # assign parameter names to columns
    dict_df.columns.values[[0, 1]] = [column_keys, column_values]
    
    # if desired sort the dataframe by the values column
    if sort_values == True:
        dict_df = dict_df.sort_values(by = [column_values], ascending = descending)
        
    # return the created pandas.core.frame.DataFrame
    return dict_df


   
Star_Wars_df = dict_to_dataframe(Star_Wars_Dict,'Characters','Mentions',True)
        
Test = add_value_to_dict(Test_Dict, Test_List)
    
