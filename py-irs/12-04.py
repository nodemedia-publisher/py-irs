import hgsysinc
from hgdistance import GetEditDistance
print('----------------------------------')
print('EditDistance')
print('----------------------------------')
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print (f'[{word}] EditDistance:', GetEditDistance('take', word))

"""
처리 결과
==========================================
----------------------------------
EditDistance
----------------------------------
[make] EditDistance: 1
[taken] EditDistance: 1
[takes] EditDistance: 1
[stake] EditDistance: 1
[makes] EditDistance: 2
[like] EditDistance: 2

"""

