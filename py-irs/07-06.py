import hgsysinc
from hgkbd_test import String2KBDJamo_711
#-----------
# 초중종 자모를 두벌식 자모로 변환
String = '가자미' # 초중종 자모(Hangul Jamo) 자모: <-- 6글자 길이의 문자열(화면에 3글자로 보일 수도 있음)
String2KBDJamo_711(String)
print()

String = '낡' # 초중종 자모(Hangul Jamo) 자모: <-- 3글자 길이의 문자열(화면에 1글자로 보일 수도 있음)
String2KBDJamo_711(String)
print()



'''
출력 결과:
===================================
입력 (6): 가자미
두벌식 자모 문자열 (6): ㄱㅏㅈㅏㅁㅣ
음절 문자열 (3): 가자미

입력 (3): 낡
두벌식 자모 문자열 (4): ㄴㅏㄹㄱ
음절 문자열 (1): 낡
 

'''
