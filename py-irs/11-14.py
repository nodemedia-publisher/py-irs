import hgsysinc
from hgcrawl import get_filename__Anne_of_Green_Gables
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
#----------
#----------
import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import GetWordDictList_WordList
from hgwordlist import PrintWordDictList
#----------
#----------
KeywordList = GetKeywordList_File(filename1, encoding=encoding)
WordDictList = GetWordDictList_WordList(KeywordList, LowerCasifyFlag=True) # 대문자를 소문자로 통합

# sort by freq high, abc
#= ('---------------- word dict sort freq high -> low, a->z')
print('# @@@ 단어 빈도 (높은) 순서로 정렬(코드 순서로 2차 정렬)')
WordDictList.sort(key = lambda item: (-item['freq'], item['word'])) # by freq high, abc
PrintWordDictList(WordDictList, OneLine=True, 
    PrintIndex=True, SimpleFormat=True, RateFlag=True)



'''
처리 결과:
==================================
# @@@ 단어 빈도 (높은) 순서로 정렬(코드 순서로 2차 정렬)
TotalWordFreq: 106775
순서	단어	빈도	점유율
1:	the	3925	3.7
2:	and	3395	3.2
3:	i	3265	3.1
4:	to	3042	2.8
5:	a	2226	2.1
6:	it	2098	2.0
7:	of	1914	1.8
8:	you	1700	1.6
9:	she	1519	1.4
10:	in	1479	1.4
11:	that	1371	1.3
12:	was	1364	1.3
13:	her	1315	1.2
14:	anne	1207	1.1
15:	t	1189	1.1
16:	s	1151	1.1
17:	marilla	851	0.8
18:	but	849	0.8
19:	be	820	0.8
20:	as	791	0.7
21:	with	790	0.7
22:	had	772	0.7
23:	for	734	0.7
24:	said	640	0.6
25:	so	638	0.6
26:	at	616	0.6
27:	on	577	0.5
28:	have	566	0.5
29:	all	544	0.5
30:	is	544	0.5
31:	me	535	0.5
32:	he	490	0.5
33:	when	466	0.4
34:	up	457	0.4
35:	if	455	0.4
36:	not	444	0.4
37:	there	441	0.4
38:	diana	415	0.4
39:	mrs	406	0.4
40:	my	397	0.4
41:	out	382	0.4
42:	matthew	363	0.3
43:	m	362	0.3
44:	just	358	0.3
45:	would	344	0.3
46:	over	332	0.3
47:	don	326	0.3
48:	ll	325	0.3
49:	what	319	0.3
50:	were	318	0.3
:
:
7591:   yarn    1       0.0
7592:   yelling 1       0.0
7593:   yellowish-brown 1       0.0
7594:   yellowish-gray  1       0.0
7595:   yellowish-green 1       0.0
7596:   younger 1       0.0
7597:   youngest        1       0.0
7598:   yourselves      1       0.0

'''

