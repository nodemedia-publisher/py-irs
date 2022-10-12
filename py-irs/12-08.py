import hgsysinc
from hgdistance import GetEditDistance
from hgworddistance import GetEditDistance_NGram
#=print('----------------------------------')
#=print('[N-Gram] EditDistance')
#=print('----------------------------------')
#@@@ 아래 2블록은 [N-Gram] 차이를 비교하기 위한 것

#=print('----------------------------------')
#=print('EditDistance')
#=print('----------------------------------')
print('[N-Gram(X)]')
words = ['govenment', 'overnment', 'govetnment', 'fovernment', 'governmenr',]
for word in words:
    print (f'[{word}] EditDistance:', GetEditDistance( word, 'government'))
print()
#=print('----------------------------------')
#=print('[N-Gram] EditDistance')
#=print('----------------------------------')
print('[N-Gram(O)]')
#=words = ['govenment', 'overnment', 'govetnment', 'fovernment', 'governmenr',]
for word in words:
    print (f'[{word}] EditDistance:',GetEditDistance_NGram(word,'government', NGram=2))


'''
처리 결과:
=================================
EditDistance
[govenment] EditDistance: 1
[overnment] EditDistance: 1
[govetnment] EditDistance: 1
[fovernment] EditDistance: 1
[governmenr] EditDistance: 1

[N-Gram] EditDistance
[govenment] EditDistance: 2
[overnment] EditDistance: 1
[govetnment] EditDistance: 2
[fovernment] EditDistance: 1
[governmenr] EditDistance: 1
 
'''
