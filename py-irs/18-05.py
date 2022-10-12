import hgsysinc
from hgtest import load_dictfreq_us_president
from hgworddistance import MakeNGramVocabulary__DictFreq, MakeStringNGram
from hgdistance import GetEditDistance
#----------
#----------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president()
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
FindWord = 'fovern'
FindNGram = MakeStringNGram(FindWord, NGram=ngram_k, MoreThan=True)

#----------
#----------
# make n-gram suggest
NGramSuggestion_ByFreq = {} # 빈도용
NGramSuggestion_ByEditDis = {} # 편집 거리용 
for dic_f in FindNGram:
    NGramDicVocabulary = NGramVocabulary.get(dic_f)
    if(NGramDicVocabulary == None):
        continue
    for NGramDic in NGramDicVocabulary:#format:{'key': 'giver', 'word': 'giver', 'weight': 1}
        Keyword = NGramDic['key']
        if(not NGramSuggestion_ByFreq.get(Keyword)):
            NGramSuggestion_ByFreq[Keyword] = NGramDic['weight']
            # 편집 거리 계산
            EditDistance = GetEditDistance(FindWord, Keyword)
            NGramSuggestion_ByEditDis[Keyword] = EditDistance
print('# 생성 순서대로 출력')
print("('단어', 빈도)")
print(*NGramSuggestion_ByFreq.items(), sep='\n'), print()
print()

#-----------------------------
print('[가중치:빈도]  {n-gram suggest} sort by high')
Vocabulary_High = sorted(NGramSuggestion_ByFreq.items(), key=lambda item: -item[1]) # by high
print("('단어', 빈도)")
print(*Vocabulary_High, sep='\n'), print() # (빈도) 큰 값부터 출력

#-----------------------------
print('[가중치:편집 거리] {n-gram suggest} sort by low')
Vocabulary_Low = sorted(NGramSuggestion_ByEditDis.items(), key=lambda item: item[1]) # by low
print("('단어', 편집거리)")
print(*Vocabulary_Low, sep='\n'), print() # (편집 거리) 작은 값부터 출력



'''
출력 결과:
===================================
이 예제는 [미국 대통령 취임 연설(InaugurationSpeech)] 사전 목록을 사용한다.
===================================
Dict Num: 9110
NGram Dict Num: 63715
# 생성 순서대로 출력
('단어', 빈도)
('govern', 19)
('governed', 10)
('governing', 6)
('government', 607)
('governmental', 8)
('governments', 52)
('governs', 1)
('supergovernment', 1)


[가중치:빈도]  {n-gram suggest} sort by high
('단어', 빈도)
('government', 607)
('governments', 52)
('govern', 19)
('governed', 10)
('governmental', 8)
('governing', 6)
('governs', 1)
('supergovernment', 1)

[가중치:편집 거리] {n-gram suggest} sort by low
('단어', 편집거리)
('govern', 1)
('governs', 2)
('governed', 3)
('governing', 4)
('government', 5)
('governments', 6)
('governmental', 7)
('supergovernment', 10)


'''




