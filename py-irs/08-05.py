import hgsysinc
from hgkbd_test import Hng2Eng_411, Hng2Eng_412, Hng2Eng_421
##----------
##----------
print('문자열을 영문자 문자열로 변환')
EngString1 = Hng2Eng_411('한')
EngString2 = Hng2Eng_411('하ㄴ')
EngString3 = Hng2Eng_411('ㅎㅏㄴ')
print()
print('영문자 문자열을 음절 문자열로 변환')
Hng2Eng_421(EngString1) # from 'gks' <== 'ㅎㅏㄴ' <== '한'
Hng2Eng_421(EngString2) # from 'gks' <== 'ㅎㅏㄴ' <== '하ㄴ'
Hng2Eng_421(EngString3) # from 'gks' <== 'ㅎㅏㄴ' <== 'ㅎㅏㄴ'


"""
출력 결과:
===================================
문자열을 영문자 문자열로 변환
한 : gks
하ㄴ : gks
ㅎㅏㄴ : gks

영문자 문자열을 음절 문자열로 변환
gks  ==>  ㅎㅏㄴ  ==>  한
gks  ==>  ㅎㅏㄴ  ==>  한
gks  ==>  ㅎㅏㄴ  ==>  한


"""

