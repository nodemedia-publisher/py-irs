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
#=print ('@@@ BackWordDictList : 데이터 그대로 출력')
#=PrintWordDictList(BackWordDictList, OneLine=True, PrintIndex=True, SimpleFormat=True)
#=print (),
print ('@@@ BackWordDictList : 출력할 때 [BackwardFlag] 적용')
PrintWordDictList(BackWordDictList, OneLine=True, 
    PrintIndex=True, SimpleFormat=True, BackwardFlag=True)


'''
처리 결과:
==================================
---------------- back-word dict
@@@ BackWordDictList : 출력할 때 [BackwardFlag] 적용
TotalWordFreq: 173
순서    단어    빈도    점유율
1:      KBS     1       0.6
2:      날씨가  2       1.2
3:      기상전문기자가  1       0.6
......
25:     시작되는        1       0.6
26:     날리는  1       0.6
27:     추위는  1       0.6
......
94:     싶어요  1       0.6
95:     차가운  1       0.6
96:     매서운  2       1.2
97:     겨울    1       0.6
......
151:    새해    4       2.3
152:    이후    1       0.6
153:    단단히  1       0.6

'''
