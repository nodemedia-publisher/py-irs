import hgsysinc
from hgtest import load_textlist_us_president
from hgdict import MakeDictFreqList__EngTextList
from hgfind import Han2EngChecker
#-----------------------------
#-----------------------------
#=print('reading texts')
us_president = load_textlist_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#-----------------------------
#-----------------------------
# foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
DictFreqList = MakeDictFreqList__EngTextList(us_president)
print('Dict Num:', len(DictFreqList))
#=WordNum = sum(DictFreqList[dic][df_k] for dic in DictFreqList for df_k in DictFreqList[dic])
#=print('Word Num:', WordNum)

print('#==============')
print('한영 변환과 철자 오류 교정')
print('#==============')
Han2EngChecker('햎ㄷ구ㅡ둣', DictFreqList) # 'government' (한영변환 오류)
Han2EngChecker('퍛새교', DictFreqList) # 'victory' (한영변환 오류)

Han2EngChecker('랲ㄷ구ㅡ둣', DictFreqList) # 'fovernment' <--- 'government' (한영변환 오류 + 철자 오류)
Han2EngChecker('챷새교', DictFreqList) # 'cictory' <--'victory' (한영변환 오류 + 철자 오류)




'''
처리 결과:
===========================
Dict Num: 9110
#==============
한영 변환과 철자 오류 교정
#==============
[한영변환] 햎ㄷ구ㅡ둣 ===> government

DisWord Num: 7
# 편집 거리 순서 출력
1 : government (0, 54)
2 : governments (1, 29)
3 : governmental (2, 5)
4 : governed (3, 7)
5 : movement (3, 6)
6 : governing (3, 6)
7 : concernment (3, 2)

[한영변환] 퍛새교 ===> victory

DisWord Num: 11
# 편집 거리 순서 출력
1 : victory (0, 10)
2 : history (2, 36)
3 : factory (2, 6)
4 : vigor (3, 11)
5 : story (3, 5)
6 : vicious (3, 4)
7 : victories (3, 3)
8 : victims (3, 3)
9 : picture (3, 2)
10 : victim (3, 1)
11 : factor (3, 1)

[한영변환] 랲ㄷ구ㅡ둣 ===> fovernment

DisWord Num: 5
# 편집 거리 순서 출력
1 : government (1, 54)
2 : governments (2, 29)
3 : movement (3, 6)
4 : governmental (3, 5)
5 : concernment (3, 2)

[한영변환] 챷새교 ===> cictory

DisWord Num: 9
# 편집 거리 순서 출력
1 : victory (1, 10)
2 : history (2, 36)
3 : factory (2, 6)
4 : century (3, 22)
5 : city (3, 11)
6 : story (3, 5)
7 : picture (3, 2)
8 : custody (3, 1)
9 : factor (3, 1)

>>> 

'''
