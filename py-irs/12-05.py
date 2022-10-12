import hgsysinc
from hgdistance import GetEditDistance
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print (f'[{word}] EditDistance: %.2f' % GetEditDistance('take', word, Norm=True))
print()
print ('EditDistance: %.2f' % GetEditDistance('govenment', 'government', Norm=True)) # Distance: 0.10
print ('EditDistance: %.2f' % GetEditDistance('difterential', 'differential', Norm=True)) # Distance: 0.083


"""
처리 결과
==========================================
[make] EditDistance: 0.25
[taken] EditDistance: 0.20
[takes] EditDistance: 0.20
[stake] EditDistance: 0.20
[makes] EditDistance: 0.40
[like] EditDistance: 0.50

EditDistance: 0.10
EditDistance: 0.08

"""
