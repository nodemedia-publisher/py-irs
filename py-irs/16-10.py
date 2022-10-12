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
    KBDCharString = HGTransString2KBDJamo(CurWord)
    #=TrieTest.InsertWord(CurWord, Weight=WordFreq) # RealWord=? 사용하지 않는 버전
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()
#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '한국방송'
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글 음절->두벌식 자모 변환
SugList = TrieTest.FindWord(FindWord_KBDjamo)
#=print(len(SugList), ':', SugList)

SugList_Sort = sorted(SugList, key=lambda item: -item['weight']) # by high
#=print(len(SugList_Sort), ':', SugList_Sort)
print(f'<{FindWord}(<==={FindWord_KBDjamo})> Suggest {len(SugList_Sort)}:')
#=print(f'<{FindWord}> Suggest {len(SugList_Sort)}:')
print(*SugList_Sort[:12], sep='\n') # 12개까지 출력




'''
출력 결과:
=============================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.

한글 음절로 된 단어를 두벌식 자모로 변환하여 트라이를 생성한다.
=============================================
<한국방송(<===ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ)> Suggest 17:
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅕㅂㅎㅗㅣ', 'realword': '한국방송협회', 'weight': 67}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄷㅐㅅㅏㅇ', 'realword': '한국방송대상', 'weight': 25}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅣㅈㅏㅋㅡㄹㄹㅓㅂ', 'realword': '한국방송기자클럽', 'weight': 22}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅏㅇㄱㅗㄱㅗㅇㅅㅏ', 'realword': '한국방송광고공사', 'weight': 19}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅕㅂㅎㅗㅣㅈㅏㅇ', 'realword': '한국방송협회장', 'weight': 13}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅎㅏㄱㅎㅗㅣ', 'realword': '한국방송학회', 'weight': 12}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅇㅅㅏ', 'realword': '한국방송공사', 'weight': 11}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅇㅕㅇㅅㅏㅇㅅㅏㄴㅇㅓㅂㅈㅣㄴㅎㅡㅇㅇㅜㅓㄴ', 'realword': '한국방송영상산업진흥원', 'weight': 8}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㄱㅗㅏㅇㄱㅗㅈㅣㄴㅎㅡㅇㄱㅗㅇㅅㅏ', 'realword': '한국방송광고진흥공사', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅋㅏㅁㅔㄹㅏㄱㅣㅈㅏㅎㅕㅂㅎㅗㅣ', 'realword': '한국방송카메라기자협회', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅌㅗㅇㅅㅣㄴㄷㅐㅎㅏㄱㄱㅛ', 'realword': '한국방송통신대학교', 'weight': 7}
{'word': 'ㅎㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇㅌㅗㅇㅅㅣㄴㄷㅐㅎㅏㄱ', 'realword': '한국방송통신대학', 'weight': 4}


'''




