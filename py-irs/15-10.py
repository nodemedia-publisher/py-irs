import hgsysinc
from hgtest import load_dictfreq_kbs_2009
from hgtest import load_dictfreq_kbs_01_16
from hgfind import GetSpellCheck_NGram
from hgdistance import GetEditDistance

from hgworddistance import MakeNGramVocabulary__DictFreq, __Hng_2_Jamo__
from hgkbd import HGTransString2KBDJamo
from hgtest_ext_kbs import load_kbs_16_and_trans_ngram
#-----------------------
#-----------------------
run_type = 'run_type_make'
#=run_type = 'run_type_load'

if(run_type == 'run_type_make'):
    print()
    print('reading texts')
    #=Vocabulary = load_dictfreq_kbs_2009() # [KBS 9시 뉴스: 2009년]
    Vocabulary = load_dictfreq_kbs_01_16()  # [KBS 9시 뉴스: 16년치(2001~2016)]
    #=print('Dict Num:', len(Vocabulary))
    #=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
    #=print(Vocabulary)

    #-----------------------------
    # make n-gram
    #-----------------------------
    # __Hng_2_Jamo__: 검색어 사전을 두벌식 자모 n-gram 사전으로 변환
    ngram_k = 5
    NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, ngram_k, HngFmt=__Hng_2_Jamo__)
    #=print('NGram Dict Num:', len(NGramVocabulary))
else: # 'run_type_load': # hgfind_344_a11~a16.py 에서는 이 방식으로 썼음(결과가 위의 방식과 일치해야 한다.)
    #-----------------------
    # [KBS 9시 뉴스: 16년치(2001~2016)], N그램 사전 변환
    #-----------------------
    ngram_k = 5
    Vocabulary, NGramVocabulary = load_kbs_16_and_trans_ngram(NGram=ngram_k) # [KBS 9시 뉴스]

#-----------------------------
#-----------------------------
hnglist = ['란국', '롼율', '대헌민국', '대한밍국'] # 1글자 오류
hnglist.extend(['란국경제',]) # 1글자 오류
hnglist.extend(['란국경재', '란국경ㅈ', ]) # 2글자 오류
hnglist.extend(['란국경ㅂ', '란국경ㄷ', ]) # 3글자 오류
hnglist.extend(['란극경ㅈ', '란극경재']) # 3글자 오류
hnglist.extend(['란극경재정']) # 5글자 오류

#-----------------------------
#-----------------------------
print('# 편집 거리 제한 기본값(3) 적용 ')
for i, word in enumerate(hnglist):
    SpellCheckWord = GetSpellCheck_NGram(word, 
            NGramVocabulary, ngram_k, Hng2Jamo=True)
    if(len(SpellCheckWord) > 0): # 교정 단어 있는 경우
        FindWord_KBDjamo = HGTransString2KBDJamo(word)
        SpellWord_KBDjamo = HGTransString2KBDJamo(SpellCheckWord)
        EditDistance = GetEditDistance(FindWord_KBDjamo, SpellWord_KBDjamo)
        print(f'({i+1})EditDistance: {EditDistance} <{word}> ===> {SpellCheckWord}')
    else: # 교정 단어 없는 경우
        print(f'({i+1})EditDistance: (-1) <{word}> ===> {SpellCheckWord}')
print(),print(),print(),



'''
출력 결과:

-----------------------------------
@@@ 철자 교정 테스트
-----------------------------------
이 예제는 [KBS 9시 뉴스] 사전 목록을 사용한다.
[KBS 9시 뉴스] 사전을 N그램(N=5) 사전으로 변환하여 N그램 추천

====================================================
# 편집 거리 제한 기본값(3) 적용
(1)EditDistance: 1 <란국> ===> 한국
(2)EditDistance: 1 <롼율> ===> 환율
(3)EditDistance: 1 <대헌민국> ===> 대한민국
(4)EditDistance: 1 <대한밍국> ===> 대한민국
(5)EditDistance: 1 <란국경제> ===> 한국경제
(6)EditDistance: 2 <란국경재> ===> 한국경제
(7)EditDistance: 2 <란국경ㅈ> ===> 한국경제
(8)EditDistance: 3 <란국경ㅂ> ===> 한국형
(9)EditDistance: 3 <란국경ㄷ> ===> 한국형
(10)EditDistance: 3 <란극경ㅈ> ===> 한국경제
(11)EditDistance: 3 <란극경재> ===> 한국경제
(12)EditDistance: (-1) <란극경재정> ===> 



'''




