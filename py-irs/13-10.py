import hgsysinc
from hgunicode import hgGetChoJungJongString, hgSyllableStr__Jamo3Str
from hgtest import load_dictfreq_kbs_2009 
from hgworddistance import FindDisWord_Vocabulary
#-----------------------------
#-----------------------------
#=print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
print('Dict Num:', len(DictFreqList))
#=WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
#=print('Word Num:', WordNum)

#-----
print('# 사전을 초성, 중성, 종성 자모로 변환:')
#-----
DictFreq_jamo = {}
for dic in DictFreqList:
    dic_jamo = hgGetChoJungJongString(dic)
    DictFreq_jamo[dic_jamo] = int(DictFreqList[dic])
#
#=word_jamo = hgGetChoJungJongString('죈장') # <-- '된장'
word_jamo = hgGetChoJungJongString('솽장') # <-- '광장'
#=word_jamo = hgGetChoJungJongString('햑신') # <-- '혁신'
print('초성, 중성, 종성 자모 사전 스캔:')
DisWord = FindDisWord_Vocabulary(word_jamo, DictFreq_jamo, DisNum=10, DisMax=0)
print('DisWord Num:', len(DisWord))

print(), print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-freq
for i, x in enumerate(DisWord_Sort):
    #=print((i+1), ':', 자모_음절변환(x[0]) , x[1])
    SyllableStr = hgSyllableStr__Jamo3Str(x[0])
    print((i+1), ':', SyllableStr , x[1])            


'''
처리 결과:
=================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
# 사전을 초성, 중성, 종성 자모로 변환:
초성, 중성, 종성 자모 사전 스캔:
DisWord Num: 65

# 편집 거리 순서 출력
1 : 성장 (1, 277)
2 : 광장 (1, 95)
3 : 상장 (1, 15)
4 : 생장 (1, 7)
5 : 송장 (1, 1)
6 : 황장 (1, 1)
7 : 시장 (2, 466)
8 : 공장 (2, 386)
9 : 사장 (2, 341)
10 : 당장 (2, 281)
11 : 등장 (2, 252)
12 : 청장 (2, 142)
13 : 과장 (2, 138)
14 : 확장 (2, 116)
15 : 상징 (2, 112)
16 : 총장 (2, 109)
17 : 상정 (2, 73)
18 : 심장 (2, 70)
19 : 통장 (2, 70)
20 : 소장 (2, 65)
21 : 상상 (2, 64)
22 : 성당 (2, 58)
23 : 선장 (2, 55)
24 : 영장 (2, 49)
25 : 화장 (2, 49)
26 : 실장 (2, 47)
27 : 신장 (2, 44)
28 : 수장 (2, 43)
29 : 상자 (2, 40)
30 : 상당 (2, 36)
31 : 승자 (2, 36)
32 : 웅장 (2, 28)
33 : 경장 (2, 26)
34 : 농장 (2, 22)
35 : 명장 (2, 22)
36 : 정장 (2, 20)
37 : 관장 (2, 13)
38 : 굉장 (2, 10)
39 : 서장 (2, 9)
40 : 중장 (2, 9)
41 : 성자 (2, 7)
42 : 식장 (2, 6)
43 : 행장 (2, 6)
44 : 병장 (2, 4)
45 : 황당 (2, 4)
46 : 동장 (2, 3)
47 : 왕자 (2, 3)
48 : 좌장 (2, 3)
49 : 산장 (2, 2)
50 : 상강 (2, 2)
51 : 생강 (2, 2)
52 : 석장 (2, 2)
53 : 완장 (2, 2)
54 : 왕징 (2, 2)
55 : 환장 (2, 2)
56 : 냉장 (2, 1)
57 : 상방 (2, 1)
58 : 상중 (2, 1)
59 : 성종 (2, 1)
60 : 세장 (2, 1)
61 : 송정 (2, 1)
62 : 순장 (2, 1)
63 : 왕팡 (2, 1)
64 : 평장 (2, 1)
65 : 황창 (2, 1)

'''
