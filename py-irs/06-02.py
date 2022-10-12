import hgsysinc
from hgunicode import hgGetChoJungJongString_Inx
#----------------------
#----------------------
#=ChoJungJongInx = {'cho':-1, 'jung':-1, 'jong':-1}
ChoJungJongInx = {
    'cho' :9, # 'ㅅ'
    'jung':0, # 'ㅏ'
    'jong':4, # 'ㄴ'
}
ChoJungJongString = hgGetChoJungJongString_Inx(ChoJungJongInx)
print(ChoJungJongInx, ':', ChoJungJongString)

'''
출력 결과:

응용프로그램에 따라 출력 모양이 다를 수 있음.
---------------------------------------
{'cho': 9, 'jung': 0, 'jong': 4} : 산
'''

