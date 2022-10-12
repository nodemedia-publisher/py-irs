import hgsysinc
from hgkbd_test import Hng2Jamo_511, Hng2Jamo_521

#----------
#----------
print('문자열을 두벌식 자모 문자열로 변환')
JaumMoumString1 = Hng2Jamo_511('한')
JaumMoumString2 = Hng2Jamo_511('하ㄴ')
JaumMoumString3 = Hng2Jamo_511('ㅎㅏㄴ')
print()
print('두벌식 자모 문자열을 음절 문자열로 변환')
Hng2Jamo_521(JaumMoumString1) # from 'ㅎㅏㄴ' <== '한'
Hng2Jamo_521(JaumMoumString2) # from 'ㅎㅏㄴ' <== '하ㄴ'
Hng2Jamo_521(JaumMoumString3) # from 'ㅎㅏㄴ' <== 'ㅎㅏㄴ'



'''
출력 결과:
===================================
문자열을 두벌식 자모 문자열로 변환
한 : ㅎㅏㄴ
하ㄴ : ㅎㅏㄴ
ㅎㅏㄴ : ㅎㅏㄴ

두벌식 자모 문자열을 음절 문자열로 변환
ㅎㅏㄴ : 한
ㅎㅏㄴ : 한
ㅎㅏㄴ : 한

 

'''
