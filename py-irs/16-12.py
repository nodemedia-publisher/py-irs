import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie
from hgkbd import HGTransString2KBDJamo
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
#=TrieTest.MakeTrie__DictFreq(Vocabulary) # 이 함수는 이미 NGram과 한영 변환이 적용되니까 예제에서는 사용 안 함.
for CurWord in Vocabulary:
    WordFreq = Vocabulary[CurWord]
    KBDCharString = HGTransString2KBDJamo(CurWord)
    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '한국방송'
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글 음절->두벌식 자모 변환
#=print(f'{FindWord}:{FindWord_KBDjamo}')
SugList = TrieTest.GetSuggestion(FindWord_KBDjamo)
print(), print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList)}:')
#=print(), print(f'<{FindWord}> Suggest {len(SugList)}:')
#=print(*SugList, sep='\n')
for i, x in enumerate(SugList):
    print(f"{i+1}, {x['realword']}({x['weight']})")


'''
이 모듈은 TrieTest.GetSuggestion() 함수를 사용하는 버전이다.
========================================
출력 결과:
========================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 두벌식 자모로 변환하여 트라이를 생성한다.
========================================
<한국방송(<===ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ)> Suggest 10:
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




