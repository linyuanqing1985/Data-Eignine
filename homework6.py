# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:22:01 2020

@author: LinYuanqing
"""


import pandas as pd
from fbprophet import Prophet


# 数据加载


def data_collect(train):
    train['Datetime']=pd.to_datetime(train.Datetime,format="%d-%m-%Y %H:%M")
    train.index=train.Datetime
    train.drop(['ID','Datetime'],axis=1,inplace=True)
    daily_train=train.resample('D').sum()
    daily_train['ds']=daily_train.index
    daily_train['y']=daily_train.Count
    daily_train.drop(['Count'],axis=1,inplace=True)
    return daily_train


def daily_fbprophet(daily_train):
    m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
# 预测未来7个月，213天
    m.fit(daily_train)
    future = m.make_future_dataframe(periods=213)
    forecast=m.predict(future)
    print(forecast)
    m.plot(forecast)
    m.plot_components(forecast)
    
    
def main():
    datapath='./train.csv'
    train=pd.read_csv(datapath)
    daily_train=data_collect(train)
    daily_fbprophet(daily_train)
    
    
main()