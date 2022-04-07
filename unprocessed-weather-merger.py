# Script to merge all years of a station's weather into 1 CSV

import sys
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

# args = sys.argv

# folder_path = args[1]

folder_dir = "C:/Users/Flyin/Desktop/SVR-PSO-Load-Forecaster/Data/DOM/Weather/2010-2019/"
stations = ["Norfolk","Richmond","Washington"]

output_path = "C:/Users/Flyin/Desktop/SVR-PSO-Load-Forecaster/Data/DOM/Weather/"

for station in stations:
    folder_path = folder_dir + station + '/'
    
    # List files in folder path that has all weather CSVs.
    files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    print(files)
    
    dfs = []
    
    # Read all CSVs into Pandas DataFrames and then put into list.
    for f in files:
        dfs.append(pd.read_csv(folder_path + f))
        
    dfs_all = pd.concat(dfs)
    
    dfs_all.to_csv(output_path + 'unprocessed-weather-2010-2019-' + station + '.csv')
