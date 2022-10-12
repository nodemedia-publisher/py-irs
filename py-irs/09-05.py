import hgsysinc
from hgtest import load_textlist_us_president
from hgdict import MakeDictFreqList__EngTextList
from datetime import datetime
#-----------------------------
#=print('reading texts:') 
us_president = load_textlist_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#-----------------------------
# 자동 색인: 공백 문자를 기준으로
# foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
DictFreqList = MakeDictFreqList__EngTextList(us_president)
print('Dict Num:', len(DictFreqList))
TotalFreq = sum(DictFreqList[dic][df_k] 
                for dic in DictFreqList 
                for df_k in DictFreqList[dic])
print('Word Num:', TotalFreq)
#-----------------------------
# 검색:
time_beg = datetime.now() # 검색 시작 시각
FindWord = 'nation'
results = DictFreqList.get(FindWord)
time_end = datetime.now() # 검색 종료 시각
if(results):
    TotalFreq = sum(results[df_k] for df_k in results)
    print(f'{len(results)} Docs: {TotalFreq} 회 출현')
    print(results)
# 경과 시간 출력
elapsed = time_end - time_beg
print('Elapsed:', elapsed)

'''
출력 결과:
============================================
nation: 54문서, 317회

============================================
============================================
Dict Num: 9110
Word Num: 136767
54 Docs: 317 회 출현
{0: 2, 2: 9, 3: 2, 4: 2, 5: 2, 6: 4, 7: 4, 8: 8, 9: 8, 10: 1, 12: 1, 13: 7, 14: 3, 16: 8, 17: 6, 19: 3, 20: 3, 21: 3, 22: 5, 23: 9, 24: 1, 25: 10, 26: 2, 27: 1, 28: 4, 29: 5, 30: 2, 31: 6, 32: 5, 33: 5, 34: 8, 35: 12, 36: 5, 37: 9, 38: 12, 40: 2, 41: 4, 42: 4, 43: 2, 44: 12, 45: 5, 46: 1, 47: 11, 48: 13, 49: 6, 50: 4, 51: 10, 52: 5, 53: 13, 54: 11, 55: 10, 56: 12, 57: 6, 58: 9}
Elapsed: 0:00:00

'''


