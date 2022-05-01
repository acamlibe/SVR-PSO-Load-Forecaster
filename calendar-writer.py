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
while index < end_date:
    wd = index.weekday()
    wm = index.month
    he = index.hour + 1

    is_monday = 1 if wd == 0 else 0
    is_tuesday = 1 if wd == 1 else 0
    is_wednesday = 1 if wd == 2 else 0
    is_thursday = 1 if wd == 3 else 0
    is_friday = 1 if wd == 4 else 0
    is_saturday = 1 if wd == 5 else 0
    is_sunday = 1 if wd == 6 else 0

    is_january = 1 if wm == 1 else 0
    is_february = 1 if wm == 2 else 0
    is_march = 1 if wm == 3 else 0
    is_april = 1 if wm == 4 else 0
    is_may = 1 if wm == 5 else 0
    is_june = 1 if wm == 6 else 0
    is_july = 1 if wm == 7 else 0
    is_august = 1 if wm == 8 else 0
    is_september = 1 if wm == 9 else 0
    is_october = 1 if wm == 10 else 0
    is_november = 1 if wm == 11 else 0
    is_december = 1 if wm == 12 else 0

    is_he1 = 1 if he == 1 else 0
    is_he2 = 1 if he == 2 else 0
    is_he3 = 1 if he == 3 else 0
    is_he4 = 1 if he == 4 else 0
    is_he5 = 1 if he == 5 else 0
    is_he6 = 1 if he == 6 else 0
    is_he7 = 1 if he == 7 else 0
    is_he8 = 1 if he == 8 else 0
    is_he9 = 1 if he == 9 else 0
    is_he10 = 1 if he == 10 else 0
    is_he11 = 1 if he == 11 else 0
    is_he12 = 1 if he == 12 else 0
    is_he13 = 1 if he == 13 else 0
    is_he14 = 1 if he == 14 else 0
    is_he15 = 1 if he == 15 else 0
    is_he16 = 1 if he == 16 else 0
    is_he17 = 1 if he == 17 else 0
    is_he18 = 1 if he == 18 else 0
    is_he19 = 1 if he == 19 else 0
    is_he20 = 1 if he == 20 else 0
    is_he21 = 1 if he == 21 else 0
    is_he22 = 1 if he == 22 else 0
    is_he23 = 1 if he == 23 else 0
    is_he24 = 1 if he == 24 else 0

    is_prevday_holiday = 1 if index + timedelta(days=-1) in us_holidays else 0
    is_currentday_holiday = 1 if index in us_holidays else 0
    is_nextday_holiday = 1 if index + timedelta(days=1) in us_holidays else 0
    is_dayafternext_holiday = 1 if index + timedelta(days=2) in us_holidays else 0
    
    row = pd.DataFrame({
        'DATE': [index],
        'IS_HE1': [is_he1],
        'IS_HE2': [is_he2],
        'IS_HE3': [is_he3],
        'IS_HE4': [is_he4],
        'IS_HE5': [is_he5],
        'IS_HE6': [is_he6],
        'IS_HE7': [is_he7],
        'IS_HE8': [is_he8],
        'IS_HE9': [is_he9],
        'IS_HE10': [is_he10],
        'IS_HE11': [is_he11],
        'IS_HE12': [is_he12],
        'IS_HE13': [is_he13],
        'IS_HE14': [is_he14],
        'IS_HE15': [is_he15],
        'IS_HE16': [is_he16],
        'IS_HE17': [is_he17],
        'IS_HE18': [is_he18],
        'IS_HE19': [is_he19],
        'IS_HE20': [is_he20],
        'IS_HE21': [is_he21],
        'IS_HE22': [is_he22],
        'IS_HE23': [is_he23],
        'IS_HE24': [is_he24],
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