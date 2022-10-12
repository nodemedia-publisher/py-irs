import hgsysinc
from hgtest import load_textlist_us_president
from hgdict import MakeDictFreqList__EngTextList
#-----------------------------
#-----------------------------
#=print('reading texts')
us_president = load_textlist_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#-----------------------------
#-----------------------------
# foramt: {'word': {13: 1, 27: 1, 30: 1, 47: 1}}
DictFreqList = MakeDictFreqList__EngTextList(us_president)
print('Dict Num:', len(DictFreqList))
WordNum = sum(DictFreqList[dic][df_k] for dic in DictFreqList for df_k in DictFreqList[dic])
print('Word Num:', WordNum)

#-----
#-----
from hgworddistance import FindDisWord_Vocabulary
#-----
# 아래 FindDisWord_Vocabulary() 함수에서 {DisMax} 매개변수를 '0'으로 지정해서 
# 편집 거래 최대 한계를 계산하지 않도록 했다.
# 지정값은 '3'으로 편집 거리가 3보다 크면 사실상 어색한 단어가 많아서 
# 찾아봤자 쓸모없지만 이 함수의 결과가 어떤 지 살펴보려면 '0'으로 바꿨다.
# 알고리즘 설명을 위해서 {DisMax} 매개변수를 '0'으로 지정한다.
# {DisMax} 변수의 차이를 설명하려고 바꾼다.
#-----
print('EditDistance: 1글자 빠진 상태')
#=DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=0, DisMax=0) # 모두 출력
DisWord = FindDisWord_Vocabulary('govenment', DictFreqList, DisNum=10, DisMax=0)
print('DisWord Num:', len(DisWord))

print('# 코드 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: kv[0]) # by a->z
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)
print()
print('# 편집 거리 순서 출력')
DisWord_Sort = sorted(DisWord.items(), key=lambda kv: (kv[1][0], -kv[1][1])) # by low value(distance), high-doc-num
for i, x in enumerate(DisWord_Sort):
    print((i+1), ':', x)


'''
처리 결과
==========================
Dict Num: 9110
Word Num: 136767
EditDistance: 1글자 빠진 상태
DisWord Num: 33
# 코드 순서 출력
1 : ('agreement', (4, 4))
2 : ('amendment', (4, 7))
3 : ('cement', (4, 3))
4 : ('concernment', (4, 2))
5 : ('consent', (4, 7))
6 : ('content', (4, 5))
7 : ('contentment', (4, 4))
8 : ('convenient', (3, 1))
9 : ('covenant', (3, 4))
10 : ('covenants', (4, 2))
11 : ('dependent', (4, 4))
12 : ('divergent', (4, 1))
13 : ('document', (4, 1))
14 : ('element', (4, 6))
15 : ('govern', (4, 12))
16 : ('governed', (4, 7))
17 : ('governing', (4, 6))
18 : ('government', (1, 54))
19 : ('governmental', (3, 5))
20 : ('governments', (2, 29))
21 : ('governs', (4, 1))
22 : ('investment', (4, 4))
23 : ('lenient', (4, 1))
24 : ('moment', (4, 22))
25 : ('monument', (4, 1))
26 : ('movement', (2, 6))
27 : ('movements', (3, 4))
28 : ('obedient', (4, 1))
29 : ('ornament', (4, 2))
30 : ('overset', (4, 1))
31 : ('resentment', (4, 1))
32 : ('reverent', (4, 1))
33 : ('torment', (4, 1))

# 편집 거리 순서 출력
1 : ('government', (1, 54))
2 : ('governments', (2, 29))
3 : ('movement', (2, 6))
4 : ('governmental', (3, 5))
5 : ('movements', (3, 4))
6 : ('covenant', (3, 4))
7 : ('convenient', (3, 1))
8 : ('moment', (4, 22))
9 : ('govern', (4, 12))
10 : ('consent', (4, 7))
11 : ('amendment', (4, 7))
12 : ('governed', (4, 7))
13 : ('element', (4, 6))
14 : ('governing', (4, 6))
15 : ('content', (4, 5))
16 : ('dependent', (4, 4))
17 : ('agreement', (4, 4))
18 : ('contentment', (4, 4))
19 : ('investment', (4, 4))
20 : ('cement', (4, 3))
21 : ('ornament', (4, 2))
22 : ('concernment', (4, 2))
23 : ('covenants', (4, 2))
24 : ('overset', (4, 1))
25 : ('governs', (4, 1))
26 : ('document', (4, 1))
27 : ('lenient', (4, 1))
28 : ('divergent', (4, 1))
29 : ('reverent', (4, 1))
30 : ('obedient', (4, 1))
31 : ('monument', (4, 1))
32 : ('torment', (4, 1))
33 : ('resentment', (4, 1))

'''

