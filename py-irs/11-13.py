from pathlib import Path
filename1 = Path("./../testtext/hgcode/test1.txt");
encoding='euc-kr'
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import GetWordDictList_WordList
from hgwordlist import GetWordDictList_LenListInfo
from hgwordlist import PrintWordDictListInfo
#---------- word dict
#---------- word dict
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
WordDictList = GetWordDictList_WordList(KeywordList)

LenListInfo = GetWordDictList_LenListInfo(WordDictList)
#print(LenListInfo)
PrintWordDictListInfo(LenListInfo)


'''
처리 결과:
==================================
List Num: 7 List Sum: 153
Total Freq: 173
Freq Filter: 0
{'len': 1, 'count': 10}
{'len': 2, 'count': 37}
{'len': 3, 'count': 48}
{'len': 4, 'count': 29}
{'len': 5, 'count': 13}
{'len': 6, 'count': 13}
{'len': 7, 'count': 3}




'''

