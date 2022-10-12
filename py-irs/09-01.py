import hgsysinc
from hgtext import 애국가
text = 애국가
textlen = len(text)

#=find = '남'
#=find = '남산이'
find = '남산'
findlen = len(find)

for tx_i in range(textlen):
    if(text[tx_i] == find[0]): # '남'
        match = True
        for fn_j in range(findlen):
            #=print(find[fn_j], text[tx_i + fn_j])
            if(find[fn_j] != text[tx_i + fn_j]):
                match = False
                break
        if(match == True):
            #=print('find:', tx_i, text[tx_i: tx_i + findlen])
            print('find:', tx_i)


'''
처리 결과:
=======================
find: 39
'''

