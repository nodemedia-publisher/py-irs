import hgsysinc
from hgstat_test_data import (
    covid19_korea_data, data_korea_pop, 
    covid19_japan_data, data_japan_pop,
    covid19_italy_data, data_italy_pop,
)
from hgstat import get_milion_value
# 나라별 인구 : 위키백과(ko.wikipedia.org), 2021.01.23. 기준
#=data_korea_pop = int('51,821,669'.replace(',',''))
#=data_japan_pop = int('125,960,000'.replace(',',''))
#=data_italy_pop = int('59,575,231'.replace(',',''))
#
print('[확진자 비교] 인구 1백만 명 당')
covid_milion_korea = sum(covid19_korea_data) / get_milion_value(data_korea_pop)
covid_milion_japan = sum(covid19_japan_data) / get_milion_value(data_japan_pop)
covid_milion_italy = sum(covid19_italy_data) / get_milion_value(data_italy_pop)
print('백만 명 당 [korea] : %.1f' % covid_milion_korea)
print('백만 명 당 [japan] : %.1f' % covid_milion_japan)
print('백만 명 당 [italy] : %.1f' % covid_milion_italy)
#
covid_milion_rate = covid_milion_japan / covid_milion_korea
print('covid_milion_rate [japan / korea] : %.1f ( %.0f / %.0f)' % 
    (covid_milion_rate, covid_milion_japan, covid_milion_korea))
covid_milion_rate = covid_milion_italy / covid_milion_korea
print('covid_milion_rate [italy / korea] : %.1f ( %.0f / %.0f)' % 
    (covid_milion_rate, covid_milion_italy, covid_milion_korea))
covid_milion_rate = covid_milion_italy / covid_milion_japan
print('covid_milion_rate [italy / japan] : %.1f ( %.0f / %.0f)' % 
    (covid_milion_rate, covid_milion_italy, covid_milion_japan))
#
covid19_datas = [covid_milion_korea, covid_milion_japan, covid_milion_italy]
#-----
# 그래프 출력
#-----
import matplotlib.pyplot as plt
bar_num = [n for n in range(len(covid19_datas))]
plt.figure(figsize=(5, 6))
bars = plt.bar(bar_num, covid19_datas, width=0.65)
plt.show()



'''

===============================================
[확진자 비교] 인구 1백만 명 당
백만 명 당 [korea] : 1425.9
백만 명 당 [japan] : 2740.3
백만 명 당 [italy] : 40758.9
covid_milion_rate [japan / korea] : 1.9 ( 2740 / 1426)
covid_milion_rate [italy / korea] : 28.6 ( 40759 / 1426)
covid_milion_rate [italy / japan] : 14.9 ( 40759 / 2740)

'''
