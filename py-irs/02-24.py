from string_base import (
str202_e1, #= 'ʧipmʌŋk' # 영어(chipmunk:다람쥐)의 발음 기호
str202_s1, #= 'español' # 스페인어: 스페인어
str202_d2, #= 'außerhalb' # 독일어
str202_d3, #= 'läuten' # 독일어: 종을 울리다.
str202_f1, #= 'fâcheux' # 프랑스어: 속상하다
str202_f2, #= 'maɲifik' # 프랑스어(magnifique)의 발음 기호
str202_j1, #= 'サッポ' # 일본어: 삿포르
str202_r1, #= 'Одесса' # 러이사어: 오데사
str202_sd1,#= 'Tjåkkå' # 스웨덴어: 감사하다
str202_k1, #= '한국'
str202_c1, #= '中國'
str211, #= '123'
)

# 함수 처리 예: 대문자 변환
print(f"ㄱ) [{str202_k1}] islower :", str202_k1.islower(), str202_k1.upper())
print(f"ㄴ) [{str202_c1}] islower :", str202_c1.islower(), str202_c1.upper())
print(f"ㄷ) [{str202_j1}] islower :", str202_j1.islower(), str202_j1.upper())
print(f"ㄹ) [{str202_e1}] islower :", str202_e1.islower(), str202_e1.upper())
print(f"ㅁ) [{str202_s1}] islower :", str202_s1.islower(), str202_s1.upper())
print(f"ㅂ) [{str202_d2}] islower :", str202_d2.islower(), str202_d2.upper())
print(f"ㅅ) [{str202_d3}] islower :", str202_d3.islower(), str202_d3.upper())
print(f"ㅇ) [{str202_f1}] islower :", str202_f1.islower(), str202_f1.upper())
print(f"ㅈ) [{str202_f2}] islower :", str202_f2.islower(), str202_f2.upper())
print(f"ㅊ) [{str202_r1}] islower :", str202_r1.islower(), str202_r1.upper())
print(f"ㅋ) [{str202_sd1}] islower :", str202_sd1.islower(), str202_sd1.upper())
print(f"ㅌ) [{str211}] islower :", str211.islower(), str211.upper())

 


'''
처리 결과:
=============================
ㄱ) [한국] islower : False 한국
ㄴ) [中國] islower : False 中國
ㄷ) [サッポ] islower : False サッポ
ㄹ) [ʧipmʌŋk] islower : True ʧIPMɅŊK
ㅁ) [español] islower : True ESPAÑOL
ㅂ) [außerhalb] islower : True AUSSERHALB
ㅅ) [läuten] islower : True LÄUTEN
ㅇ) [fâcheux] islower : True FÂCHEUX
ㅈ) [maɲifik] islower : True MAƝIFIK
ㅊ) [Одесса] islower : False ОДЕССА
ㅋ) [Tjåkkå] islower : False TJÅKKÅ
ㅌ) [123] islower : False 123


'''


