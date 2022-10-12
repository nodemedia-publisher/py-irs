import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import MatchPrefix_SortDict_naive
from hgfind import PrintMatchDictFreq
#----------
#----------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
MatchDict = MatchPrefix_SortDict_naive('가격', Vocabulary)

# 접두사 일치 단어 빈도 순 정렬
list_by_values = sorted(MatchDict.items(), key=lambda item: -item[1]) # by high
MatchDict_Sort = dict(list_by_values) # list_by_values: [(key, value),...]
PrintMatchDictFreq('가격', MatchDict_Sort, 'dict type:')

'''
출력 결과:
===========================================================
@@@ [KBS 9시 뉴스] @@@
Dict Num: 413165

#-----------------------------
@@@  dict type: @@@
#-----------------------------
prefix [가격]: 77
1, 가격 : 7286
2, 가격경쟁력 : 287
3, 가격인상 : 195
4, 가격인하 : 179
5, 가격상승 : 131
6, 가격경쟁 : 127
7, 가격차이 : 125
8, 가격담합 : 110
9, 가격하락 : 104
10, 가격대 : 84
11, 가격표 : 82
12, 가격차 : 70
13, 가격안정 : 65
14, 가격거품 : 52
15, 가격할인 : 52
16, 가격급등 : 48
17, 가격폭락 : 39
18, 가격협상 : 32
19, 가격정보 : 30
20, 가격파괴 : 30
21, 가격폭등 : 30
22, 가격대비 : 29
23, 가격표시 : 29
24, 가격부담 : 25
25, 가격표시제 : 25
26, 가격변동 : 24
27, 가격비교 : 24
28, 가격정책 : 22
29, 가격하락세 : 21
30, 가격적 : 20
31, 가격입찰 : 18
32, 가격상승률 : 17
33, 가격통제 : 17
34, 가격조정 : 16
35, 가격상승세 : 14
36, 가격구조 : 13
37, 가격기준 : 12
38, 가격동향 : 11
39, 가격비교사이트 : 9
40, 가격조건 : 9
41, 가격제한폭 : 8
42, 가격책정 : 8
43, 가격표시판 : 7
44, 가격후려치기 : 6
45, 가격인상폭 : 4
46, 가격면 : 3
47, 가격상 : 3
48, 가격제 : 3
49, 가격판 : 3
50, 가격폭 : 3
51, 가격품목 : 3
52, 가격경 : 1
53, 가격경쟁력을키울 : 1
54, 가격기준대 : 1
55, 가격낮추기 : 1
56, 가격댑니 : 1
57, 가격때문 : 1
58, 가격률 : 1
59, 가격망 : 1
60, 가격산정안 : 1
61, 가격선 : 1
62, 가격안 : 1
63, 가격에는팔지 : 1
64, 가격에제품 : 1
65, 가격요인 : 1
66, 가격이더 : 1
67, 가격이라곤생각 : 1
68, 가격입 : 1
69, 가격전 : 1
70, 가격제한선 : 1
71, 가격조사기관 : 1
72, 가격증 : 1
73, 가격지지 : 1
74, 가격지지형 : 1
75, 가격투찰 : 1
76, 가격표시라는지 : 1
77, 가격협의 : 1

'''
