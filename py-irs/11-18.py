import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import PrintWordDictList
from hgwordlist import GetBackWordDictList__WordList
from hgcrawl import get_filename__Anne_of_Green_Gables
print ('---------------- back-word dict')
# ver 1
#--------------------
#--------------------
# 빨강 머리 앤
filename1 = get_filename__Anne_of_Green_Gables() # {빨강 머리 앤}의 파일 경로
# 해당 파일이 있는지 검사하여 없으면 다운로드한다.
from pathlib import Path
file_check = Path(filename1)
if ((file_check.is_file() == True) and (file_check.exists() == True)):
        pass
else:
    from hgcrawl import download_gutenberg_Anne_of_Green_Gables
    download_gutenberg_Anne_of_Green_Gables()
#-----
encoding='utf-8' 
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
#=BackWordDictList = GetBackWordDictList__WordList(KeywordList)
BackWordDictList = GetBackWordDictList__WordList(KeywordList, LowerCasifyFlag=True) # 대문자를 소문자로 통합
BackWordDictList.sort(key = lambda item: (item['word'])) # by abc
#=print ('BackWordDictList : 데이터 그대로 출력')
#=PrintWordDictList(BackWordDictList, OneLine=True, PrintIndex=True, SimpleFormat=True)
#=print (),
print ('BackWordDictList : 출력할 때 [BackwardFlag] 적용')
PrintWordDictList(BackWordDictList, OneLine=True, 
    PrintIndex=True, SimpleFormat=True, BackwardFlag=True)



'''
처리 결과:
=====================
순서	단어	빈도	점유율
1:	c.s.	1	0.0
2:	p.s.	1	0.0
3:	a	2226	2.1
4:	canada	2	0.0
5:	veranda	1	0.0
6:	miranda	1	0.0
7:	rhoda	1	0.0
8:	idea	15	0.0
9:	avonlea	92	0.1
10:	plea	2	0.0
11:	sea	11	0.0
12:	tea	58	0.1
.........
7596:	bronzy	2	0.0
7597:	cozy	1	0.0
7598:	dizzy	4	0.0

'''
