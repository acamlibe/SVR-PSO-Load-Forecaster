import sys
import numpy as np
import pandas as pd

args = sys.argv

file_path = args[1]
output_path = args[2]

df = pd.read_csv(file_path)

df.drop(['datetime_beginning_utc', 
        'nerc_region', 
        'mkt_region', 
        'zone', 
        'load_area', 
        'is_verified'], axis=1, inplace=True)

df.rename(columns={'datetime_beginning_ept': 'DATE', 'mw': 'MW'}, inplace=True)

df = df.round()

df['DATE'] = pd.to_datetime(df['DATE'])
df.index = df['DATE']
df = df.resample('H').mean()
df = df.interpolate(method='linear')

df.to_csv(output_path)