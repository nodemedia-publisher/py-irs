import hgsysinc
from hgtest import load_dictfreq_us_president
#=from hgworddistance import MakeNGramVocabulary__DictFreq
from hgworddistance import (
    PrintNGramVocabulary_New, 
    MakeStringNGram, AddNGramVocabulary__WordWeight,
)
from hgworddistance import PrintVocabulary
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
#=ngram_k = 5
ngram_k = 7
#=NGramVocabulary = MakeNGramVocabulary__DictFreq(Vocabulary, NGram=ngram_k)
NGramVocabulary = {}
for i, CurWord in enumerate(Vocabulary):
    CurWord_Low = CurWord.lower() # 소문자 변환
    WordFreq = Vocabulary[CurWord]
    AddNGramVocabulary__WordWeight(NGramVocabulary, CurWord_Low, 
        Weight=WordFreq, NGram=ngram_k)
#=print('NGram Dict Num:', len(NGramVocabulary))

#-----------------------------
#-----------------------------
FindWord = 'gpvernment'
FindNGram = MakeStringNGram(FindWord, NGram=ngram_k, MoreThan=True)
print(), print(f'{ngram_k}-Gram ({len(FindNGram)}): {FindNGram}')
#=for NGramDicNum, dic_f in enumerate(FindNGram):
#=    print(f'{NGramDicNum+1}\t{dic_f}')

print()
print('#-----------------------------')
# make n-gram suggest
NGramSuggestionDictFreq = {}
for NGramDicNum, dic_f in enumerate(FindNGram):
    NGramDicVocabulary = NGramVocabulary.get(dic_f)
    if(NGramDicVocabulary == None):
        continue

    print(f'{NGramDicNum+1}, {dic_f} ({len(NGramDicVocabulary)}) :')
    #=print(NGramDicVocabulary)
    PrintNGramVocabulary_New(NGramDicVocabulary, PrintNum=0, LeadingString='\t')
    print()

    for NGramDic in NGramDicVocabulary:
        #= format: {'key': 'giver', 'word': 'giver', 'weight': 1}
        #=print(NGramDic) #= format: {'key': 'giver', 'word': 'giver', 'weight': 1}
        if(NGramSuggestionDictFreq.get(NGramDic['key']) is None):
            #=NGramSuggestionDictFreq[NGramDic['key']] = NGramDicVocabulary[NGramDic]
            NGramSuggestionDictFreq[NGramDic['key']] = NGramDic['weight']
#=print(NGramSuggestionDictFreq)
print(), print ('교정 후보 목록')
PrintVocabulary(NGramSuggestionDictFreq)



'''
출력 결과:
=======================================
7-Gram (10): ['gpvernm', 'gpvernme', 'gpvernmen', 'gpvernment', 'pvernme', 'pvernmen', 'pvernment', 'vernmen', 'vernment', 'ernment']

#-----------------------------
8, vernmen (4) :
        1, government: 607
        2, governmental: 8
        3, governments: 52
        4, supergovernment: 1

9, vernment (4) :
        1, government: 607
        2, governmental: 8
        3, governments: 52
        4, supergovernment: 1

10, ernment (6) :
        1, concernment: 2
        2, discernment: 1
        3, government: 607
        4, governmental: 8
        5, governments: 52
        6, supergovernment: 1


교정 후보 목록
0, concernment: 2
1, discernment: 1
2, government: 607
3, governmental: 8
4, governments: 52
5, supergovernment: 1


'''




