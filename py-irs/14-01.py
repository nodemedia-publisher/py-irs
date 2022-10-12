import hgsysinc
from hgtest import load_dictfreq_kbs_2009, load_dictfreq_kbs_01_16
from hgkbd import HGGetSyllable__EngString
#-----------------------------
#-----------------------------
#=print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
#=DictFreqList = load_dictfreq_kbs_01_16()
print('Dict Num:', len(DictFreqList))
#=WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
#=print('Word Num:', WordNum)

#@@@@@@@@@@@@@@@@@@@@
#@@@ 먼저 검색어 사전을 탐색하지 않고 곧 바로 영한 변환한 후에 검색어 사전 탐색
#@@@@@@@@@@@@@@@@@@@@
##----------
##----------
#=FindWord = 'eogksalsrnr' # 대한민국 <== 없다
#=FindWord = 'ghksdbf' # 환율
FindWord = 'gksrnr' # 한국
HGSyllable = HGGetSyllable__EngString(FindWord) # 영문자를 한글로 변환
if HGSyllable in DictFreqList:
    print(f'[{FindWord} -> {HGSyllable}] : {DictFreqList[HGSyllable]} 회')
else:
    print(f'[{HGSyllable}] 검색어가 없습니다.')

'''
처리 결과:
==============================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
[gksrnr -> 한국] : 1655 회

'''

