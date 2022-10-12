import hgsysinc
from hgstat import hgCoefficient_low
#----------
#----------
# 상관계수:혼합음료
data_drink = [32122, 36529, 52409, 63650, 72324, 72228, 71971, 69514, 56564, 53861, 45193]
data_weather = [-1.7, 2.3, 5.5, 9.9, 17.1, 22.3, 25.4, 26.9, 21.8, 14.5, 7.1]

#. 1
#=print('# 혼합음료 상관계수:', hgCoefficient_low(data_drink, data_weather, debugPrint=True))
print('# 혼합음료 상관계수:', hgCoefficient_low(data_drink, data_weather))

#. 2
import numpy
print('# {numpy} 혼합음료 상관계수:', numpy.corrcoef(data_drink, data_weather))

#. 3
from scipy.stats import pearsonr
print('# {scipy} 혼합음료 상관계수:', pearsonr(data_drink, data_weather))

# 4
import pandas as pd
drink_series = pd.Series(data_drink)
weather_series = pd.Series(data_weather)
print('# {pandas} 혼합음료 상관계수:', drink_series.corr(weather_series))




'''
출력 결과:
#================
# 혼합음료 상관계수: 0.8642998742161233
# {numpy} 혼합음료 상관계수: [[1.         0.86429987]
 [0.86429987 1.        ]]
# {scipy} 혼합음료 상관계수: (0.8642998742161233, 0.0005990129506067524)
# {pandas} 혼합음료 상관계수: 0.8642998742161232

'''
