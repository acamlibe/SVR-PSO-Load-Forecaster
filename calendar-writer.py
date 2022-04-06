import sys
import numpy as np
import pandas as pd
import holidays
from dateutil.parser import parse
from datetime import date, timedelta

from pyparsing import col

args = sys.argv

us_holidays = holidays.US()

start_date = parse(args[1])
end_date = parse(args[2])

print(f'Writing calendar features from {start_date} to {end_date}')

index = start_date

df = pd.DataFrame(columns=['DATE',
    'IS_MONDAY',
    'IS_TUESDAY',
    'IS_WEDNESDAY',
    'IS_THURSDAY',
    'IS_FRIDAY',
    'IS_SATURDAY',
    'IS_SUNDAY',
    'IS_JANUARY',
    'IS_FEBRUARY',
    'IS_MARCH',
    'IS_APRIL',
    'IS_MAY',
    'IS_JUNE',
    'IS_JULY',
    'IS_AUGUST',
    'IS_SEPTEMBER',
    'IS_OCTOBER',
    'IS_NOVEMBER',
    'IS_DECEMBER',
    'IS_PREVDAY_HOLIDAY',
    'IS_CURRENTDAY_HOLIDAY',
    'IS_NEXTDAY_HOLIDAY',
    'IS_DAYAFTER_HOLIDAY'])


df['DATE']= pd.to_datetime(df['DATE'])
while index <= end_date:
    wd = index.weekday()
    wm = index.month

    is_monday = wd == 0
    is_tuesday = wd == 1
    is_wednesday = wd == 2
    is_thursday = wd == 3
    is_friday = wd == 4
    is_saturday = wd == 5
    is_sunday = wd == 6

    is_january = wm == 1
    is_february = wm == 2
    is_march = wm == 3
    is_april = wm == 4
    is_may = wm == 5
    is_june = wm == 6
    is_july = wm == 7
    is_august = wm == 8
    is_september = wm == 9
    is_october = wm == 10
    is_november = wm == 11
    is_december = wm == 12

    is_prevday_holiday = index + timedelta(days=-1) in us_holidays
    is_currentday_holiday = index in us_holidays
    is_nextday_holiday = index + timedelta(days=1) in us_holidays
    is_dayafternext_holiday = index + timedelta(days=2) in us_holidays
    
    row = pd.DataFrame({
        'DATE': [index],
        'IS_MONDAY': [is_monday],
        'IS_TUESDAY': [is_tuesday],
        'IS_WEDNESDAY': [is_wednesday],
        'IS_THURSDAY': [is_thursday],
        'IS_FRIDAY': [is_friday],
        'IS_SATURDAY': [is_saturday],
        'IS_SUNDAY': [is_sunday],
        'IS_JANUARY': [is_january],
        'IS_FEBRUARY': [is_february],
        'IS_MARCH': [is_march],
        'IS_APRIL': [is_april],
        'IS_MAY': [is_may],
        'IS_JUNE': [is_june],
        'IS_JULY': [is_july],
        'IS_AUGUST': [is_august],
        'IS_SEPTEMBER': [is_september],
        'IS_OCTOBER': [is_october],
        'IS_NOVEMBER': [is_november],
        'IS_DECEMBER': [is_december],
        'IS_PREVDAY_HOLIDAY': [is_prevday_holiday],
        'IS_CURRENTDAY_HOLIDAY': [is_currentday_holiday],
        'IS_NEXTDAY_HOLIDAY': [is_nextday_holiday],
        'IS_DAYAFTER_HOLIDAY': [is_dayafternext_holiday],
    })

    df = pd.concat([df, row], ignore_index=False, axis=0)

    index += timedelta(hours=1)
    print(f"Processing [{index}]", end="\r", flush=True)

print('Writing to CSV at Data/calendar.csv')
df.to_csv('Data/calendar.csv', index=False)