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
# 아래 FindDisWord_Vocabulary() 함수에서 {DisMax} 매개변수를 '0'으로 지정해서 
# 편집 거래 최대 한계를 계산하지 않도록 했다.
# 지정값은 '3'으로 편집 거리가 3보다 크면 사실상 어색한 단어가 많아서 
# 찾아봤자 쓸모없지만 이 함수의 결과가 어떤지 살펴보려면 '0'으로 바꿨다.
# 알고리즘 설명을 위해서 {DisMax} 매개변수를 '0'으로 지정한다.
# {DisMax} 변수의 차이를 설명하려고 바꾼다.
#-----
print('EditDistance: 1글자 빠진 상태')
#=DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=0, DisMax=0, DebugPrint=False) # 모두 출력
DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=10, DisMax=0, DebugPrint=False)
print('DisWord Num:', len(DisWord))


'''
처리 결과
#===================
Dict Num: 9110
Word Num: 136767
EditDistance: 1글자 빠진 상태
DisWord Num: 33

'''
