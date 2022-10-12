import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind import HGTrie, __Hng_AsItIs__
from hgkbd import HGTransString2EngString
from hgkbd import HGTransString2KBDJamo
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
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
    TrieTest.InsertNode(CurWord, Weight=WordFreq)
    #=KBDCharString = HGTransString2KBDJamo(CurWord) # 한글->키보드 자모(여기서 영어 사전이라서 바뀌는 것은 없다.)
    #=TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=print('CountTrie:', TrieTest.CountTrie())

#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = '햎ㄷ' # 'gove' 한영변환 오류 입력
SugList = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList)}:')

if(len(SugList) <= 0): # 추천 목록이 없는 경우
    # [한글==>영문자] 방식
    FindWord_EngString = HGTransString2EngString(FindWord) # 한->영 입력 변환
    SugList = TrieTest.GetSuggestion(FindWord_EngString)
    print(f'<{FindWord}(<=={FindWord_EngString})> Suggest {len(SugList)}:')
#---
print(*SugList, sep='\n')



'''
출력 결과:


영한 변환 오류 입력하면 한영 변환 자동 추천


@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
<햎ㄷ> Suggest 0:
<햎ㄷ(<==gove)> Suggest 7:
{'word': 'government', 'realword': '', 'weight': 607}
{'word': 'governments', 'realword': '', 'weight': 52}
{'word': 'govern', 'realword': '', 'weight': 19}
{'word': 'governed', 'realword': '', 'weight': 10}
{'word': 'governmental', 'realword': '', 'weight': 8}
{'word': 'governing', 'realword': '', 'weight': 6}
{'word': 'governs', 'realword': '', 'weight': 1}


'''




