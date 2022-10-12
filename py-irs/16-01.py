import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind import MatchPrefix_SortDict_naive
#-----
#-----
#=print('reading texts')
# 미국 대통령 취임 연설(InaugurationSpeech)
Vocabulary = load_dictfreq_us_president(SortFlag=True) # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----------------------------
# Vocabulary: sorted by a->z
#-----------------------------
FindWord = 'abo'
MatchDict = MatchPrefix_SortDict_naive(FindWord, Vocabulary)

# 접두사 일치 단어 빈도 순 정렬
MatchDict_Sort = sorted(MatchDict.items(), key=lambda item: -item[1]) # by high

# 접두사 일치 목록 출력
print(f'prefix [{FindWord}]: {len(MatchDict_Sort)}')
print('(단어, 빈도)')
print(*MatchDict_Sort, sep='\n')


'''
출력 결과:
====================================================
이 예제는 사전에서 접두어와 일치하는 어휘를 (빈도가 포함된) 사전 형식으로 
반환받은 후에 빈도순으로 정렬하여 사전을 출력한다.

조건1: 
이 예제는 abc 순서에 맞게 정렬된 사전 목록을 사용한다.
처음부터 차례대로 비교하면서 정렬된 상태이므로 일치하는 단어가 발견된 이후에 
일치하는 어휘가 없으면 더 이상 검사하지 않아도 된다.

====================================================
Dict Num: 9110
prefix [abo]: 12
(단어, 빈도)
('about', 43)
('above', 21)
('aboriginal', 5)
('abolish', 2)
('abolished', 2)
('abounding', 2)
('abode', 1)
('abodes', 1)
('abolishing', 1)
('aborigines', 1)
('abound', 1)
('abounds', 1)

'''
