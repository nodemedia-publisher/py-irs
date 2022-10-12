import hgsysinc
from hgwordlist import GetKeywordList_File
from hgwordlist import PrintWordDictList
from hgwordlist import GetBackWordDictList__WordList, BackWordDictList_Suffix
from hgcrawl import get_filename__Anne_of_Green_Gables
#-----------------------------
#-----------------------------
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

#=Suffix = 'able'
#=Suffix = 'ful'
#=Suffix = 'ly'
#=Suffix = 'tic'
#=Suffix = 'ible'
#=Suffix = 'ion'
#=Suffix = 'less'
#=Suffix = 'ous'
#=Suffix = 'ment'
#=Suffix = 'est'
#=Suffix = 'bly'
Suffix = 'ness'
BackWordDictList_Suffix = BackWordDictList_Suffix(BackWordDictList, Suffix)

print('# 빈도 높은 순 정렬')
print(f'[-{Suffix}] word num:', len(BackWordDictList_Suffix))
BackWordDictList_Suffix.sort(key = lambda item: (-item['freq'])) # by high -> low
PrintWordDictList(BackWordDictList_Suffix, OneLine=True, 
    PrintIndex=True, SimpleFormat=True, BackwardFlag=True, RateFlag=False)


'''
처리 결과:
=====================
---------------- back-word dict
# 빈도 높은 순 정렬
[-ness] word num: 66
순서    단어    빈도

1:      goodness        14
2:      business        11
3:      consciousness   9
4:      darkness        7
5:      happiness       5
6:      sweetness       5
7:      loveliness      4
8:      weakness        4
9:      bitterness      4
10:     kindness        3
11:     crispness       3
12:     gladness        2
13:     bareness        2
14:     foolishness     2
15:     steadiness      2
16:     stinginess      2
17:     loneliness      2
18:     homesickness    2
19:     illness 2
20:     cheerfulness    2
21:     harness 2
22:     wilderness      2
23:     nervousness     2
24:     fitness 2
25:     shyness 2
26:     dumbness        1
27:     unaccustomedness        1
28:     paleness        1
29:     sameness        1
30:     goneness        1
31:     blueness        1
32:     forgiveness     1
33:     undemonstrativeness     1
34:     thoroughness    1
35:     freshness       1
36:     smoothness      1
37:     spiciness       1
38:     readiness       1
39:     holiness        1
40:     skinniness      1
41:     skimpiness      1
42:     unhappiness     1
43:     weariness       1
44:     heaviness       1
45:     sickness        1
46:     stillness       1
47:     fulness 1
48:     untruthfulness  1
49:     thankfulness    1
50:     thoughtfulness  1
51:     suddenness      1
52:     plainness       1
53:     stubbornness    1
54:     tenderness      1
55:     heedlessness    1
56:     carelessness    1
57:     harmlessness    1
58:     helplessness    1
59:     powerlessness   1
60:     softness        1
61:     brightness      1
62:     faintness       1
63:     promptness      1
64:     smartness       1
65:     grayness        1
66:     slyness 1


'''
