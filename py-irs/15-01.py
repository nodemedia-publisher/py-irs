import hgsysinc
from hgtest import load_dictfreq_us_president
from hgfind_test import Find_1_Subword
#-----------------------
#-----------------------
#=print('reading texts')
Vocabulary = load_dictfreq_us_president() # 미국 대통령 취임 연설(InaugurationSpeech)
print('Dict Num:', len(Vocabulary))
#=print('Word Num:', sum([Vocabulary[dic] for dic in Vocabulary]))
#=print(Vocabulary)

#
Find_1_Subword('fovernment', Vocabulary)

#-----
#-----
#=Find_1_Subword('hovernment')
#=print(),print(),print(),
#=
#=Find_1_Subword('qovernment')
#=print(),print(),print(),
#=
#=Find_1_Subword('zovernment')
#=print(),print(),print(),


'''
출력 결과:
-----------------------------------
Dict Num: 9110
input: fovernment
sub input: overnment
순서: 단어(빈도)
1: government(607)
2: governmental(8)
3: governments(52)
4: supergovernment(1)

'''




