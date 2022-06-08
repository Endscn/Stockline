import pandas as pd
import numpy as np
import time


# 랜덤시드 고정
np.random.seed(0)


start = time.time()

# 더미데이터 만들기
N = 15000
df = pd.DataFrame(data=np.random.choice(range(5), size=(N, 8)))
df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

"""
#유사행 찾는 함수 정의
def similar_rows(idx, row, df):
    mask = np.logical_and.reduce([
        df['a'] == row['a'],
        abs(df['b'] - row['b']) <= 1,
        df['h'] == (3 - row['h'])
    ])

    df_tmp = df.loc[mask, :]
    df_tmp.insert(0, 'original_index', idx)
    return df_tmp


# 결과 생성
df_new = pd.concat([similar_rows(idx, row, df) for idx, row in df.iterrows()])
df_new.reset_index(inplace=True)
df_new.rename({'index': 'similar_index'}, axis=1, inplace=True)
print(df_new.head(10))
"""

#----------------------------------------------------------


# 여기는 임의로 선택한 행에 대해서 근처를 보여주는 함수

# 랜덤row 생성
row = df.loc[np.random.choice(N), :]

#10번째 행 지정, :은 전부다 불러오라는 뜻#
#row = df.loc[10, :]

print('Randomly Selected Row:')
print(pd.DataFrame(row).T)

"""
group_name1 = ['char', 'flow','wide',
               'drea','dens','pers',
               'colo','scen','call','pend']
"""
df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# 여기서 row는 pandas.series 로 받아오기때문에 그에 맞게 관리해야한다. row.keys를 사용해서 head값을 따올 수 있다.
row = df.loc[np.random.choice(N), :]
print(row)

#최댓값 찾는 로직

max_percentage = max(row[:])
print(max_percentage)

maxcatelist =[]

#print(row.keys())

for i in range(len(row.keys())):
    if row[i] == max_percentage:
        print(row[i],"max 값")
        print(row.keys()[i],"max 값의 카테고리")
        print(i,"max값이 존재하는 위치")
        max_cate = df.columns[i]  #df.columns 에서 i번째 있는 퍼센트를 maxcate에 넣는다.
print(max_cate)


#두번째로 큰 값 찾는 로직
sec_max_percentage = sorted(row[:],reverse=True)
sec_max_percentage = sec_max_percentage[1]
print(sec_max_percentage)

sec_maxcatelist =[]

for i in range(len(row.keys())):
    if row[i] == sec_max_percentage:
        print(row[i],"두번째로 큰 값")
        print(row.keys()[i],"두번째로 큰 값의 카테고리")
        print(i,"두번째로 큰 값이 존재하는 위치")

        sec_max_cate = df.columns[i]
        sec_maxcatelist.append(sec_max_cate)

print(sec_max_cate)





# 임의로 생성한 유사한 행에 대해서 마스크 생성,적용
mask = np.logical_and.reduce([
    df[max_cate] == row[max_cate],
    df[sec_max_cate] == row[sec_max_cate],
    #abs(df['b'] - row['b']) <= 1,
    #df['h'] == (3 - row['h'])
])

#print(mask)

print('"Similar" Results:')
df_filtered = df.loc[mask, :]
print(df_filtered)

end = time.time()
print("time :",end - start)

#help(np.logical_and.reduce)


"""
#나누고 나면 1이 남는 수를 구하는 공식
A = int(input("A값을 입력하세요"))
nanulist = []

for i in range(1,A):
    if A%i==1:
        nanulist.append(i)
        print(A,"/",i,"=","(",A//i,"*",i,")","+",A%i)

print(nanulist)
"""








