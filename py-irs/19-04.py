import hgsysinc
from hgstat_test_data import (
    covid19_korea_data, covid19_japan_data, covid19_italy_data,
)
from hggraph import stat_graph_line_compare
#---
#=covid19_korea_data = [0,1,1,1,27,...,386,403,400] # total:73890(342개),20.2.15~21.1.21
#=covid19_japan_data = [0,6,7,8,10,...,6034,5446,5447] # total:345168(342개),20.2.15~21.1.21
#=covid19_italy_data = [0,0,0,0,0,1,17,...,13548,14078]  # total: 2428218건(342개), 2020.02.15 ~ 2021.01.21
#---
nation = '<Korea:Japan:Italy>'
title = 'COVID 19: ' + nation + ' New Case'

label1 = 'New Case: Korea'
label2 = 'New Case: Japan'
label3 = 'New Case: Itay'

covid19_datas = [covid19_korea_data, covid19_japan_data, covid19_italy_data]
labels = [label1, label2, label3]
linestyles = ['solid', 'dotted', 'dashed']

# 그래프 출력
stat_graph_line_compare(covid19_datas, labels, linestyles=linestyles)

