#!/usr/bin/env python
# coding: utf-8

# In[34]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 8 14:44:33 2024
Based on: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023
Sample input: --filter="ARTIST" --value="Dua Lipa" --order_by="STREAMS" --order="ASC" --limit="6"'
@author: rivera
@author: htae
"""
import sys
import pandas as pd
import datetime as dt


def sample_function(input: str) -> str:
    """Sample function (removable) that shows good use of documentation.
            Parameters
            ----------
                input : str, required
                    The input message.

            Returns
            -------
                str
                    The text returned.
    """
    return input.upper()

def readFile(data: str) -> pd.DataFrame:
    """
    Open and load the data in a csv file into pandas DataFrame
            Parameters
            ----------
                data : str, required
                    The name of the csv file.

            Returns
            -------
                pd.DataFrame
                    The loaded dataframe
    """
    songs_df: pd.DataFrame = pd.read_csv(data)
    return songs_df
        
def filterRows(songs_df: pd.DataFrame, criteria: str, value: str) -> pd.DataFrame:
    """
    For the questions with 'filter', filter the data according to the value given
            Parameters
            ----------
                songs_df : pd.DataFrame, required
                    The dataframe with all the data from the csv file
                criteria : str
                    The 'filter' text. Specifies the column in question.
                value : str
                    The 'value' text. Gives the certain value to filter by.

            Returns
            -------
                pd.DataFrame
                    The filtered or not filtered dataframe.
    """
    if criteria is None:
        return songs_df
    else:
        if criteria == 'ARTIST':
            songs_df = songs_df[songs_df['artist(s)_name'].str.contains(value)]
        elif criteria == 'YEAR':
            songs_df = songs_df[songs_df['released_year'].astype(int) == int(value)]
        return songs_df

def sortInOrder(df : pd.DataFrame , col : str, order : str, limit : str) -> pd.DataFrame:
    """
    Sort the data in ascending/descending order based on the given column. If limit is not null, leaves 
    only the first 'limit' rows.
            Parameters
            ----------
                df : pd.DataFrame, required
                    The input dataframe
                col : str
                    Specifies the column to look into
                order : str
                    Specifies whether in ascending or descending order
                limit : str
                    Limits the number of rows to include

            Returns
            -------
                pd.DataFrame
                    Returns the modified, sorted dataframe.
    """
    if col == 'STREAMS':
        col = 'streams'
    elif col == 'NO_SPOTIFY_PLAYLISTS':
        col = 'in_spotify_playlists'
    elif col == 'NO_APPLE_PLAYLISTS':
        col = 'in_apple_playlists'
    
    order_to_num = True
    if order == 'DES':
        order_to_num = False
    
    if limit is None:
        return df.sort_values(by = col, ascending = order_to_num)
    else:
        return df.sort_values(by = col, ascending = order_to_num).head(int(limit))
    
def mergeDate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge the columns 'released_year', 'released_month', 'released_day' to one column 'released'
    Format text in "weekday, Month day, Year"
    Drop the separate columns after use
            Parameters
            ----------
                df : pd.DataFrame
                    The input dataframe

            Returns
            -------
                pd.DataFrame
                    The modified dataframe
    """
    date_df = pd.DataFrame({'year': df['released_year'].astype(int),
                   'month': df['released_month'].astype(int),
                   'day': df['released_day'].astype(int)})
    df['released'] = pd.to_datetime(date_df).dt.strftime("%a, %B %d, %Y")
    df.drop(['released_year', 'released_month', 'released_day'], inplace = True, axis = 1)
    return df


def main():
    """Main entry point of the program."""
    # Get argument
    args = {}
    for i in sys.argv[1:]:
        key, value = i.split("=")
        args[key.strip("-")] = value.strip("\"")
    
    # calling the sample function
    songs_df = readFile(args.get('data'))
    songs_df = filterRows(songs_df, args.get('filter'), args.get('value'))
    songs_df = sortInOrder(songs_df, args.get('order_by'), args.get('order'), args.get('limit'))
    if args.get('order_by') == 'NO_SPOTIFY_PLAYLISTS':
        songs_df.drop(['artist_count', 'streams', 'in_apple_playlists', 'bpm', 'key', 'mode', 
'danceability_%'], inplace = True, axis = 1) # drop unnecessary columns
        songs_df = mergeDate(songs_df)
        songs_df = songs_df[['released','track_name','artist(s)_name',
'in_spotify_playlists']] # reorder the columns
    elif args.get('order_by') == 'NO_APPLE_PLAYLISTS':
        songs_df.drop(['artist_count', 'in_spotify_playlists', 'streams', 'bpm', 'key', 'mode', 
'danceability_%'], inplace = True, axis = 1)
        songs_df = mergeDate(songs_df)
        songs_df = songs_df[['released','track_name','artist(s)_name',
'in_apple_playlists']]
    else:
        songs_df.drop(['artist_count', 'in_spotify_playlists', 'in_apple_playlists', 'bpm', 'key', 'mode', 
'danceability_%'], inplace = True, axis = 1)
        songs_df = mergeDate(songs_df)
        songs_df = songs_df[['released','track_name','artist(s)_name',
'streams']]
    songs_df.to_csv('output.csv',index=False) # write to csv file


if __name__ == '__main__':
    main()

