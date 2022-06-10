
import numpy as np
from pyimagesearch.pyimagesearch.colordescriptor import ColorDescriptor as cd
from pyimagesearch.pyimagesearch.searcher import Searcher
import csv
import cv2
import imutils



# 카이 제곱 거리 사용
def chi2_distance(histA, histB, eps=1e-10):
    # compute the chi-squared distance
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
                      for (a, b) in zip(histA, histB)])
    # return the chi-squared distance
    return d



# query 값만 따로 불러와서 테스트용
cd = ColorDescriptor((8, 12, 3))
query = cv2.imread("pyimagesearch/queries/nature.png")
queryFeatures = cd.describe(query)


# 내가 사용할 데이터를 위해서 따로 csv 만들어서 테스트 해보자
import yfinance as yf
import datetime
import matplotlib.pyplot as plt

start_date = datetime.date(2021, 1, 1)
# print(start_date)
# end_date = datetime.date(2022, 7, 15)
end_date = datetime.date.today()
# print(end_date)

symbolList = ["tsla","msft","mga","aapl","meta","nflx","rblx","tqqq","amd"]

# -----------------------------정규화 했을때 그래프 비교-------------------------------
tickerSymbol = 'tsla'
tickerData = yf.Ticker(tickerSymbol)
range_data = tickerData.history(period='1d', start=start_date, end=end_date)
print(range_data["Close"])

# 정규화 전 후 그래프 비교
range_b4 = range_data["Close"]
mean = range_data.mean(axis=0)
range_data -= mean
std = range_data.std(axis=0)
range_data /= std
target = range_data["Close"]

# 두개를 비교해도 모양은 같다.
plt.subplot(211)
plt.plot(target)

plt.subplot(212)
plt.plot(range_b4)
plt.show()

# --------------------------------------------------------------------------------------

import yfinance as yf
import datetime
import pandas as pd
import matplotlib.pyplot as plt


start_date = datetime.date(2021, 1, 1)
# print(start_date)
# end_date = datetime.date(2022, 7, 15)
end_date = datetime.date.today()
# print(end_date)

symbolList = ["tsla","msft"
            ,"mga","aapl","meta","nflx","rblx","tqqq","amd"
              ]

# tickerSymbol = 'tsla'
# tickerData = yf.Ticker(tickerSymbol)
# range_data = tickerData.history(period='1d', start=start_date, end=end_date)

df_accum = pd.DataFrame()
list_of_df = []
for i in symbolList:
    tickerSymbol = i
    tickerData = yf.Ticker(tickerSymbol)
    temp_data = tickerData.history(period='1d',start=start_date, end=end_date)
    temp_data = pd.DataFrame(temp_data["Close"])
    temp_data.columns = [i]
    temp_data = temp_data.T
    list_of_df.append(temp_data)
    print(i ,"complete")
    # print(temp_data)
    # print(list_of_df)

df_accum = pd.concat(list_of_df)
print(df_accum)

### csv파일 완성 헤더 삭제하면서 저장
df_accum.to_csv("index4stock.csv", index=False, na_rep='0')

### query 데이터 선택
queryFeatures =
print(queryFeatures)





# initialize our dictionary of results
results = {}
limit = 3
indexPath = "index4stock.csv"

# open the index file for reading
with open(indexPath) as f:
    # initialize the CSV reader
    reader = csv.reader(f)
    # loop over the rows in the index
    for row in reader:
        # parse out the image ID and features, then compute the
        # chi-squared distance between the features in our index
        # and our query features
        features = [float(x) for x in row[1:]]
        print(features)

        # queryFeatures =

        d = chi2_distance(features, queryFeatures)  #query를 colordescriptor로 분석한 것을 features로 받아온다.
        # now that we have the distance between the two feature
        # vectors, we can udpate the results dictionary -- the
        # key is the current image ID in the index and the
        # value is the distance we just computed, representing
        # how 'similar' the image in the index is to our query
        results[row[0]] = d
        print(results)
    # close the reader
    f.close()

# sort our results, so that the smaller distances (i.e. the
# more relevant images are at the front of the list)
results = sorted([(v, k) for (k, v) in results.items()])

print(results[:limit])