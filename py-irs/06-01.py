import hgsysinc
from hgunicode import hgGetChoJungJongInx_Char
#----------------------
#----------------------
hgchar = '한'
ChoJungJongInx = hgGetChoJungJongInx_Char(hgchar)
print(hgchar, ':', ChoJungJongInx)

'''
출력 결과:
---------------------------------------
한 : {'cho': 18, 'jung': 0, 'jong': 4}

'''
