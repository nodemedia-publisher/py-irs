import hgsysinc
from hgtest import load_dictfreq_us_president
from hgworddistance import (
    MakeNGramVocabulary__DictFreq, PrintNGramVocabulary_New, MakeStringNGram,
)
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# make n-gram dict: 어휘 사전을 n-gram로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
print('NGram Dict Num:', len(NGramVocabulary))

#----------
#----------
# 검색어 n-gram 변환
FindWord = 'governnen'
FindNGram = MakeStringNGram(FindWord, NGram=ngram_k, MoreThan=True)
print(f'[{FindWord}] {ngram_k}-Gram ({len(FindNGram)}): {FindNGram}')

#----------
#----------
# 검색어 n-gram으로 n-gram 사전 탐색
for NGram_i, dic_f in enumerate(FindNGram):
    NGramDicVocabulary = NGramVocabulary.get(dic_f)
    if(NGramDicVocabulary):
        print(f'{NGram_i + 1}, {dic_f} ({len(NGramDicVocabulary)}) :')
        PrintNGramVocabulary_New(NGramDicVocabulary, LeadingString='\t')
        print()


'''
출력 결과:
===================================
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
===================================
Dict Num: 9110
NGram Dict Num: 63715
[governnen] 5-Gram (15): ['gover', 'govern', 'governn', 'governne', 'governnen', 'overn', 'overnn', 'overnne', 'overnnen', 'vernn', 'vernne', 'vernnen', 'ernne', 'ernnen', 'rnnen']
1, gover (8) :
        1, govern: 19
        2, governed: 10
        3, governing: 6
        4, government: 607
        5, governmental: 8
        6, governments: 52
        7, governs: 1
        8, supergovernment: 1

2, govern (8) :
        1, govern: 19
        2, governed: 10
        3, governing: 6
        4, government: 607
        5, governmental: 8
        6, governments: 52
        7, governs: 1
        8, supergovernment: 1

6, overn (8) :
        1, govern: 19
        2, governed: 10
        3, governing: 6
        4, government: 607
        5, governmental: 8
        6, governments: 52
        7, governs: 1
        8, supergovernment: 1

'''




