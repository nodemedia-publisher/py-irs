import hgsysinc
from hgworddistance import GetWordDistance_Jacard
print('----------------------------------')
print('Distance_Jacard')
print('----------------------------------')
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print (f'[{word}] Distance: %.2f' % GetWordDistance_Jacard('take', word))


"""
처리 결과
#===================
----------------------------------
Distance_Jacard
----------------------------------
[make] Distance: 0.40
[taken] Distance: 0.20
[takes] Distance: 0.20
[stake] Distance: 0.20
[makes] Distance: 0.50
[like] Distance: 0.67


"""

