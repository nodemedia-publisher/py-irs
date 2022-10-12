import hgsysinc
from hgtest import load_dictfreq_us_president
#=from hgworddistance import MakeNGramVocabulary__DictFreq
from hgworddistance import AddNGramVocabulary__WordWeight
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
# make n-gram
#-----------------------------
#=ngram_k = 5
ngram_k = 7
#=NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
NGramVocabulary = {}
for i, CurWord in enumerate(Vocabulary):
    CurWord_Low = CurWord.lower() # 소문자 변환
    WordFreq = Vocabulary[CurWord]
    AddNGramVocabulary__WordWeight(NGramVocabulary, CurWord_Low, 
        Weight=WordFreq, NGram=ngram_k)
print('NGram Dict Num:', len(NGramVocabulary))


'''
출력 결과:
====================================
Dict Num: 9110
NGram Dict Num: 35855

'''




