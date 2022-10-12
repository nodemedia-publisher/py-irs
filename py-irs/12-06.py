import hgsysinc
from hgworddistance import MakeStringNGram
print('----------------------------------')
print('N-Gram')
print('----------------------------------')
print(MakeStringNGram('government', NGram=1))
print(MakeStringNGram('government', NGram=2))
print(MakeStringNGram('government', NGram=3))
print(MakeStringNGram('government', NGram=4))

print(MakeStringNGram('대한교과서주식회사', NGram=1))
print(MakeStringNGram('대한교과서주식회사', NGram=2))
print(MakeStringNGram('대한교과서주식회사', NGram=3))
print(MakeStringNGram('대한교과서주식회사', NGram=4))


'''
----------------------------------
N-Gram
----------------------------------
['g', 'o', 'v', 'e', 'r', 'n', 'm', 'e', 'n', 't']
['go', 'ov', 've', 'er', 'rn', 'nm', 'me', 'en', 'nt']
['gov', 'ove', 'ver', 'ern', 'rnm', 'nme', 'men', 'ent']
['gove', 'over', 'vern', 'ernm', 'rnme', 'nmen', 'ment']
['대', '한', '교', '과', '서', '주', '식', '회', '사']
['대한', '한교', '교과', '과서', '서주', '주식', '식회', '회사']
['대한교', '한교과', '교과서', '과서주', '서주식', '주식회', '식회사']
['대한교과', '한교과서', '교과서주', '과서주식', '서주식회', '주식회사']

'''
