# 외부 라이브러리와 함수 호출 예:
from datetime import datetime
time_beg = datetime.now() # 시작 시각
mulsum = 1
for i in range(1, 10001):
    mulsum = mulsum * i
time_end = datetime.now() # 종료 시각
print(f'1부터 {i}까지 곱합기 ({len(str(mulsum))}) 자리:', mulsum)

elapsed = time_end - time_beg # 경과 시간
print('시작 시각:', time_beg)
print('종료 시각:', time_end)
print('경과 시간(Elapsed):', elapsed)


'''
=========================
1부터 10000까지 곱합기 (35660) 자리: 28462596809170545189064 ... 0000
시작 시각: 2021-07-20 15:42:19.564137
종료 시각: 2021-07-20 15:42:19.588138
경과 시간(Elapsed): 0:00:00.024001
>>> 
'''
