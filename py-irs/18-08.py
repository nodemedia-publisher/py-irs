import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import GetSuggestion_NGram, __Hng_2_Jamo__
from hgworddistance import MakeNGramVocabulary__DictFreq
from hgkbd import HGGetJaumMoum__EngString, HGGetSyllable__EngString
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
# make n-gram: 검색어 사전을 두벌식 자모에 의한 n-gram으로 변환
# __Hng_2_Jamo__: 한글 검색어 사전을 두벌식 n-gram 사전으로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, 
                                    NGram=ngram_k, HngFmt=__Hng_2_Jamo__)
#=print('NGram Dict Num:', len(NGramVocabulary))
#-----------------------------
#-----------------------------
# 검색어 변환: 영문자 -> 한글
FindWord = 'fksrnrqkdthd' # (란국방송) <- {한국방송}의 철자 오류 입력
FindWord_KBDJamo = HGGetJaumMoum__EngString(FindWord)#영문자->한글 두벌식 자모

# n-gram에서 검색어 추천
SuggestNum = 10 # N그램에서 10개만 추천
SugList_NGram = GetSuggestion_NGram(FindWord_KBDJamo, NGramVocabulary, 
            NGram=ngram_k, SuggestNum=SuggestNum, HngFmt=__Hng_2_Jamo__)

# 추천 목록 출력
FindWord_Hangul = HGGetSyllable__EngString(FindWord) # 영문자->한글
print(f'<{FindWord}(<=={FindWord_KBDJamo}, {FindWord_Hangul})> NGram Suggest {len(SugList_NGram)}:')
if(len(SugList_NGram) > 0):
    print(*SugList_NGram, sep='\n')




'''
출력 결과:

-----------------------------------
====================================
[KBS 9시 뉴스(16년치)] 사전에서 한글을 두벌식 자모로 변환한 후에 N그램(N=5) 사전으로 변환한다.
====================================

한글 오류 입력로 인하여 '한국경제'를 'fksrnrrudwp'('란국경제')로 검색 상황을 시뮬레이션에 필요해서
1. 검색어 사전을 두벌식 자모로 변환한 후에 N그램 사전으로 확장
2. 검색어 'fksrnrrudwp'(란국경제)를 두벌식 자모로 변경 -> 'ㄹㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ'
3. 'ㄹㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ'의 N그램으로 N그램 사전을 탐색하여 목록 출력
-----------------------------------
<fksrnrqkdthd(<==ㄹㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ, 란국방송)> NGram Suggest 10:
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송협회', 'weight': 67}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송대상', 'weight': 25}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송기자클럽', 'weight': 22}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송광고공사', 'weight': 19}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송협회장', 'weight': 13}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송학회', 'weight': 12}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송공사', 'weight': 11}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송영상산업진흥원', 'weight': 8}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송통신대학교', 'weight': 7}
{'word': 'ㅏㄴㄱㅜㄱㅂㅏㅇㅅㅗㅇ', 'realword': '한국방송카메라기자협회', 'weight': 7}

'''




