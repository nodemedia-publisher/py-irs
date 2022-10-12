import hgsysinc
from hgstat_test_data import covid19_korea_data
# 그래프 예제: 코로나19 
#=covid19_korea_data = [0,1,1,1,27,...,386,403,400] # total:73890(342개),20.2.15~21.1.21
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.plot(covid19_korea_data)
plt.show()

