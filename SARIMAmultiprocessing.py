# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 18:20:38 2022

@author: Michael Gray
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from math import sqrt
import itertools
import statsmodels.api as sm
from joblib import Parallel
from joblib import delayed
from warnings import catch_warnings
from warnings import filterwarnings
from multiprocessing import cpu_count
from sklearn.metrics import mean_squared_error

df = pd.read_csv('Data/DOM/Load Actuals/Processed/Aggregated/load.csv', parse_dates=['DATE'])

# df.rename(columns={'datetime_beginning_utc': 'date','mw':'mw'},inplace=True)
# mask1 = df['date'].dt.date == datetime.date(2012, 2, 29)
# mask2 = df['date'].dt.date == datetime.date(2016, 2, 29)
# df.drop(df.index[mask1 | mask2],inplace=True)

plt.figure(figsize=(10,4))
plt.plot(df['MW'])

start_date_mask = df['DATE'].dt.date >= datetime.date(2019, 1, 1)
end_date_mask = df['DATE'].dt.date < datetime.date(2019, 3, 8)
df_subset = df[start_date_mask & end_date_mask]

# df_subset.set_index('date',inplace=True)

def train_test_split(data, n_test):
	return data[:-n_test], data[-n_test:]

train, test = train_test_split(df_subset['MW'].values, 168)

x_axis = np.arange(train.shape[0] + test.shape[0])
x_dates = df_subset['DATE'].values

plt.figure(figsize=(10,4))
plt.plot(x_dates[x_axis[:train.shape[0]]], train, alpha=0.75)
plt.plot(x_dates[x_axis[train.shape[0]:]], test, alpha=0.75)
plt.title('Train and Test Data')

season_period = 24

def sarima_configs():
    p = q = range(0, 3)
    d = range(0,2)

    pdq = list(itertools.product(p, d, q))
    pdqs = [(x[0], x[1], x[2], season_period) for x in list(itertools.product(p, d, q))]

    all_combs = []
    for comb in pdq:
        for combs in pdqs:
            all_combs.append([comb,combs])
    return all_combs

# root mean squared error or rmse
def measure_rmse(actual, predicted):
	return sqrt(mean_squared_error(actual, predicted))

def score_model(train, test, cfg):
# convert config to a key
    key = str(cfg)
    try:
        # ever show warnings when grid searching, too noisy
        with catch_warnings():
            filterwarnings("ignore")
            model = sm.tsa.statespace.SARIMAX(train, 
                                               order = cfg[0], 
                                               seasonal_order = cfg[1],
                                                enforce_stationarity=False,
                                                enforce_invertibility=False) 
            model_fit = model.fit(disp=False)
            yhat = model_fit.forecast(steps=168)
            error = measure_rmse(test, yhat)
    except:
        error = None
	# check for an interesting result
    if yhat is not None:
        print(' > Model fitted:' + key + ' RMSE: ' + str(error))
    return(key, error)

cfg_list = sarima_configs()

if __name__ == '__main__':
    executor = Parallel(n_jobs=cpu_count(), backend='multiprocessing')
    tasks = (delayed(score_model)(train, test, cfg) for cfg in cfg_list)
    scores = executor(tasks)      

    scores.sort(key = lambda x: x[1]) # sort score tuples by RMSEs

    print('Best Model: ' + str(scores[0]))



                
                
                
                
                
                

