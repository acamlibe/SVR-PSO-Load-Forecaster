import sys
import numpy as np
import pandas as pd

def process_temperature (df):
    temp_str = df.str.split(',').str[0]
    celsius_scaled = temp_str.astype(float)
    celsius = celsius_scaled / 10.0
    fahrenheit = celsius * 1.8 + 32

    return fahrenheit

def process_windspeed (df):
    windspeed_str = df.str.split(',').str[3]
    windspeed_scaled = windspeed_str.astype(float)
    wind_speed = windspeed_scaled / 10.0

    return wind_speed

args = sys.argv

file_path = args[1]
output_path = args[2]

# Read CSV. These are how NA values are formatted in the datasets.
df = pd.read_csv(file_path, na_values=['+9999,9', '999,9,9,9999,9'])

# Drop unused columns.
df.drop(['STATION', 'NAME', 'SOURCE', 'REPORT_TYPE', 'CALL_SIGN', 'QUALITY_CONTROL', 'CIG'], axis=1, inplace=True)

# Format for data is in #### format and scaled by 10 - e.g., 0034 is 3.4. Convert to regular format, and for temperature, convert to Fahrenheit.
df['TMP'] = process_temperature(df['TMP'])
df['DEW'] = process_temperature(df['DEW'])
df['WND'] = process_windspeed(df['WND'])

# Average the intrahour readings, so that there is only a single value to represent each hour.
df['DATE'] = pd.to_datetime(df['DATE'])
df.index = df['DATE']
df = df.resample('H').mean()

# Interpolate missing values in the dataset. Will work well considering this is a time series dataset.
df = df.interpolate(method='linear')

# Round out values, as only whole numbers should be used in the model.
df = df.round()

# Reorder to make sure TMP is the first column after date.
df = df[['TMP', 'DEW', 'WND']]

# Write out to output CSV, defined by command line args.
df.to_csv(output_path)