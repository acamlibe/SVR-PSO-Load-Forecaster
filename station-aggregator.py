import sys
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

args = sys.argv

folder_path = args[1]

# List files in folder path that has all processed CSVs.
files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]

dfs = []

# Read all CSVs into Pandas DataFrames and then put into list.
for f in files:
    dfs.append(pd.read_csv(folder_path + '/' + f))

# Use concat to concat the datasets, grouping by DATE column.
average_df = pd.concat(dfs).groupby('DATE').mean()

# Round values.
average_df = average_df.round()

# Write out weather.csv out in Processed folder.
average_df.to_csv(folder_path + '/weather.csv')

# TODO: Convert to weighted average using weights provided by PJM.