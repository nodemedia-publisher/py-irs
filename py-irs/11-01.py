import hgsysinc
from hgchartype import HGGetToken
from hgchartype import GetStringListByScriptList
from hgchartype import HGGetKeywordList
#----------------------
#----------------------
str1 = "원주율(π, paɪ, 圓周率)은 수학 상수로 3.1415926535...이다."
#=GetStringListByScriptList(HGGetToken(str1))
print('ㄱ)', GetStringListByScriptList(HGGetToken(str1)))

#=HGGetKeywordList(str1)
print('ㄴ)', HGGetKeywordList(str1))

'''
처리 결과
=============================================
ㄱ) ['원주율', '(', 'π', ',', ' ', 'paɪ', ',', ' ', '圓周率', ')', '은', ' ', '수학', ' ', '상수로', ' ', '3.1415926535', '...', '이다', '.']
ㄴ) ['원주율', 'π', 'paɪ', '圓周率', '은', '수학', '상수로', '3.1415926535', '이다']


'''
