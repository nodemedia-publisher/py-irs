import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind import GetSuggestion_NGram
from hgworddistance import MakeNGramVocabulary__DictFreq
from hgkbd import HGTransString2EngString
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# make n-gram: 검색어 사전을 n-gram으로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
#=print('NGram Dict Num:', len(NGramVocabulary))
#-----------------------------
#-----------------------------
# 검색어를 영문자로 변환
FindWord = '챷색' # (cictor) <- {victory}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자

# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord_Eng, 
    NGramVocabulary, NGram=ngram_k, SuggestNum=SuggestNum)

# 추천 목록 출력
print(f'<{FindWord}(<=={FindWord_Eng})> NGram Suggest {len(SugList_NGram)}:')
if(len(SugList_NGram) > 0):
    print(*SugList_NGram, sep='\n')


'''
출력 결과:
====================================
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
[미국 대통령 취임 연설(InaugurationSpeech)] 사전을 N그램(N=5) 사전으로 변환한다.
====================================
영문 오류 입력로 인하여 'victory'을 '챷색(cictor)'로 검색 상황을 시뮬레이션에 필요해서
1. 검색어 사전을 N그램 사전으로 확장
2. 검색어 '챷색'을 영문자로 변경 -> 'cictor'
3. 'cictor'의 N그램으로 N그램 사전을 탐색하여 목록 출력
-----------------------------------
<챷색(<==cictor)> NGram Suggest 3:
{'word': 'ictor', 'realword': 'victory', 'weight': 11}
{'word': 'ictor', 'realword': 'victories', 'weight': 4}
{'word': 'ictor', 'realword': 'victorious', 'weight': 1}

'''




