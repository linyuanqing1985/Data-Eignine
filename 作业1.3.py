

# 开始

print('step1')

import pandas as pd

data=pd.read_csv("car_complain.csv")

# print(data)

print('step2')
data = data.drop('problem', 1).join(data.problem.str.get_dummies(','))
data.to_csv("Car_problem.csv")
# print(data)

print('Step3')

brandcount= data.groupby(['brand'])['id'].agg(['count']).sort_values('count',ascending=False)
print(brandcount)

modelcount=data.groupby(['brand','car_model'])['id'].agg(['count']).sort_values('count',ascending=False)
print(modelcount)

data.reset_index(inplace=True)
meancount=data.groupby(['brand','car_model'])['id'].agg(['count']).groupby(['brand']).mean()
print(meancount)