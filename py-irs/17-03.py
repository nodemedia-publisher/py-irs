import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie, __Hng_AsItIs__
from hgkbd import HGTransString2EngString, HGTransString2KBDJamo
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()# [KBS 9시 뉴스: 16년치(2001~2016)]
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie() 
#=# 편집용 옵션 조정
#=TrieTest.Opt_Hng_Fmt = __Hng_AsItIs__ # 한글: 변형없이 그대로 처리(음절)(기본값은 __Hng_2_Jamo__[한글=>두벌식자모])

#=TrieTest.MakeTrie__DictFreq(Vocabulary) # 이 함수는 이미 NGram과 한영 변환이 적용되니까 예제에서는 사용 안 함.
for CurWord in Vocabulary:
    WordFreq = Vocabulary[CurWord]
    CurWord = CurWord.lower() # 소문자 변환
    #=TrieTest.InsertWord(CurWord, RealWord=CurWord, Weight=WordFreq)
    KBDCharString = HGTransString2KBDJamo(CurWord) # 한글->두벌식 자모
    #=TrieTest.InsertNode(CurWord, Weight=WordFreq)
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()

#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = 'ㄹㅊ' # 'fc' 한영변환 오류 입력
SugList = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList)}:')

if(len(SugList) <= 0): # 추천 목록이 없는 경우
    # [한글==>영문자] 방식
    FindWord_EngString = HGTransString2EngString(FindWord) # 한글->영문자 변환
    SugList = TrieTest.GetSuggestion(FindWord_EngString)
    print(f'<{FindWord}(<=={FindWord_EngString})> Suggest {len(SugList)}:')
#---
print(*SugList, sep='\n')



'''
출력 결과:
=========================================
영한 변환 오류 입력하면 한영 변환 자동 추천
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
[KBS 9시 뉴스: 16년치] @@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
<ㄹㅊ> Suggest 0:
<ㄹㅊ(<==fc)> Suggest 10:
{'word': 'fcㅅㅓㅇㅜㄹ', 'realword': 'fc서울', 'weight': 410}
{'word': 'fcㅂㅏㄹㅡㅅㅔㄹㄹㅗㄴㅏ', 'realword': 'fc바르셀로나', 'weight': 67}
{'word': 'fc ㅂㅏㄹㅡㅅㅔㄹㄹㅗㄴㅏ', 'realword': 'fc 바르셀로나', 'weight': 53}
{'word': 'fc ㅍㅗㄹㅡㅌㅜ', 'realword': 'fc 포르투', 'weight': 30}
{'word': 'fcㄷㅗㅋㅛ', 'realword': 'fc도쿄', 'weight': 18}
{'word': 'fc ㅁㅔㅅㅡ', 'realword': 'fc 메스', 'weight': 14}
{'word': 'fcㅁㅔㅅㅡ', 'realword': 'fc메스', 'weight': 11}
{'word': 'fc ㅇㅏㄴㅇㅑㅇ', 'realword': 'fc 안양', 'weight': 10}
{'word': 'fc ㄷㅗㅋㅛ', 'realword': 'fc 도쿄', 'weight': 8}
{'word': 'fc', 'realword': 'fc', 'weight': 5}


'''


