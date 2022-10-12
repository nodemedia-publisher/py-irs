import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import HGTrie
from hgkbd import HGTransString2KBDJamo, HGGetJaumMoum__EngString
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
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
    #=TrieTest.InsertWord(CurWord, RealWord=CurWord, Weight=WordFreq)
    KBDCharString = HGTransString2KBDJamo(CurWord) # 한글->두벌식 자모
    #=TrieTest.InsertNode(CurWord, Weight=WordFreq)
    TrieTest.InsertNode(KBDCharString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()

#=# 임시로 자동 추천 단어수를 늘린다.
#=TrieTest.Opt_SuggestNum = 550

#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = 'gksrnr' # '한국' 한영변환 오류 입력
SugList = TrieTest.GetSuggestion(FindWord) # 영문자 단어로 자동 추천
print(f'<{FindWord}> Suggest {len(SugList)}:')

if(len(SugList) <= 0): # 추천 목록이 없는 경우
    # [영문자==>두벌식 자모] 방식(직접변환)
    FindWord_KBDjamo = HGGetJaumMoum__EngString(FindWord) # 영문자->두벌식 자모
    SugList = TrieTest.GetSuggestion(FindWord_KBDjamo) # 두벌식 자모로 자동 추천
    print(f'<{FindWord}(<=={FindWord_KBDjamo})> Suggest {len(SugList)}:')
#---
print(*SugList, sep='\n')


'''
출력 결과:
========================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.
========================================
<gksrnr> Suggest 0:
<gksrnr(<==ㅎㅏㄴㄱㅜㄱ)> Suggest 10:
{'word': 'ㅎㅏㄴㄱㅜㄱ', 'realword': '한국', 'weight': 26326}
{'word': 'ㅎㅏㄴㄱㅜㄱㅇㅣㄴ', 'realword': '한국인', 'weight': 5808}
{'word': 'ㅎㅏㄴㄱㅜㄱㅊㅜㄱㄱㅜ', 'realword': '한국축구', 'weight': 2469}
{'word': 'ㅎㅏㄴㄱㅜㄱㅇㅡㄴㅎㅐㅇ', 'realword': '한국은행', 'weight': 1719}
{'word': 'ㅎㅏㄴㄱㅜㄱㅅㅣㄹㅣㅈㅡ', 'realword': '한국시리즈', 'weight': 1528}
{'word': 'ㅎㅏㄴㄱㅜㄱㅈㅓㅇㅂㅜ', 'realword': '한국정부', 'weight': 912}
{'word': 'ㅎㅏㄴㄱㅜㄱㅅㅓㄴㅅㅜ', 'realword': '한국선수', 'weight': 830}
{'word': 'ㅎㅏㄴㄱㅜㄱㅈㅓㄴㄹㅕㄱ', 'realword': '한국전력', 'weight': 812}
{'word': 'ㅎㅏㄴㄱㅜㄱㅈㅓㄴㅈㅐㅇ', 'realword': '한국전쟁', 'weight': 644}
{'word': 'ㅎㅏㄴㄱㅜㄱㄴㅗㅊㅗㅇ', 'realword': '한국노총', 'weight': 639}

'''



