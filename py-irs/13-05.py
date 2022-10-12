import hgsysinc
from hgtest import load_dictfreq_kbs_2009
#-----------------------------
#-----------------------------
#=print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009() # {KBS 9시 2009년 뉴스}
print('Dict Num:', len(DictFreqList))
WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
print('Word Num:', WordNum)
#
if('대한민국' in DictFreqList):
    print('대한민국:', DictFreqList['대한민국'])
if('한국' in DictFreqList):
    print('한국:', DictFreqList['한국'])



'''
처리결과:
========================================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
Word Num: 1689975
대한민국: 261
한국: 1655

'''


