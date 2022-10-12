import hgsysinc
from hgstat import get_histo_avg
# 히스토그램 평균 테스트
# 가상 영화 평점
vals = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
data = [10, 8, 25, 11, 130, 67, 250, 33, 186, 0]
data_sum = sum(data)
data_avg = get_histo_avg(vals, data)
print(f'({len(data)}) sum: {data_sum}')
print('data_avg: %.1f' % data_avg)

'''
처리 결과:
===============
(10) sum: 720
data_avg: 3.4

'''
