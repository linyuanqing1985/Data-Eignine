# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 22:59:46 2020

@author: LinYuanqing
"""


import pandas as pd
from pandas import Series, DataFrame
data = {'Chinese': [68, 95, 98, 90,80],'Math': [65, 76, 86, 88, 90],'English': [30, 98, 88, 77, 90]}
df1= DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'liubei', 'dianwei', 'xuchu'], columns=['Chinese', 'Math', 'English'])


averagescore=df2.mean()
print("Chinese average score:",averagescore["Chinese"])
print("Math average score:",averagescore["Math"])
print("English average score:",averagescore["English"])

maxscore=df2.max()
print("Chinese max score:",maxscore["Chinese"])
print("Math max score:",maxscore["Math"])
print("English max score:",maxscore["English"])

minscore=df2.min()
print("Chinese min score:",minscore["Chinese"])
print("Math min score:",minscore["Math"])
print("English min score:",minscore["English"])

varscore=df2.min()
print("Chinese varient score:",varscore["Chinese"])
print("Math varient score:",varscore["Math"])
print("English varient score:",varscore["English"])

stdscore=df2.min()
print("Chinese standard deviation score:",stdscore["Chinese"])
print("Math standard deviation score:",stdscore["Math"])
print("English standard deviation score:",stdscore["English"])


def plus(df):
    df['total']=df['Chinese']+df['Math']+df['English']
    return df
df3=plus(df2)

df4=df3.sort_values(by='total',ascending=False,axis=0,inplace=False)

print(df4['total'])


