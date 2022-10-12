#=import hgsysinc
#=from hgstat_test_data import (
#=    kma_weather_2010, kosos_drink_2010, kosos_soymilk_2010, kosos_carbonated_drink_2010,
#=)
#-----
#=data_x = [kosos_drink_2010[k] for k in kosos_drink_2010] # 혼합 음료
#=data_y = [kma_weather_2010[k] for k in kma_weather_2010] # 날씨
#=print('data_x:', data_x)
#=print('data_y:', data_y)

# 산포도 : 혼합음료 x 날씨
data_drink = [32122, 36529, 52409, 63650, 72324, 72228, 71971, 69514, 56564, 53861, 45193]
data_weather = [-1.7, 2.3, 5.5, 9.9, 17.1, 22.3, 25.4, 26.9, 21.8, 14.5, 7.1]

#
data_x = data_weather # 날씨
data_y = data_drink # 혼합 음료

title_x = '2010 Weather'
title_y = '2010 Drink', 
label_x = 'Weather'
label_y = 'Drink'

title = '2010 ' + label_y + ' & ' + label_x

# 그래프 출력
import matplotlib.pyplot as plt

#=figsize = (10, 5) # 가로 데이터가 많을 때
figsize = (6, 6) # 가로, 세로 데이터 수가 같을 때
#=dotSize = 50
dotSize = 130 # 점을 크게
#
plt.figure(figsize=figsize)
plt.scatter(data_x, data_y, s=dotSize) # 날씨(data_x)를 가로축에
#
plt.xlabel(label_x, fontsize=15)
plt.ylabel(label_y, fontsize=15)
#=plt.legend(loc='upper left')

figure = plt.gcf()
#=figure.canvas.set_window_title(title) # 윈도우 창에 [제목] 보이기
#=#=plt.suptitle(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시
plt.title(title, fontsize=20, y=1.04) # 이미지 밖의 위쪽에 [제목] 표시

#=# 숫자가 클 경우에 라벨 표기가 지수형(exponential)으로 바뀌지 않게
#=plt.ticklabel_format(useOffset=False, style='plain', axis='y')
#
figure.tight_layout() # x,y label 잘리지 않도록
#
plt.show()

# 
plt.close() # 이 함수를 호출하지 않으면 다음 호출에 이전 그림이 같이 호출됨.



'''
출력 결과:

#================
#================

data_x: [32122, 36529, 52409, 63650, 72324, 72228, 71971, 69514, 56564, 53861, 45193]
data_y: [-1.7, 2.3, 5.5, 9.9, 17.1, 22.3, 25.4, 26.9, 21.8, 14.5, 7.1

'''
