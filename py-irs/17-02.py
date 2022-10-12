import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgkbd import HGTransString2EngString
from hgfind import HGTrie
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
    EngString = HGTransString2EngString(CurWord) # 한글->영문자
    #=TrieTest.InsertNode(CurWord, Weight=WordFreq)
    TrieTest.InsertNode(EngString, RealWord=CurWord, Weight=WordFreq)
#=TrieTest.PrintTrie()

#=# 임시로 자동 추천 단어수를 늘린다.
#=TrieTest.Opt_SuggestNum = 550

#-----------------------------
#-----------------------------
# 트라이 추천(Suggestion)
FindWord = 'gksrnr' # '한국' 한영 변환 오류 입력
SugList = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList)}:')
print(*SugList, sep='\n')


'''
출력 결과:
========================================
이 예제는 [KBS 9시 뉴스 16년치] 사전 목록을 사용한다.
========================================
<gksrnr> Suggest 10:
{'word': 'gksrnr', 'realword': '한국', 'weight': 26326}
{'word': 'gksrnrdls', 'realword': '한국인', 'weight': 5808}
{'word': 'gksrnrcnrrn', 'realword': '한국축구', 'weight': 2469}
{'word': 'gksrnrdmsgod', 'realword': '한국은행', 'weight': 1719}
{'word': 'gksrnrtlflwm', 'realword': '한국시리즈', 'weight': 1528}
{'word': 'gksrnrwjdqn', 'realword': '한국정부', 'weight': 912}
{'word': 'gksrnrtjstn', 'realword': '한국선수', 'weight': 830}
{'word': 'gksrnrwjsfur', 'realword': '한국전력', 'weight': 812}
{'word': 'gksrnrwjswod', 'realword': '한국전쟁', 'weight': 644}
{'word': 'gksrnrshchd', 'realword': '한국노총', 'weight': 639}


'''




