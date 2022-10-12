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
#--------------
#=WordNum = sum(DictFreqList[dic][df_k] for dic in DictFreqList for df_k in DictFreqList[dic])
#=print('Word Num:', WordNum)
#
if('freedom' in DictFreqList):
    docnum = len(DictFreqList['freedom'])
    print(f'freedom ({docnum}) :', DictFreqList['freedom'])



'''
처리결과:
==================================
Dict Num: 9110
freedom (37) : {3: 4, 4: 2, 5: 1, 9: 5, 10: 1, 13: 6, 14: 2, 16: 3, 23: 7, 25: 2, 27: 1, 28: 4, 30: 2, 32: 2, 33: 5, 34: 6, 35: 6, 38: 6, 39: 1, 40: 13, 41: 10, 42: 11, 43: 4, 44: 2, 45: 2, 46: 1, 47: 4, 48: 
4, 49: 8, 50: 14, 51: 6, 52: 3, 53: 2, 54: 5, 55: 27, 56: 3, 57: 6}


'''


