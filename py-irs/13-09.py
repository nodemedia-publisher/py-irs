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
    dic_jamo = hgGetChoJungJongString(dic) # 초성, 중성, 종성 자모 문자열로 변환
    DictFreq_jamo[dic_jamo] = int(DictFreqList[dic])
#
word_jamo = hgGetChoJungJongString('마국경제') # 초성, 중성, 종성 자모 문자열로 변환
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
======================
@@@ [KBS 9시 뉴스] @@@
@@@ @@@ [토큰처리] -  {주제어}
file: ..\testtext\hgdatsci\_kbs_2009_\2009.가나순_WordList.txt
Dict Num: 99989
# 사전을 초성, 중성, 종성 자모로 변환:
초성, 중성, 종성 자모 사전 스캔:
DisWord Num: 25

# 편집 거리 순서 출력
1 : 미국경제 (1, 14)
2 : 한국경제 (2, 64)
3 : 중국경제 (3, 7)
4 : 세계경제 (4, 101)
5 : 국경 (4, 38)
6 : 지역경제 (4, 25)
7 : 미국령 (4, 10)
8 : 가격경쟁 (4, 8)
9 : 국가경제 (4, 8)
10 : 국내경제 (4, 7)
11 : 미국여자 (4, 4)
12 : 박경재 (4, 4)
13 : 자궁경부 (4, 4)
14 : 지식경제 (4, 4)
15 : 국제경제 (4, 3)
16 : 계획경제 (4, 2)
17 : 미경제 (4, 2)
18 : 가격통제 (4, 1)
19 : 가정경제 (4, 1)
20 : 국경절 (4, 1)
21 : 미국명 (4, 1)
22 : 미국영화 (4, 1)
23 : 미국제 (4, 1)
24 : 사회경제 (4, 1)
25 : 서울경제 (4, 1)

'''
