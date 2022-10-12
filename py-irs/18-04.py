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
#----------
#----------
# make n-gram dict: 어휘 사전을 n-gram로 변환
ngram_k = 5
NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
print('NGram Dict Num:', len(NGramVocabulary))

#----------
#----------
# 검색어 n-gram 변환
FindWord = 'givernm'
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
print()

#----------
#----------
from hgfind import PrintVocabulary
print('# make n-gram suggest')
NGramSuggestionDictFreq = {}
for dic_f in FindNGram:
    NGramDicVocabulary = NGramVocabulary.get(dic_f)
    if(NGramDicVocabulary is None):
        continue
    for NGramDic in NGramDicVocabulary: # format: {'key':'giver','word':'giver','weight': 1}
        Keyword = NGramDic['key']
        if(NGramSuggestionDictFreq.get(Keyword) is None):
            NGramSuggestionDictFreq[Keyword] = NGramDic['weight']
PrintVocabulary(NGramSuggestionDictFreq)
print()

#----------
#----------
print('# {n-gram suggest} sort by high')
Vocabulary_High = sorted(NGramSuggestionDictFreq.items(), 
                         key=lambda item: -item[1]) # by high
print(*Vocabulary_High, sep='\n')




'''
출력 결과:
===================================
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
===================================
Dict Num: 9110
NGram Dict Num: 63715
[givernm] 5-Gram (6): ['giver', 'givern', 'givernm', 'ivern', 'ivernm', 'vernm']
1, giver (3) :
        1, giver: 1
        2, lawgiver: 1
        3, lawgivers: 1

6, vernm (4) :
        1, government: 607
        2, governmental: 8
        3, governments: 52
        4, supergovernment: 1


# make n-gram suggest
0, giver: 1
1, government: 607
2, governmental: 8
3, governments: 52
4, lawgiver: 1
5, lawgivers: 1
6, supergovernment: 1

# {n-gram suggest} sort by high
('government', 607)
('governments', 52)
('governmental', 8)
('giver', 1)
('lawgiver', 1)
('lawgivers', 1)
('supergovernment', 1)


'''




