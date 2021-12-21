# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:26:43 2021

@author: MC
"""

import pandas as pd
import altair as alt
import streamlit as st

Disney_Characters = pd.read_csv("data/disney-characters.csv")
Disney_Reviews_df = pd.read_csv("data/DisneylandReviews.csv",encoding='latin-1')

Disney_Reviews_df = Disney_Reviews_df.assign(Review_Text=Disney_Reviews_df['Review_Text'].str.title())

Disney_Reviews_df = Disney_Reviews_df[Disney_Reviews_df['Rating']>= 3].drop(columns = ['Reviewer_Location','Year_Month'])

#Creating a list from the 'Review_Text' column 
Reviews_List = list(Disney_Reviews_df['Review_Text'])

Disney_Characters = Disney_Characters.rename(columns = {'villian':'villain'})

Heros_Villains = Disney_Characters.melt(id_vars= ['movie_title'],
                                        value_vars =['hero','villain'],
                                        var_name = 'allegiance',
                                        value_name = 'character')

Character_List = list(Heros_Villains['character'])

#Remove NaN value in list
Character_List = [x for x in Character_List if str(x) != 'nan']     

#Creating a dictionary from the list with each keys value set at 0
Character_Dictionary = {character:0 for character in Character_List}


#Designated Areas for app to be seperated by
header = st.container()#header region holds title, and instructions
graphs = st.container()
footer = st.container()

#Displaying title and then a little information about how to run the app 
with header:
    st.title('Welcome to my Disney Project!')
    st.markdown('This project analyzes over 40,000 reviews from Trip Advisor about Disneyland parks')
    st.text('and isolates the mentions of Disney Characters')
    st.text('Simply select the type of characters you are looking for from the dropdown menu')
    st.text('Then hit the "Visualize!" button')
    st.text('Cheers - Mark Vaz')
    st.text('Trip Advisor Review data can be found in the link below')
    st.markdown('https://www.kaggle.com/arushchillar/disneyland-reviews' ,unsafe_allow_html=True)
    
from add_value_to_dict import add_value_to_dict
from dict_to_dataframe import dict_to_df

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
                             'Merida':0,}

Star_Wars_Dict = {'Luke Skywalker':0,
                  'Darth Vader':0,
                  'R2':0,
                  'Chewbacca':0,
                  'Storm Troopers':0,
                  'Han Solo':0,
                  'Rey':0,
                  'Princess Leia':0,
                  'Storm Trooper':0,
                  'Jedi':0,
                  'Lightsaber':0}

Mickey_and_Friends_Dict = {'Mickey':0,
                           'Minnie':0,
                           'Goofy':0,
                           'Donald Duck':0,
                           'Pluto':0,
                           'Daisy Duck':0}



Disney_Princess_dict = add_value_to_dict(Disney_Princess_dict, Reviews_List)

Disney_Princesses_df = dict_to_df(Disney_Princess_dict,'Princess','Mentions',True)

Disney_Princesses_df = Disney_Princesses_df.reset_index(drop = True)

Disney_Princesses = (alt.Chart(Disney_Princesses_df, width = 600, height = 400)
                     .mark_bar()
                     .encode(x=alt.X("Princess:O", title = 'Princess Name', sort = '-y')
                             ,y= alt.Y("Mentions:Q", title = 'Number of Mentions'))
                     .properties(title = "Number of Mentions per Princess"))

Star_Wars_Dict = add_value_to_dict(Star_Wars_Dict, Reviews_List)

Star_Wars_df = dict_to_df(Star_Wars_Dict,'Character','Mentions',True)

Star_Wars_df = Star_Wars_df.reset_index(drop = True)

Star_Wars = (alt.Chart(Star_Wars_df, width = 600, height = 400)
             .mark_bar()
             .encode(x=alt.X("Character:O", title = 'Character Name', sort = '-y')
                     ,y= alt.Y("Mentions:Q", title = 'Number of Mentions'))
             .properties(title = "Number of Mentions per Character"))

Heros_Villains_dict = add_value_to_dict(Character_Dictionary, Reviews_List)

Heros_Villains_df = dict_to_df(Heros_Villains_dict,'Character','Mentions',True)

Heros_Villains_df = Heros_Villains_df.reset_index(drop = True)

Heros_Villains_df = (Heros_Villains_df[Heros_Villains_df['Mentions'] > 10]
                     #We drop rows with duplicate entries in the character column
                     .drop_duplicates(subset = ['Character'])
                       #We reset the index
                     .reset_index(drop = True))

Heros_Villains_df = Heros_Villains.merge(Heros_Villains_df, left_on = 'character', right_on = 'Character')

Heros_Villains = (alt.Chart(Heros_Villains_df, width = 600, height = 400)
                  .mark_bar()
                  .encode(x=alt.X("Character:O", title = 'Character Name', sort = '-y'),
                          y= alt.Y("Mentions:Q", title = 'Number of Mentions'),color = 'allegiance:N')
                  .properties(title = "Number of Mentions per Character"))

Mickey_and_Friends_Dict = add_value_to_dict(Mickey_and_Friends_Dict, Reviews_List)

Mickey_and_Friends_df = dict_to_df(Mickey_and_Friends_Dict,'Character','Mentions',True)

Mickey_and_Friends_df = Mickey_and_Friends_df.reset_index(drop = True)

Mickey_and_Friends = (alt.Chart(Mickey_and_Friends_df, width = 600, height = 400)
                      .mark_bar()
                      .encode(x=alt.X("Character:O", title = 'Character Name', sort = '-y'),
                              y= alt.Y("Mentions:Q", title = 'Number of Mentions'))
                      .properties(title = "Number of Mentions per Character"))
character_groups = ['Disney Princesses','Star Wars','Heros and Villains','Mickey and Friends']

character_groups_dict = {'Disney Princesses':Disney_Princesses,
                         'Star Wars':Star_Wars,
                         'Heros and Villains (UBC Project)':Heros_Villains,
                         'Mickey and Friends':Mickey_and_Friends}

character_groups_items = character_groups_dict.items()

with graphs:
    
    selection = st.selectbox('Select Character Group', character_groups)
 
 

    
    result = st.button('Visualize!')
    
    if result:
        #Iterating over cities_items assigning the designated city's URL to the variable "selected_city"   
        for characters , value in character_groups_items:
            if characters == selection:
                selected_group = value
        
        st.altair_chart(selected_group, use_container_width=True)

with footer:
    st.text('Thanks for checking out my project!')