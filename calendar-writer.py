import sys
import numpy as np
import pandas as pd
import holidays
from dateutil.parser import parse
from datetime import date, timedelta

from pyparsing import col

def season_of_date(date):
    year = str(date.year)
    seasons = {'SPRING': pd.date_range(start='21/03/'+year, end='20/06/'+year),
               'SUMMER': pd.date_range(start='21/06/'+year, end='22/09/'+year),
               'AUTUMN': pd.date_range(start='23/09/'+year, end='20/12/'+year)}
    if date in seasons['SPRING']:
        return 'SPRING'
    if date in seasons['SUMMER']:
        return 'SUMMER'
    if date in seasons['AUTUMN']:
        return 'AUTUMN'
    else:
        return 'WINTER'

args = sys.argv

us_holidays = holidays.US()

start_date = parse(args[1])
end_date = parse(args[2])

index = start_date

df = pd.DataFrame(columns=['DATE', 'YEAR', 'MONTH', 'DAY', 'HOUR', 'SEASON', 'IS_HOLIDAY'])
df['DATE']= pd.to_datetime(df['DATE'])
while index <= end_date:
    wd = index.weekday()

    is_monday = wd == 0
    is_tuesday = wd == 1
    is_wednesday = wd == 2
    is_thursday = wd == 3
    is_friday = wd == 4
    is_saturday = wd == 5
    is_sunday = wd == 6

    year = index.year
    month = index.month
    day = index.day
    hour = index.hour
    season = season_of_date(index)
    is_holiday = index in us_holidays

    df = df.append({
        'DATE': index,
        'YEAR': year,
        'MONTH': month,
        'DAY': day,
        'HOUR': hour,
        'SEASON': season,
        'IS_HOLIDAY': is_holiday
    }, ignore_index=True)


    index += timedelta(hours=1)

df.index = df['DATE']
df = df.resample('H').mean()
df.to_csv('Data/calendar.csv')