from dict_base import 한글사전
print('@@@ 편집 코드 : 한글사전 =', 한글사전) # 편집 코드

print(한글사전.keys()) # 편집 코드
print(한글사전.values()) # 편집 코드
print(한글사전.items()) # 편집 코드
print()

# 사전(dict) 처리 예: 항목 뒤집기
print('# ㄱ)')
한글사전_reversed = reversed(한글사전) # == reversed(d.keys())
print(type(한글사전_reversed))
#=print(한글사전_reversed) # 내용 대신 객체 주소를 보여줌.
한글사전_거꾸로 = {}
for key in 한글사전_reversed:
    한글사전_거꾸로[key] = 한글사전[key]
print(한글사전_거꾸로)
print()

print('# ㄴ)')
한글사전_reversed = reversed(한글사전.items())
print(type(한글사전_reversed))
#=print(한글사전_reversed) # 내용 대신 객체 주소를 보여줌.
한글사전_거꾸로 = {}
for key, value in 한글사전_reversed:
    한글사전_거꾸로[key] = value
print(한글사전_거꾸로)
print()

print('# ㄷ)')
한글사전_거꾸로 = dict(reversed(한글사전.items()))
print(한글사전_거꾸로)
print()



'''


================
@@@ 편집 코드 : 한글사전 = {'표제어': '흙', '품사': '명사', '등록자': '세종대왕'}
dict_keys(['표제어', '품사', '등록자'])
dict_values(['흙', '명사', '세종대왕'])
dict_items([('표제어', '흙'), ('품사', '명사'), ('등록자', '세종대왕')])

# ㄱ)
<class 'dict_reversekeyiterator'>
{'등록자': '세종대왕', '품사': '명사', '표제어': '흙'}

# ㄴ)
<class 'dict_reverseitemiterator'>
{'등록자': '세종대왕', '품사': '명사', '표제어': '흙'}

# ㄷ)
{'등록자': '세종대왕', '품사': '명사', '표제어': '흙'}

'''

