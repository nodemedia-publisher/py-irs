import hgsysinc
from hgkbd import HGTransString2KBDJamo, HGGetSyllable_JaumMoumString
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
print('# 사전을 두벌식 자모로 변환:')
#-----
DictFreq_KBDJamo = {}
for dic in DictFreqList:
    dic_jamo = HGTransString2KBDJamo(dic) # 두벌식 자모 문자열로 변환
    DictFreq_KBDJamo[dic_jamo] = int(DictFreqList[dic])
# '솽장' <-- '광장'
kbd_jamo = HGTransString2KBDJamo('솽장') # 두벌식 자모 문자열로 변환
print('두벌식 자모 사전 스캔:')
DisWord = FindDisWord_Vocabulary(kbd_jamo, DictFreq_KBDJamo, DisNum=10)
print('DisWord Num:', len(DisWord))

print(), print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-freq
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', HGGetSyllable_JaumMoumString(x[0]) , x[1])            
    

'''
처리 결과:
===========================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
# 사전을 두벌식 자모로 변환:
두벌식 자모 사전 스캔:
DisWord Num: 42

# 편집 거리 순서 출력
1 : 광장 (1, 95)
2 : 상장 (1, 15)
3 : 소방장 (1, 2)
4 : 송장 (1, 1)
5 : 황장 (1, 1)
6 : 공장 (2, 386)
7 : 사장 (2, 341)
8 : 당장 (2, 281)
9 : 성장 (2, 277)
10 : 과장 (2, 138)
11 : 확장 (2, 116)
12 : 상징 (2, 112)
13 : 총장 (2, 109)
14 : 상정 (2, 73)
15 : 통장 (2, 70)
16 : 소장 (2, 65)
17 : 상상 (2, 64)
18 : 화장 (2, 49)
19 : 상자 (2, 40)
20 : 상당 (2, 36)
21 : 농장 (2, 22)
22 : 관장 (2, 13)
23 : 굉장 (2, 10)
24 : 생장 (2, 7)
25 : 소각장 (2, 4)
26 : 황당 (2, 4)
27 : 동장 (2, 3)
28 : 왕자 (2, 3)
29 : 좌장 (2, 3)
30 : 산장 (2, 2)
31 : 상강 (2, 2)
32 : 소장자 (2, 2)
33 : 완장 (2, 2)
34 : 왕징 (2, 2)
35 : 환장 (2, 2)
36 : 상방 (2, 1)
37 : 상중 (2, 1)
38 : 소송장 (2, 1)
39 : 소포장 (2, 1)
40 : 송정 (2, 1)
41 : 왕팡 (2, 1)
42 : 황창 (2, 1)

'''
