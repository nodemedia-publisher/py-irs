import hgsysinc
from hgkbd_test import String2KBDJamo_711
#-----------
# 반각 자모를 두벌식 자모로 변환
String = 'ﾡￂﾸￂﾱￜ' # 반각(Halfwidth) 자모: <-- 'ㄱㅏㅈㅏㅁㅣ' <-- {가자미}
String2KBDJamo_711(String)
print()

String = 'ﾾￂﾤﾡￓﾡ' # 반각(Halfwidth) 자모: <-- 'ㅎㅏㄴㄱㅜㄱ' <-- {한국}
String2KBDJamo_711(String)
print()




'''
출력 결과:
===================================
입력 (6): ﾡￂﾸￂﾱￜ
두벌식 자모 문자열 (6): ㄱㅏㅈㅏㅁㅣ
음절 문자열 (3): 가자미

입력 (6): ﾾￂﾤﾡￓﾡ
두벌식 자모 문자열 (6): ㅎㅏㄴㄱㅜㄱ
음절 문자열 (2): 한국
 

'''
