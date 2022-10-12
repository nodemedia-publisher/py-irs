import hgsysinc
from hgstat_test_data import covid19_korea_data, covid19_japan_data
# 코로나19 그래프 예제: 한국과 일본 비교
#---
#=covid19_korea_data = [0,1,1,1,27,...,386,403,400] # total:73890(342개),20.2.15~21.1.21
#=covid19_japan_data = [0,6,7,8,10,...,6034,5446,5447] # total:345168(342개),20.2.15~21.1.21
#---
covid19_datas = [covid19_korea_data, covid19_japan_data]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
for i, data in enumerate(covid19_datas):
    plt.plot(data)
plt.show()
    
