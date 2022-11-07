import pandas as pd
import numpy as np


def load_and_process(path_to_csv):
    '''
    This function will load, process, and sort data. Columns will also be reformatted appropriately for arrests data.
    
    '''
    
    #Method Chain 1 for loading, sorting, and renaming columns within dataset
    loaddf = (pd.read_csv("..\\data\\raw\\arrests.csv", sep=',')
    .copy().drop(['home_team', 'away_team', 'home_score', 'away_score', 'OT_flag', 'division_game'],axis=1))
    loaddf.sort_values(by=['season', 'day_of_week'],inplace=True)
    loaddf.rename(columns={'day_of_week':'Day of Week','week_num':'Week Number','gametime_local': 'Gametime Local', 
                        'arrests':'Arrests', 'season':'Season'},inplace = True)
    
    #Method Chain 2 converting NaN variables to 0 int values.
    finaldf = loaddf['Arrests'] = loaddf['Arrests'].fillna(0)
    return (loaddf)
    