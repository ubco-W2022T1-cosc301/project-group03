import pandas as pd
import numpy as np


def load_and_process(path_to_csv):
    '''
    This function will load, process, and sort data. Columns will also be reformatted appropriately for arrests data.
    
    '''
    
    #Method Chain 1 for loading, sorting, and renaming columns within dataset
    loaddf = (pd.read_csv('../data/raw/arrests.csv', sep= ",").copy().drop(['week_num', 'day_of_week', 'gametime_local', 'home_score', 'away_score', 'division_game'], axis = 1))
    loaddf.sort_values(by = ['season', 'OT_flag'], inplace = True)
    loaddf.rename(columns = {'home_team':'Home Team','away_team':'Away Team','OT_flag': 'Overtime (OT)', 
                        'arrests':'Arrests', 'season':'Season'}, inplace = True)
    loaddf.head()
    
    #Method Chain 2 converting NaN variables to 0 int values.
    finaldf = loaddf
    finaldf['Arrests'] = finaldf['Arrests'].fillna(0)
    finaldf.head()