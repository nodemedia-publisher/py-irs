import hgsysinc
from hgworddistance import GetWordDistance_Tanimoto
print('----------------------------------')
print('Distance_Tanimoto')
print('----------------------------------')
words = ['make', 'taken', 'takes', 'stake', 'makes', 'like']
for word in words:
    print (f'[{word}] Distance: %.2f' % GetWordDistance_Tanimoto('take', word))
# 위에 타미모토 거리값은 자카드 거리값과 차이가 없다.
# 글자수 가중치를 적용하는데 위에 단어는 모두 1글자라서 가중치 효과가 없다.



"""
처리 결과
#===================
----------------------------------
Distance_Tanimoto
----------------------------------
[make] Distance: 0.40
[taken] Distance: 0.20
[takes] Distance: 0.20
[stake] Distance: 0.20
[makes] Distance: 0.50
[like] Distance: 0.67


"""
