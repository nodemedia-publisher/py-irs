import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind import GetSuggestion_NGram, __Hng_2_Jamo__
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
FindWord = '랲ㄷ구ㅡ' # (fovernm) <- {government}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자

# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord_Eng, 
    NGramVocabulary, NGram=ngram_k, SuggestNum=SuggestNum)

# 추천 목록 출력
print(f'<{FindWord}(<=={FindWord_Eng})> NGram Suggest {len(SugList_NGram)}:')
if(len(SugList_NGram) > 0):
    print(*SugList_NGram, sep='\n')
    print(),


'''
출력 결과:
====================================
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
[미국 대통령 취임 연설(InaugurationSpeech)] 사전을 N그램(N=5) 사전으로 변환한다.
====================================
<랲ㄷ구ㅡ(<==fovernm)> NGram Suggest 8:
{'word': 'overnm', 'realword': 'government', 'weight': 607}
{'word': 'overnm', 'realword': 'governments', 'weight': 52}
{'word': 'overn', 'realword': 'govern', 'weight': 19}
{'word': 'overn', 'realword': 'governed', 'weight': 10}
{'word': 'overnm', 'realword': 'governmental', 'weight': 8}
{'word': 'overn', 'realword': 'governing', 'weight': 6}
{'word': 'overn', 'realword': 'governs', 'weight': 1}
{'word': 'overnm', 'realword': 'supergovernment', 'weight': 1}



'''




