import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie
from hgkbd import HGTransString2KBDJamo
#---------------
#---------------
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
    KBDCharString = HGTransString2KBDJamo(CurWord) # 한글 음절->두벌식 자모 변환
    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '맛' # 325 단어
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글 음절->두벌식 자모 변환
SugList = TrieTest.FindWord(FindWord_KBDjamo)
#=print(len(SugList), ':', SugList)
SugList_Sort = sorted(SugList, key=lambda item: -item['weight']) # by high
#=print(len(SugList_Sort), ':', SugList_Sort)

print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList_Sort)}:')
#=print(f'<{FindWord}> Suggest {len(SugList_Sort)}:')
print(*SugList_Sort[:10], sep='\n') # 10개만 출력



'''
출력 결과:
=============================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 두벌식 자모로 변환하여 트라이를 생성한다.
=============================================
<맛(<===ㅁㅏㅅ)> Suggest 325:
{'word': 'ㅁㅏㅅㅣㄷㅏ', 'realword': '마시다', 'weight': 4352}
{'word': 'ㅁㅏㅅ', 'realword': '맛', 'weight': 1643}
{'word': 'ㅁㅏㅅㅡㅋㅡ', 'realword': '마스크', 'weight': 909}
{'word': 'ㅁㅏㅅㅂㅗㄷㅏ', 'realword': '맛보다', 'weight': 862}
{'word': 'ㅁㅏㅅㅇㅣㅆㄷㅏ', 'realword': '맛있다', 'weight': 748}
{'word': 'ㅁㅏㅅㅏㄴ', 'realword': '마산', 'weight': 453}
{'word': 'ㅁㅏㅅㅡㅌㅓㅅㅡ', 'realword': '마스터스', 'weight': 326}
{'word': 'ㅁㅏㅅㅡㅋㅗㅌㅡ', 'realword': '마스코트', 'weight': 275}
{'word': 'ㅁㅏㅅㅏㅎㅗㅣ', 'realword': '마사회', 'weight': 184}
{'word': 'ㅁㅏㅅㅜㄹ', 'realword': '마술', 'weight': 176}

'''




