import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind_test import Check_1_Subword
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)
#-----
#-----
Check_1_Subword('fovernment', Vocabulary)

#=print(),print(),print(),
#=Check_1_Subword('hovernment', Vocabulary)
#=Check_1_Subword('qovernment', Vocabulary)
#=Check_1_Subword('zovernment', Vocabulary)


'''
출력 결과:
===================================
Dict Num: 9110
input: fovernment
sub input: overnment
순서: 단어      [편집거리, 빈도]
1: government   [1, 607]
2: governments  [2, 52]
3: governmental [3, 8]
4: supergovernment      [6, 1]

'''




