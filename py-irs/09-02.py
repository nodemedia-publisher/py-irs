import hgsysinc
from hgtext import 애국가
text = 애국가
# ㄱ)
find = '남산'
find_inx = text.find(find) 
print('# ㄱ) find:', find_inx)
if(find_inx >= 0):
    print(text[find_inx: (find_inx+11)])
# ㄴ)
find_inx = text.find('남대문')
print('# ㄴ) find:', find_inx)
if(find_inx >= 0):
    print(text[find_inx: (find_inx+11)])


'''
처리 결과:
================================
# ㄱ) find: 39
남산 위에 저 소나무
# ㄴ) find: -1
'''


