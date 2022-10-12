#-----------------------
# 어휘 빈도 사전과 검색어 자동 추천
#-----------------------
import hgsysinc
from hgtest import load_dictfreq_gutenberg_wordlist
from hgworddistance import MakeNGramVocabulary__DictFreq
from hgkbd import HGTransString2EngString
from hgfind import HGTrie, GetSuggestion_NGram, PrintSuggestionList
#-----------------------
# gutenberg porject
Vocabulary = load_dictfreq_gutenberg_wordlist(Stopword=True)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
print()

#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie() 
for CurWord in Vocabulary:
    WordFreq = Vocabulary[CurWord]
    CurWord = CurWord.lower() # 소문자 변환
    TrieTest.InsertNode(CurWord, Weight=WordFreq)

#-----------------------
# 검색어 자동 추천 알고리즘 (16장)
#-----------------------
# 트라이 추천(Suggestion)
FindWord = 'autho'
SugList = TrieTest.GetSuggestion(FindWord)
print(f'<{FindWord}> Suggest {len(SugList)}:')
#=print(*SugList, sep='\n')
PrintSuggestionList(SugList)
print()

#-----------------------
# 한/영 변환 자동 추천 알고리즘 (17장)
#-----------------------
# 트라이 추천(Suggestion)
FindWord = '며쇄' # 'autho' 한영변환 오류 입력
FindWord_EngString = HGTransString2EngString(FindWord) # 한->영 입력 변환
SugList = TrieTest.GetSuggestion(FindWord_EngString)
print(f'<{FindWord}(<=={FindWord_EngString})> Suggest {len(SugList)}:')
#=print(*SugList, sep='\n')
PrintSuggestionList(SugList)
print()
    
#-----------------------
# n-gram 기반 철자 교정 자동 추천 알고리즘 (18장)
#-----------------------
# make n-gram
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
print('NGram Dict Num:', len(NGramVocabulary))

#-----------------------------
FindWord = 'vircum' # (vircum) <- {circum}의 철자 오류 입력
# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord, 
    NGramVocabulary, NGram=ngram_k, SuggestNum=SuggestNum)

# 추천 목록 출력
print(f'<{FindWord})> NGram Suggest {len(SugList_NGram)}:')
#=print(*SugList_NGram, sep='\n')
PrintSuggestionList(SugList_NGram)
print()

#-----------------------------
# 검색어를 영문자로 변환
FindWord = '퍅쳐ㅡ' # (vircum) <- {circum}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자

# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord_Eng, 
    NGramVocabulary, NGram=ngram_k, SuggestNum=SuggestNum)

# 추천 목록 출력
print(f'<{FindWord}(<=={FindWord_Eng})> NGram Suggest {len(SugList_NGram)}:')
#=print(*SugList_NGram, sep='\n')
PrintSuggestionList(SugList_NGram)
#=print()


'''
출력 결과:
-----------------------------------
@@@ 검색어 추천 테스트
-----------------------------------
이 예제는 [gutenberg] 사전 목록을 사용한다.
===============================================================
dictionary reading: ./../ext-src/data/gutenberg/gutenberg_wordfreq.tpx

Dict Num: 53704

<autho> Suggest 10:
1 : authority (363)
2 : author (290)
3 : authoress (43)
4 : authoritative (15)
5 : authorized (14)
6 : authorship (10)
7 : authorize (9)
8 : authorised (7)
9 : authoritatively (6)
10 : authorization (2)

<며쇄(<==autho)> Suggest 10:
1 : authority (363)
2 : author (290)
3 : authoress (43)
4 : authoritative (15)
5 : authorized (14)
6 : authorship (10)
7 : authorize (9)
8 : authorised (7)
9 : authoritatively (6)
10 : authorization (2)

NGram Dict Num: 326477
<vircum)> NGram Suggest 10:
1 : circumstance (732)
2 : circumference (29)
3 : circumstantial (25)
4 : circumspection (12)
5 : circumspectly (10)
6 : circumstantially (8)
7 : circumspect (7)
8 : circumscribed (7)
9 : circumlocution (7)
10 : circumnavigation (6)

<퍅쳐ㅡ(<==vircum)> NGram Suggest 10:
1 : circumstance (732)
2 : circumference (29)
3 : circumstantial (25)
4 : circumspection (12)
5 : circumspectly (10)
6 : circumstantially (8)
7 : circumspect (7)
8 : circumscribed (7)
9 : circumlocution (7)
10 : circumnavigation (6)

'''

