import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import GetSuggestion_NGram
from hgworddistance import (
    MakeNGramVocabulary__DictFreq, WeightNGramVocabulary,
    __Hng_2_Jamo__,
)
from hgkbd import HGTransString2KBDJamo
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# make n-gram: 검색어 사전을 두벌식 자모에 의한 n-gram으로 변환
# __Hng_2_Jamo__: 한글 검색어 사전을 두벌식 n-gram 사전으로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, 
                                NGram=ngram_k, HngFmt=__Hng_2_Jamo__)
print('NGram Dict Num:', len(NGramVocabulary))

#-----------------------------
#-----------------------------
# 검색어 두벌식 자모 변환
FindWord = '란국경ㅈ' # '한국경ㅈ'의 철자 오류 입력
FindWord_KBDjamo = HGTransString2KBDJamo(FindWord) # 한글->두벌식 자모

# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord_KBDjamo, NGramVocabulary, 
            NGram=ngram_k, SuggestNum=SuggestNum, HngFmt=__Hng_2_Jamo__)

# 추천 목록 출력
print(f'<{FindWord}(<==={FindWord_KBDjamo})>', 
    f'NGram Suggest {len(SugList_NGram)}:')
if(len(SugList_NGram) > 0):
    print(*SugList_NGram, sep='\n')


'''
출력 결과:
======================================
이 예제는 [KBS 9시 뉴스(16년치)] 사전 목록을 사용한다.
[KBS 9시 뉴스(16년치)] 사전을 N그램(N=5) 사전으로 변환하여 N그램 추천

한글 오류 입력로 인하여 '한국경제'을 '란국경ㅈ'로 검색 상황
N그램으로 비슷한 단어 찾기
======================================
Dict Num: 413165
NGram Dict Num: 4353077
<란국경ㅈ(<===ㄹㅏㄴㄱㅜㄱㄱㅕㅇㅈ)> NGram Suggest 10:
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '한국경제', 'weight': 614}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '한국경제연구원', 'weight': 288}
{'word': 'ㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '전국경제인연합회', 'weight': 132}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇ', 'realword': '한국경영자총협회', 'weight': 90}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇ', 'realword': '한국경찰', 'weight': 48}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇ', 'realword': '한국경기', 'weight': 28}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '한국경제보고서', 'weight': 5}
{'word': 'ㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '전국경제인연합', 'weight': 5}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '한국경제연구원장', 'weight': 4}
{'word': 'ㅏㄴㄱㅜㄱㄱㅕㅇㅈ', 'realword': '한국경제연구소', 'weight': 3}

'''




