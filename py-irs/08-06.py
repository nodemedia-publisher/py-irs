import hgsysinc
from hgkbd import HGTransString2EngString
##----------
##----------
# 반각 자모를 영문자로 변환
String = 'ﾱￇￇￜﾧ' # 반각(Halfwidth) 자모: <-- 'ㅁㅔㅔㅣㄷ' <-- 'apple'
EngString = HGTransString2EngString(String)
print('반각 자모:', String)
print('영문자:', EngString)
print()

String = 'ﾤﾱￚﾤￊￓﾾ' # 반각(Halfwidth) 자모: <-- 'ㄴ므녀ㅜㅎ' <-- 'samsung'
EngString = HGTransString2EngString(String)
print('반각 자모:', String)
print('영문자:', EngString)
print()


'''
처리 결과:


================================

반각 자모: ﾱￇￇￜﾧ
영문자: apple

반각 자모: ﾤﾱￚﾤￊￓﾾ
영문자: samsung


'''

