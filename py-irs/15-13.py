import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind import GetSpellCheck_NGram
from hgworddistance import MakeNGramVocabulary__DictFreq
#=from hgworddistance import AddNGramVocabulary__WordWeight, WeightNGramVocabulary
from hgkbd import HGTransString2EngString
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
#=print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
# make n-gram
#-----------------------------
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
#=NGramVocabulary = {}
#=for CurWord in Vocabulary:
#=    CurWord_Low = CurWord.lower() # 소문자 변환
#=    WordFreq = Vocabulary[CurWord]
#=    AddNGramVocabulary__WordWeight(NGramVocabulary, CurWord_Low, 
#=        RealWord=CurWord, Weight=WordFreq, NGram=ngram_k)
#=print('NGram Dict Num:', len(NGramVocabulary))
#=PrintNGramVocabulary(NGramVocabulary, PrintNum=0, PrintVocabularyList=False)
#=WeightNGramVocabulary(NGramVocabulary) # 가중치(빈도) 순으로 정렬(탐색시간 단축 위해)

#-----------------------------
#-----------------------------
FindWord = '챷새교' # (cictory) <- {victory}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자
SpellCheckWord = GetSpellCheck_NGram(FindWord_Eng, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)

#-----------------------------
#-----------------------------
FindWord = '햎두ㅡ둣' # (govenment) <- {government}의 철자 오류 입력
FindWord_Eng = HGTransString2EngString(FindWord) # 한글->영문자
SpellCheckWord = GetSpellCheck_NGram(FindWord_Eng, NGramVocabulary, ngram_k)
print(f"<{FindWord}> 이 단어가 맞나요? ===>", SpellCheckWord)



'''
출력 결과:
-----------------------------------
@@@ 철자 교정 테스트
-----------------------------------
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
[미국 대통령 취임 연설(InaugurationSpeech)] 사전을 N그램(N=5) 사전으로 변환하여 N그램 추천
-----------------------------------

<챷새교> 이 단어가 맞나요? ===> victory
<햎두ㅡ둣> 이 단어가 맞나요? ===> government




'''




