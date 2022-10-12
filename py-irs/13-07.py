import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
#-----------------------------
#-----------------------------
print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
#=DictFreqList = load_dictfreq_kbs_01_16()
print('Dict Num:', len(DictFreqList))
#=WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
#=print('Word Num:', WordNum)

#-----
#-----
from hgworddistance import FindDisWord_Vocabulary
DisWord = FindDisWord_Vocabulary('마국경제', DictFreqList, DisNum=10)
print('DisWord Num:', len(DisWord))

print(), print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-freq
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)


'''
처리 결과:
==========================================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
DisWord Num: 42

# 편집 거리 순서 출력
1 : ('한국경제', (1, 64))
2 : ('미국경제', (1, 14))
3 : ('중국경제', (1, 7))
4 : ('경제', (2, 343))
5 : ('국제', (2, 216))
6 : ('세계경제', (2, 101))
7 : ('국경', (2, 38))
8 : ('지역경제', (2, 25))
9 : ('마취제', (2, 20))
10 : ('서민경제', (2, 18))
11 : ('실물경제', (2, 12))
12 : ('북한경제', (2, 11))
13 : ('국가경제', (2, 8))
14 : ('국내경제', (2, 7))
15 : ('일본경제', (2, 7))
16 : ('시장경제', (2, 6))
17 : ('한국경찰', (2, 5))
18 : ('마경찬', (2, 4))
19 : ('우리경제', (2, 4))
20 : ('지식경제', (2, 4))
21 : ('국민경제', (2, 3))
22 : ('국제경제', (2, 3))
23 : ('대외경제', (2, 3))
24 : ('중국제', (2, 3))
25 : ('지하경제', (2, 3))
26 : ('계획경제', (2, 2))
27 : ('국경일', (2, 2))
28 : ('미경제', (2, 2))
29 : ('한국제', (2, 2))
30 : ('가정경제', (2, 1))
31 : ('국경넘', (2, 1))
32 : ('국경절', (2, 1))
33 : ('마산경기', (2, 1))
34 : ('미국제', (2, 1))
35 : ('사회경제', (2, 1))
36 : ('서울경제', (2, 1))
37 : ('신경제', (2, 1))
38 : ('신국제', (2, 1))
39 : ('외국제', (2, 1))
40 : ('전경제', (2, 1))
41 : ('정국경색', (2, 1))
42 : ('지방경제', (2, 1))

'''
