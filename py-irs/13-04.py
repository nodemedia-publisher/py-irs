import hgsysinc
from hgtest import load_textlist_us_president
from hgdict import MakeDictFreqList__EngTextList
#-----------------------------
#-----------------------------
#=print('reading texts')
us_president = load_textlist_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#-----------------------------
#-----------------------------
# foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
DictFreqList = MakeDictFreqList__EngTextList(us_president)
print('Dict Num:', len(DictFreqList))
WordNum = sum(DictFreqList[dic][df_k] for dic in DictFreqList for df_k in DictFreqList[dic])
print('Word Num:', WordNum)

#-----
#-----
from hgworddistance import FindDisWord_Vocabulary
#-----
# 아래 FindDisWord_Vocabulary() 함수에서 {DisMax} 매개변수는 
# 지정값이 '3'이라서 따로 지정하지 않아도 된다.
# 다른 코드에서는 어색한 단어를 보여주려고 의도적으로 '0'으로 바꿨다.
#-----
#=DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=0) # 모두 출력
DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=10)
print('DisWord Num:', len(DisWord))

print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-doc-num
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)


'''
처리 결과:
===================
Dict Num: 9110
Word Num: 136767
DisWord Num: 7
# 편집 거리 순서 출력
1 : ('government', (1, 54))
2 : ('governments', (2, 29))
3 : ('movement', (2, 6))
4 : ('governmental', (3, 5))
5 : ('movements', (3, 4))
6 : ('covenant', (3, 4))
7 : ('convenient', (3, 1))

'''
