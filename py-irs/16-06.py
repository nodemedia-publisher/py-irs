import hgsysinc
from hgtest import load_dictfreq_us_president
from hgtrie_inter import HGTrie_naive_d
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # [미국 대통령 취임사]
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
#-----------------------------
# 트라이 생성: 어휘 사전을 트라이로 변환
TrieTest = HGTrie_naive_d() 
#=TrieTest.MakeTrie__DictFreq(Vocabulary) 
# 편집을 위해서 MakeTrie__DictFreq(Vocabulary) 함수를 풀어서 코딩한 것
for Word in Vocabulary: 
    WordFreq = Vocabulary[Word]
    TrieTest.InsertWord(Word, Weight=WordFreq)
#=TrieTest.PrintTrie()
#=============
# 트라이 탐색
PrefixList = TrieTest.GetPrefixList('abo')
#=PrefixList = TrieTest.GetPrefixList('govern')
print(), print(f'PrefixList {len(PrefixList)}:')
print(*PrefixList, sep='\n')
#=print(), print(f'PrefixList {len(PrefixList)}:', *PrefixList)



'''
출력 결과:
=====================================
이 예제는 [미국 대통령 취임사] 정렬된 사전 목록을 사용한다.
=====================================
Dict Num: 9110

PrefixList 12:
('abode', 1)
('abodes', 1)
('abolish', 2)
('abolished', 2)
('abolishing', 1)
('aboriginal', 5)
('aborigines', 1)
('abound', 1)
('abounding', 2)
('abounds', 1)
('about', 43)
('above', 21)


'''

