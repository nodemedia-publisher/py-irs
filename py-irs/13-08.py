import hgsysinc
from hgworddistance import TestEditDistance_Jamo3
#-----
TestEditDistance_Jamo3('대한민국', '대한밍국') # '민' 음절에서 자모 1 수정
TestEditDistance_Jamo3('대한민국', '대한미국') # '민' 음절에서 자모 1 수정
TestEditDistance_Jamo3('대한민국', '대한지국') # '민' 음절에서 자모 2 수정
TestEditDistance_Jamo3('대한민국', '대한제국') # '민' 음절에서 자모 3 수정

'''
처리 결과:
===============================
EditDistance: 1
EditDistance: 1
EditDistance: 2
EditDistance: 3
'''
