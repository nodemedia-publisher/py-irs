from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import GetWordDictList_WordList
from hgwordlist import PrintWordDictList
#---------- word dict
#---------- word dict
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
WordDictList = GetWordDictList_WordList(KeywordList)

# sort by len low, abc
#= @@@---------------- word dict sort by len low -> high, a->z')
print('# @@@ 단어 길이 (짧은) 순서로 정렬(코드 순서로 2차 정렬)')
WordDictList.sort(key = lambda item: (item['len'], item['word'])) # by len low, abc
PrintWordDictList(WordDictList, OneLine=True, PrintIndex=True, SimpleFormat=True)
print ('')


'''
처리 결과:

==================================
# @@@ 단어 길이 (짧은) 순서로 정렬(코드 순서로 2차 정렬)
TotalWordFreq: 173
순서	단어	빈도	점유율
1:	그	1	0.6
2:	눈	1	0.6
3:	더	1	0.6
:
11:	1월	1	0.6
12:	가장	1	0.6
:
29:	새해	4	2.3
:
34:	영하	3	1.7
35:	오늘	2	1.2
:
49:	KBS	1	0.6
50:	강추위	1	0.6
:
96:	강추위로	1	0.6
97:	나왔는데	1	0.6
:
129:	겨울바람이	1	0.6
130:	내일부터는	2	1.2
:
152:	기상전문기자가	1	0.6
153:	끌어내렸습니다	1	0.6


'''

