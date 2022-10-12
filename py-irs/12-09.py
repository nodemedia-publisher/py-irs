import hgsysinc
from hgworddistance import GetWordDistance_Cosine
print('----------------------------------')
print('Distance_Cosine')
print('----------------------------------')
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print(f'[{word}] Distance: %.2f' % GetWordDistance_Cosine('take', word))
print()
print('Distance: %.2f' %GetWordDistance_Cosine('govenment','government'))#Distance: 0.04
print('Distance: %.2f' %GetWordDistance_Cosine('difterential','differential'))#Distance: 0.06

"""
처리 결과
#===================
[make] Distance: 0.25
[taken] Distance: 0.11
[takes] Distance: 0.11
[stake] Distance: 0.11
[makes] Distance: 0.33
[like] Distance: 0.50

Distance: 0.04
Distance: 0.06

"""
