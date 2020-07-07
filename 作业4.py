# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:47:02 2020

@author: LinYuanqing
"""


import pandas as pd
import numpy as np
from efficient_apriori import apriori

# header=none
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)




def clear_null(dataset):
    tran=[]
    for i in range(0,dataset.shape[0]):
        temp=[]
        for j in range(0,dataset.shape[1]):
            if str(dataset.values[i,j])!='nan':
                temp.append(str(dataset.values[i, j]))
                tran.append(temp)
    return tran
    


def use_efficient_apriori(tran):
    # 使用 efficient_apriori
    # 挖掘频繁项集和频繁规则
    item, rules = apriori(tran, min_support=0.05,  min_confidence=0.4)
    print("频繁项集：", item)
    print("关联规则：", rules)




# 使用 mlxtend  不太理解
def use_mlextend1(dataset):
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    from mlxtend.preprocessing import TransactionEncoder
    tempp=TransactionEncoder()
    tempp_hot_encode=tempp.fit(dataset).transform(dataset)
    df=pd.DataFrame(tempp_hot_encode,columns=tempp.columns_)
    print(df)
    
    frequent_itemsets=apriori(df,min_support=0.05,use_colnames= True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
    print("频繁项集：", frequent_itemsets)
    print("关联规则：", rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.5) ])
    rules.to_csv('关联规则.csv')



# 使用 手工转换
def transform_data(dataset):
    temppp=dataset.fillna("-")
    index_i=[]
    for i in range(dataset.shape[0]):
        index_i.append(i)
        
    temp_pd=pd.DataFrame({},index=index_i,columns=[0])
    temp_pd=temp_pd.fillna('')
    
    for i in range(dataset.shape[0]):
        for j in range(dataset.shape[1]):
            if temppp[j][i]!='':
                temp_pd.iloc[i,0]=temp_pd.iloc[i,0]+'/'+temppp[j][i]
    
    print(temp_pd)
    hot_encode=temp_pd[0].str.get_dummies ('/')
    print(hot_encode)
    return hot_encode


def use_mlextend2(hot_encode):
    from mlxtend.frequent_patterns import apriori
    from mlxtend.frequent_patterns import association_rules
    frequent_itemsets=apriori(hot_encode,min_support=0.05,use_colnames= True)
    frequent_itemsets = frequent_itemsets.sort_values(by="support" , ascending=False) 
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=0.5)
    rules = rules.sort_values(by="lift" , ascending=False) 
    print('-'*20, '关联规则', '-'*20)
    print(rules)
    rules.to_csv('关联规则2.csv')


cleandata=clear_null(dataset)
use_efficient_apriori(cleandata)

use_mlextend1(cleandata)

hot_encode=transform_data(dataset)
use_mlextend2(hot_encode)


