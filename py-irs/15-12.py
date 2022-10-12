import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import GetSpellCheck_NGram
from hgworddistance import MakeNGramVocabulary__DictFreq, __Hng_2_Jamo__
from hgkbd import HGGetJaumMoum__EngString
#=from hgworddistance import AddNGramVocabulary__WordWeight, WeightNGramVocabulary
#=from hgkbd import HGTransString2KBDJamo
#-----------------------
#-----------------------
#=print('reading texts')
#=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
# make n-gram
#-----------------------------
# __Hng_2_Jamo__: 한글 검색어 사전을 두벌식 n-gram 사전으로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, 
                            NGram=ngram_k, HngFmt=__Hng_2_Jamo__)
#=NGramVocabulary = {}
#=for CurWord in Vocabulary:
#=    CurWord_Low = CurWord.lower() # 소문자 변환
#=    KBDCharString = HGTransString2KBDJamo(CurWord_Low) # 한글->키보드 자모
#=    WordFreq = Vocabulary[CurWord]
#=    AddNGramVocabulary__WordWeight(NGramVocabulary, KBDCharString, 
#=        RealWord=CurWord, Weight=WordFreq, NGram=ngram_k)
#=print('NGram Dict Num:', len(NGramVocabulary))
#=PrintNGramVocabulary(NGramVocabulary, PrintNum=0, PrintVocabularyList=False)
#=WeightNGramVocabulary(NGramVocabulary) # 가중치(빈도) 순으로 정렬(탐색시간 단축 위해)

#-----------------------------
#-----------------------------
FindWord = 'eogjsalsrnr' # (대헌민국) <- {대한민국}의 철자 오류 입력
FindWord_Jamo = HGGetJaumMoum__EngString(FindWord) # 영문자->한글 자모
SpellCheckWord = GetSpellCheck_NGram(FindWord_Jamo, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)

#-----------------------------
#-----------------------------
FindWord = 'fksrnrqkdthd' # (란국방송) <- {한국방송}의 철자 오류 입력
FindWord_Jamo = HGGetJaumMoum__EngString(FindWord) # 영문자->한글 자모
SpellCheckWord = GetSpellCheck_NGram(FindWord_Jamo, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)


'''
출력 결과:
-----------------------------------
@@@ 철자 교정 테스트
-----------------------------------
이 예제는 [KBS 9시 뉴스] 사전 목록을 사용한다.
[KBS 9시 뉴스] 사전을 N그램(N=5) 사전으로 변환하여 N그램 추천
=============================================
<eogjsalsrnr> 이 단어가 맞나요? ===> 대한민국
<fksrnrqkdthd> 이 단어가 맞나요? ===> 한국방송


'''




