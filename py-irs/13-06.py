import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
#-----------------------------
#-----------------------------
#=print('reading texts')
# foramt: {'word': 1}
DictFreqList = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
#=DictFreqList = load_dictfreq_kbs_01_16()
print('Dict Num:', len(DictFreqList))
WordNum = sum(DictFreqList[dic] for dic in DictFreqList)
print('Word Num:', WordNum)

#-----
#-----
from hgworddistance import FindDisWord_Vocabulary
DisWord = FindDisWord_Vocabulary('대헌민국', DictFreqList, DisNum=10)
print('DisWord Num:', len(DisWord))

print(), print('# 코드 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: kv[0]) # by a->z
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)

print(), print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-freq
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)


'''
처리 결과:
======================================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
Word Num: 1689975
DisWord Num: 15

# 코드 순서 출력
1 : ('강민국', (2, 1))
2 : ('대국', (2, 7))
3 : ('대국민', (2, 20))
4 : ('대국민적', (2, 1))
5 : ('대민', (2, 1))
6 : ('대상국', (2, 4))
7 : ('대선정국', (2, 1))
8 : ('대중국', (2, 2))
9 : ('대치정국', (2, 7))
10 : ('대한민국', (1, 261))
11 : ('대한민보', (2, 1))
12 : ('대한제국', (2, 15))
13 : ('대형약국', (2, 3))
14 : ('최헌국', (2, 1))
15 : ('한민국', (2, 7))

# 편집 거리 순서 출력
1 : ('대한민국', (1, 261))
2 : ('대국민', (2, 20))
3 : ('대한제국', (2, 15))
4 : ('대국', (2, 7))
5 : ('대치정국', (2, 7))
6 : ('한민국', (2, 7))
7 : ('대상국', (2, 4))
8 : ('대형약국', (2, 3))
9 : ('대중국', (2, 2))
10 : ('강민국', (2, 1))
11 : ('대국민적', (2, 1))
12 : ('대민', (2, 1))
13 : ('대선정국', (2, 1))
14 : ('대한민보', (2, 1))
15 : ('최헌국', (2, 1))

'''
