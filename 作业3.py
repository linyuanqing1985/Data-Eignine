from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv('car_data.csv', encoding='gbk')
train_x = data[["人均GDP","城镇人口比重","交通工具消费价格指数","百户拥有汽车量"]]



# 规范化到 [0,1] 空间
min_max_scaler = preprocessing.MinMaxScaler()
tran_x = min_max_scaler.fit_transform(train_x)


# K手肘法
sse = []
for k in range(2, 11):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(train_x)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(2, 11)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt
model = AgglomerativeClustering(linkage='ward', n_clusters=3)
y = model.fit_predict(train_x)
print(y)

linkage_matrix = ward(train_x)
dendrogram(linkage_matrix)
plt.show()

#聚类
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)

# 将结果导出到CSV文件中
result.to_csv("car_data_result.csv",index="False",encoding="GBK")
