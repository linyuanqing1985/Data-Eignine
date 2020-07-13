# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 23:17:42 2020

@author: LinYuanqing
"""


# -*- coding:utf-8 -*-
# 词云展示
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree

from nltk.tokenize import word_tokenize

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['Market']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云


# 数据加载
data = pd.read_csv('./MarketBasketOptimisation.csv',header=None)


    

def create_word_cloud(data):
	print('根据词频，开始生成词云!')
# 	f = remove_stop_words(f)  
  
	cut_text = word_tokenize(all_word)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("marketbasket.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()


# 生成词云

def clear_data(data):
    tran=[]
    for i in range(0,data.shape[0]):
        temp=[]
        for j in range(0,data.shape[1]):
            if str(data.values[i,j])!='nan':
                temp.append(str(data.values[i, j]))
                tran.append(temp)
    return tran
   
cleandata=clear_data(data)
all_word=''.join('%s' %item for item in cleandata)

create_word_cloud(all_word)
