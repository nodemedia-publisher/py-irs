import hgsysinc
from hgworddistance import GetEditDistance_NGram
print('----------------------------------')
print('[N-Gram] EditDistance')
print('----------------------------------')
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print (f'[{word}] EditDistance:', GetEditDistance_NGram('take', word, NGram=2))


'''
처리 결과:
=================================
----------------------------------
[N-Gram] EditDistance
----------------------------------
[make] EditDistance: 1
[taken] EditDistance: 1
[takes] EditDistance: 1
[stake] EditDistance: 1
[makes] EditDistance: 2
[like] EditDistance: 2

'''
