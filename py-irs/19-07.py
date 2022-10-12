import hgsysinc
from hgstat import get_histo_avg
from hggraph import stat_graph_bar_histo
#------
# 가상 평점
vals = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
data = [10, 8, 25, 11, 130, 67, 250, 33, 186, 0]

data_sum = sum(data)
data_avg = get_histo_avg(vals, data)
name = 'Movie' # 영화 제목 없음
print(f'{name} >> data_sum {len(data)}:', data_sum)
print('data_avg: %.1f' % data_avg)

data_avg_str = '{:.1f}'.format(data_avg)
title = 'Movie Rating: ' + name + f'({data_sum} / {data_avg_str})'

# 그래프 출력
stat_graph_bar_histo(data, xticks=vals, title=title)


'''
출력 결과

#================================
Movie >> data_sum 10: 720
data_avg: 3.4

'''

