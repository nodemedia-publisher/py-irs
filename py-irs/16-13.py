import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie, __Hng_2_Jamo__
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16() # [KBS 9시 뉴스: 16년치(2001~2016)]
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie() 
TrieTest.Opt_Hng_Fmt = __Hng_2_Jamo__ # 한글: 두벌식(키보드) 자모로 처리
TrieTest.MakeTrie__DictFreq(Vocabulary)
#-----------------------------
#=for CurWord in Vocabulary:
#=    WordFreq = Vocabulary[CurWord]
#=    KBDCharString = HGTransString2KBDJamo(CurWord)
#=    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
#=    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#-----------------------------
#=#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '한국방송'
SugList = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList)}:')
#=print(*SugList, sep='\n')
for i, x in enumerate(SugList):
    print(f"{i+1}, {x['realword']}({x['weight']})")

#=from hgkbd import HGTransString2KBDJamo
#=FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글 음절->키보드 자모 변환
#=print(f'{FindWord}:{FindWord_KBDjamo}')
#=print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList)}:')


'''
========================================
이 모듈은 TrieTest.GetSuggestion() 함수를 사용하는 버전이다.
이 모듈은 사전을 트라이로 변환하고 검색할 때 외부에서 두벌식 자모 변환을 하지 않는다. 
대신에 트라이를 생성한 후 한글 처리를 
{Opt_Hng_Fmt = __Hng_2_Jamo__ # 한글: 키보드 자모로 처리}로 하라고 지정한다.

이전에 사용한 개별 코드를 사용하지 않고 
기본적인 함수만으로 검색어를 추천하는 것을 목적으로 한다.
========================================
출력 결과:
========================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 키보드 자모로 변환하여 트라이를 생성한다.
========================================
<한국방송> Suggest 10:
1, 한국방송협회(67)
2, 한국방송대상(25)
3, 한국방송기자클럽(22)
4, 한국방송광고공사(19)
5, 한국방송협회장(13)
6, 한국방송학회(12)
7, 한국방송공사(11)
8, 한국방송영상산업진흥원(8)
9, 한국방송통신대학교(7)
10, 한국방송카메라기자협회(7)


'''




