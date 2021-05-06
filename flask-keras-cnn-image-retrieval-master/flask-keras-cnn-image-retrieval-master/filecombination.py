import pandas as pd
import numpy as np
from glob import glob


##############파일 합치기만
totaldf = pd.DataFrame({'ID':  b'1.jpg'}, index=[1])
namelist =[]
standards = glob('C:/Users/bwang/PycharmProjects\gitCBIR/flask-keras-cnn-image-retrieval-master/flask-keras-cnn-image-retrieval-master/resultcsv/*.csv')

for i in standards:
    i = i.replace("C:/Users/bwang/PycharmProjects\gitCBIR/flask-keras-cnn-image-retrieval-master/flask-keras-cnn-image-retrieval-master/resultcsv\\resultb'","")
    i = i.replace("\'.csv","")
    print(i)
    namelist.append(i)
print(namelist)

for i in namelist:
    dfmerge1 = pd.read_csv("C:/Users/bwang/PycharmProjects\gitCBIR/flask-keras-cnn-image-retrieval-master/flask-keras-cnn-image-retrieval-master/resultcsv/resultb\'" + str(i) + "\'.csv")
    dfmerge1 = dfmerge1.drop(columns='Unnamed: 0')

    totaldf= pd.merge(totaldf,dfmerge1, on='ID', how='outer')
    print(i)

print(totaldf.head())

"""
for i in range(4000,5000):
    start = time.time
    dfmerge1 = pd.read_csv("D:/Jupyter/gitCBIR/flask-keras-cnn-image-retrieval-master/resultcsv/resultb\'" + str(i) + ".jpg\'.csv")
    dfmerge1 = dfmerge1.drop(columns='Unnamed: 0')

    totaldf= pd.merge(totaldf,dfmerge1, on='ID', how='outer')
    print(i)

print(totaldf.head())
"""

"""
for i in range(1,13):
    dfmerge1 = pd.read_csv('D:/Jupyter/gitCBIR/flask-keras-cnn-image-retrieval-master/resultcsv/results'+str(i)+'.csv')
    dfmerge1 = dfmerge1.drop(columns='Unnamed: 0')

    totaldf= pd.merge(totaldf,dfmerge1, on='ID', how='outer')
"""



totaldf.to_csv("totaldata.csv", encoding='utf-8')
print(totaldf)

######정규화 및 변경
"""
#정규화
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
#df[:] = scaler.fit_transform(df[:])
#df= pd.concat([y_data,df],axis=1)
df_test[:] = scaler.fit_transform(df_test[:])
df_test= pd.concat([y_data_test,df_test],axis=1)
"""
df = pd.read_csv("totaldata.csv")
df = df.drop(["Unnamed: 0"],axis=1)
y_data = df['ID']
df = df.drop(["ID"],axis=1)

#for test
#df_test = pd.read_csv("totaldata_test.csv")
#df_test = df_test.drop(["Unnamed: 0"],axis=1)
#y_data_test = df_test['ID']
#df_test = df_test.drop(["ID"],axis=1)

"""
#mindf 는 Min 만 찾아둔것.#
df_sorted_by_values = df_test.sort_values(by='ID',ascending=True)
mindf = df_sorted_by_values.min(axis=1)

dfvalmin = pd.concat([df_sorted_by_values,mindf],axis=1)
dfvalmin = dfvalmin.rename(columns={0:"MIN"})
"""



def kth_largest_number(arr, K):
    unique_nums = set(arr)
    sorted_nums = sorted(unique_nums, reverse=True)
    return sorted_nums[K-1]
#maxdf 는 Max값만 찾아둔것. 21년 4월 21일 작성

df_sorted_by_values = df.sort_values(by='ID',ascending=True)
print(df_sorted_by_values)
df_arr = np.array(df_sorted_by_values)
print(df_arr)

unique_nums = set(df_arr)
print(unique_nums)
sorted_nums = sorted(unique_nums, reverse=True)
print(sorted_nums[1])

kth_largest_number(df_arr,2)

df_sorted_by_values_4_findmax = df_sorted_by_values[df_sorted_by_values.between(0,1, inclusive=False)]

maxdf = df_sorted_by_values_4_findmax.max(axis=1)

dfvalmax = pd.concat([df_sorted_by_values,maxdf],axis=1)
dfvalmax = dfvalmax.rename(columns={0:"MAX"})


#print(df)
#print(mindf)
#print(dfvalmin)







batch_list = [16, 32, 64, 128]
lr_list = [0.005, 0.001, 0.0005, 0.0001]
for lr in lr_list:
    for bat in batch_list:
        batch_size = bat
        epochs = 20
        learning_rate = lr

        print(lr, bat)

