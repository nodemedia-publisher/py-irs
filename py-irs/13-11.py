import hgsysinc
from hgworddistance import TestEditDistance_Jamo2
#-----
#-----
TestEditDistance_Jamo2('마국경제', '미국경제')
TestEditDistance_Jamo2('대한밍국', '대한민국')
TestEditDistance_Jamo2('죈장','된장')
TestEditDistance_Jamo2('솽장','광장')


'''
처리 결과:
=====================
EditDistance: 1
EditDistance: 1
EditDistance: 1
EditDistance: 1
'''
