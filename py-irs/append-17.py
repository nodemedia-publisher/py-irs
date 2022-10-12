#-----------------------
# 어휘 빈도 사전과 검색어 철자 교정 
#-----------------------
import hgsysinc
from hgtest import load_dictfreq_gutenberg_wordlist
from hgworddistance import MakeNGramVocabulary__DictFreq
from hgkbd import HGTransString2EngString
from hgfind import GetSpellCheck_Find, GetSpellCheck_NGram
#-----------------------
# gutenberg porject
Vocabulary = load_dictfreq_gutenberg_wordlist(Stopword=True)
print('Dict Num:', len(Vocabulary))
print()

#-----------------------
# 철자 교정 알고리즘 (13장)
#-----------------------
FindWord = 'gpvernment' # <- {government}의 철자 오류 입력
SpellCheckWord = GetSpellCheck_Find(FindWord, Vocabulary)
if(FindWord != SpellCheckWord):
    print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)

#-----------------------
# 한/영 변환 및 철자 교정 알고리즘 (14장)
#-----------------------
FindWord = '햎ㄷ구ㅡ둣' # 'government' (한영변환 오류)
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자
SpellCheckWord = GetSpellCheck_Find(FindWord_Eng, Vocabulary)
if(FindWord != SpellCheckWord):
    print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)

#=Han2EngChecker('랲ㄷ구ㅡ둣', Vocabulary, SpellWordMode =True) # 'fovernment' <- 'government' (한영변환 오류 + 철자 오류)
FindWord = '랲ㄷ구ㅡ둣' # 'fovernment' <- 'government' (한영변환 오류 + 철자 오류)
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자
SpellCheckWord = GetSpellCheck_Find(FindWord_Eng, Vocabulary)
if(FindWord != SpellCheckWord):
    print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)


#-----------------------
# n-gram 기반 한/영 변환 및 철자 교정 알고리즘 (15장)
#-----------------------
# make n-gram
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)

#=FindWord = 'aithorize' # <- {authorize}의 철자 오류 입력
FindWord = 'lixurious' # <- {luxurious}의 철자 오류 입력
SpellCheckWord = GetSpellCheck_NGram(FindWord, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)

FindWord = '랲두ㅡ둣' # (fovenment) <- {government}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자
SpellCheckWord = GetSpellCheck_NGram(FindWord_Eng, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)


'''
출력 결과:
-----------------------------------
@@@ 철자 교정 테스트
-----------------------------------
이 예제는 [gutenberg] 사전 목록을 사용한다.
===============================================================
dictionary reading: ./../ext-src/data/gutenberg/gutenberg_wordfreq.tpx

Dict Num: 53704

<gpvernment> 이 단어가 맞나요? ===> government
<햎ㄷ구ㅡ둣> 이 단어가 맞나요? ===> government
<랲ㄷ구ㅡ둣> 이 단어가 맞나요? ===> government
<lixurious> 이 단어가 맞나요? ===> luxurious
<랲두ㅡ둣> 이 단어가 맞나요? ===> government


'''

