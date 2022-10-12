from string_base import (
str202_e1, #= 'ʧipmʌŋk' # 영어(chipmunk:다람쥐)의 발음 기호
str202_s1, #= 'español' # 스페인어: 스페인어
str202_d2, #= 'außerhalb' # 독일어
str202_d3, #= 'läuten' # 독일어: 종을 울리다.
str202_f1, #= 'fâcheux' # 프랑스어: 속상하다
str202_f2, #= 'maɲifik' # 프랑스어(magnifique)의 발음 기호
str202_j1, #= 'サッポ' # 일본어: 삿포르
str202_r1, #= 'Одесса' # 러시아어: 오데사
str202_sd1,#= 'Tjåkkå' # 스웨덴어: 감사하다
str202_k1, #= '한국'
str202_c1, #= '中國'
str211, #= '123'
)

# 함수 처리 예: 알파벳 확인
print(f"ㄱ) [{str202_k1}] isalpha :", str202_k1.isalpha())
print(f"ㄴ) [{str202_c1}] isalpha :", str202_c1.isalpha())
print(f"ㄷ) [{str202_j1}] isalpha :", str202_j1.isalpha())
print(f"ㄹ) [{str202_e1}] isalpha :", str202_e1.isalpha())
print(f"ㅁ) [{str202_s1}] isalpha :", str202_s1.isalpha())
print(f"ㅂ) [{str202_d2}] isalpha :", str202_d2.isalpha())
print(f"ㅅ) [{str202_d3}] isalpha :", str202_d3.isalpha())
print(f"ㅇ) [{str202_f1}] isalpha :", str202_f1.isalpha())
print(f"ㅈ) [{str202_f2}] isalpha :", str202_f2.isalpha())
print(f"ㅊ) [{str202_r1}] isalpha :", str202_r1.isalpha())
print(f"ㅋ) [{str202_sd1}] isalpha :", str202_sd1.isalpha())
print(f"ㅌ) [{str211}] isalpha :", str211.isalpha())
 

'''
처리 결과:
=============================
ㄱ) [한국] isalpha : True
ㄴ) [中國] isalpha : True
ㄷ) [サッポ] isalpha : True
ㄹ) [ʧipmʌŋk] isalpha : True
ㅁ) [español] isalpha : True
ㅂ) [außerhalb] isalpha : True
ㅅ) [läuten] isalpha : True
ㅇ) [fâcheux] isalpha : True
ㅈ) [maɲifik] isalpha : True
ㅊ) [Одесса] isalpha : True
ㅋ) [Tjåkkå] isalpha : True
ㅌ) [123] isalpha : False

'''


