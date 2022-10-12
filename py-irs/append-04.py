# inauguration scraping
import hgsysinc
from hgcrawl import president_list, get_inauguration_text_folder, download_inauguration_text
import time
#-----------
from datetime import datetime
time_beg = datetime.now() # 시작 시각
#-----------
# https://en.wikipedia.org/wiki/United_States_presidential_inauguration
#-----------
speech_pathname = get_inauguration_text_folder()

for inx, cur_president in enumerate(president_list):
    print(f'{inx+1}', end=' ')
    speech_url = cur_president[3]
    if(speech_url == ""):
        break
    order = cur_president[0] # format: (order, year, president, address)
    #=year = cur_president[1]
    title = cur_president[2]
    title = order + '_' + title
    #-----
    #=download_inauguration_text(speech_url, title, down_pathname=speech_pathname, debugPrint=True)
    download_inauguration_text(speech_url, title, down_pathname=speech_pathname)
    
    # 다운로드 후 대기(서버 부하를 줄이기 위해)
    if((inx + 1) < len(president_list)):
        time.sleep(5) # 5초 대기

#-----------
time_end = datetime.now() # 종료 시각
elapsed = time_end - time_beg # 경과 시간
print('시작 시각:', time_beg)
print('종료 시각:', time_end)
print('경과 시간(Elapsed):', elapsed)



'''
처리 결과:
-----------------------
59개 파일을 5초 간격으로 거의 5분 21초 걸림.
대기 시간 {290}초를 제외하면 실제로 {91}초 정도 걸림
==================

filePath: ./../pyexam/hgdatsci
parentPath: ./../pyexam
exist folder: ./../pyexam/ext-src
exist folder: ./../pyexam/ext-src/data
exist folder: ./../pyexam/ext-src/data/inauguration
exist folder: ./../pyexam/ext-src/data/inauguration/text
1 [8616]: /ext-src/data/inauguration/text/1_First_inauguration_of_George_Washington.txt
2 [787]: /ext-src/data/inauguration/text/2_George_Washington_Second_Inaugural_Address.txt
3 [13863]: /ext-src/data/inauguration/text/3_John_Adams_Inaugural_Address.txt
4 [10121]: /ext-src/data/inauguration/text/4_Thomas_Jefferson_First_Inaugural_Address.txt
5 [12903]: /ext-src/data/inauguration/text/5_Thomas_Jefferson_Second_Inaugural_Address.txt
6 [6989]: /ext-src/data/inauguration/text/6_James_Madison_First_Inaugural_Address.txt
7 [7147]: /ext-src/data/inauguration/text/7_James_Madison_Second_Inaugural_Address.txt
8 [19828]: /ext-src/data/inauguration/text/8_James_Monroe_First_Inaugural_Address.txt
9 [26299]: /ext-src/data/inauguration/text/9_James_Monroe_Second_Inaugural_Address.txt
10 [17718]: /ext-src/data/inauguration/text/10_John_Quincy_Adams_Inaugural_Address.txt
11 [6800]: /ext-src/data/inauguration/text/11_Andrew_Jackson_First_Inaugural_Address.txt
12 [7045]: /ext-src/data/inauguration/text/12_Andrew_Jackson_Second_Inaugural_Address.txt
13 [23381]: /ext-src/data/inauguration/text/13_Martin_Van_Buren_Inaugural_Address.txt
14 [49653]: /ext-src/data/inauguration/text/14_William_Henry_Harrison_Inaugural_Address.txt
15 [28696]: /ext-src/data/inauguration/text/15_James_K._Polk_Inaugural_Address.txt
16 [6594]: /ext-src/data/inauguration/text/16_Zachary_Taylor_Inaugural_Address.txt
17 [20052]: /ext-src/data/inauguration/text/17_Franklin_Pierce_Inaugural_Address.txt
18 [16806]: /ext-src/data/inauguration/text/18_James_Buchanan_Inaugural_Address.txt
19 [21093]: /ext-src/data/inauguration/text/19_Abraham_Lincoln_First_Inaugural_Address.txt
20 [3946]: /ext-src/data/inauguration/text/20_Abraham_Lincoln_Second_Inaugural_Address.txt
21 [6475]: /ext-src/data/inauguration/text/21_Ulysses_S._Grant_First_Inaugural_Address.txt
22 [7709]: /ext-src/data/inauguration/text/22_Ulysses_S._Grant_Second_Inaugural_Address.txt
23 [14889]: /ext-src/data/inauguration/text/23_Rutherford_B._Hayes_Inaugural_Address.txt
24 [17725]: /ext-src/data/inauguration/text/24_James_A._Garfield_Inaugural_Address.txt
25 [10121]: /ext-src/data/inauguration/text/25_Grover_Cleveland_First_Inaugural_Address.txt
26 [26196]: /ext-src/data/inauguration/text/26_Benjamin_Harrison_Inaugural_Address.txt
27 [12326]: /ext-src/data/inauguration/text/27_Grover_Cleveland_Second_Inaugural_Address.txt
28 [23627]: /ext-src/data/inauguration/text/28_William_McKinley_First_Inaugural_Address.txt
29 [13417]: /ext-src/data/inauguration/text/29_William_McKinley_Second_Inaugural_Address.txt
30 [5569]: /ext-src/data/inauguration/text/30_Theodore_Roosevelt_Inaugural_Address.txt
31 [32120]: /ext-src/data/inauguration/text/31_William_Howard_Taft_Inaugural_Address.txt
32 [9554]: /ext-src/data/inauguration/text/32_Woodrow_Wilson_First_Inaugural_Address.txt
33 [8368]: /ext-src/data/inauguration/text/33_Woodrow_Wilson_Second_Inaugural_Address.txt
34 [20291]: /ext-src/data/inauguration/text/34_Warren_Harding_Inaugural_Address.txt
35 [23947]: /ext-src/data/inauguration/text/35_Calvin_Coolidge_Inaugural_Address.txt
36 [22953]: /ext-src/data/inauguration/text/36_Herbert_Hoover_Inaugural_Address.txt
37 [11001]: /ext-src/data/inauguration/text/37_Franklin_Roosevelt_First_Inaugural_Address.txt
38 [10583]: /ext-src/data/inauguration/text/38_Franklin_Roosevelt_Second_Inaugural_Address.txt
39 [7473]: /ext-src/data/inauguration/text/39_Franklin_Roosevelt_Third_Inaugural_Address.txt
40 [2985]: /ext-src/data/inauguration/text/40_Franklin_Roosevelt_Fourth_Inaugural_Address.txt
41 [13587]: /ext-src/data/inauguration/text/41_Harry_S._Truman_Inaugural_Address.txt
42 [13865]: /ext-src/data/inauguration/text/42_Dwight_Eisenhower_First_Inaugural_Address.txt
43 [9103]: /ext-src/data/inauguration/text/43_Dwight_Eisenhower_Second_Inaugural_Address.txt
44 [7527]: /ext-src/data/inauguration/text/44_John_F._Kennedy_Inaugural_Address.txt
45 [8031]: /ext-src/data/inauguration/text/45_Lyndon_Johnson_Inaugural_Address.txt
46 [11491]: /ext-src/data/inauguration/text/46_Richard_Nixon_First_Inaugural_Address.txt
47 [9893]: /ext-src/data/inauguration/text/47_Richard_Nixon_Second_Inaugural_Address.txt
48 [4676]: /ext-src/data/inauguration/text/47_2_Gerald_Ford_assumption_of_the_Presidency.txt
49 [6820]: /ext-src/data/inauguration/text/48_Jimmy_Carter_Inaugural_Address.txt
50 [13713]: /ext-src/data/inauguration/text/49_Ronald_Reagan_First_Inaugural_Address.txt
51 [14497]: /ext-src/data/inauguration/text/50_Ronald_Reagan_Second_Inaugural_Address.txt
52 [12471]: /ext-src/data/inauguration/text/51_George_H._W._Bush_Inaugural_Address.txt
53 [9015]: /ext-src/data/inauguration/text/52_Bill_Clinton_first_inaugural_address.txt
54 [12169]: /ext-src/data/inauguration/text/53_Bill_Clinton_second_inaugural_address.txt
55 [9006]: /ext-src/data/inauguration/text/54_George_W._Bush_First_Inaugural_Address.txt
56 [11919]: /ext-src/data/inauguration/text/55_George_W._Bush_Second_Inaugural_Address.txt
57 [13345]: /ext-src/data/inauguration/text/56_Barack_Obama_First_Inaugural_Address.txt
58 [11954]: /ext-src/data/inauguration/text/57_Barack_Obama_Second_Inaugural_Address.txt
59 [8428]: /ext-src/data/inauguration/text/58_Donald_Trump_Inaugural_Address.txt
시작 시각: 2022-03-27 11:47:55.741341
종료 시각: 2022-03-27 11:53:16.795125
경과 시간(Elapsed): 0:05:21.053784

'''


