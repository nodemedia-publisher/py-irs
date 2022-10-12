from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import PrintWordDictList
from hgwordlist import GetBackWordDictList__WordList
print ('---------------- back-word dict')
# ver 1
#----------
#----------
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
BackWordDictList = GetBackWordDictList__WordList(KeywordList)
BackWordDictList.sort(key = lambda item: (item['word'])) # by abc
print ('@@@ BackWordDictList : 데이터 그대로 출력')
PrintWordDictList(BackWordDictList, OneLine=True,
                  PrintIndex=True, SimpleFormat=True)

'''
처리 결과:
==================================
@@@ BackWordDictList : 데이터 그대로 출력
TotalWordFreq: 173
순서    단어    빈도    점유율
1:      SBK     1       0.6
2:      가씨날  2       1.2
3:      가자기문전상기  1       0.6
4:      가파한  1       0.6
5:      갑장    1       0.6
6:      게좋    1       0.6
:
150:    하영    3       1.7
151:    해새    4       2.3
152:    후이    1       0.6
153:    히단단  1       0.6

'''
