from dict_base import 한글사전
print('@@@편집 코드 : 한글사전 = ', 한글사전) # 편집 코드
# 사전(dict) 처리 예: for loop
print('# ㄱ)')
i = 0
for key in 한글사전:
    value = 한글사전[key]
    print( f"[{i}] : '{key}':'{value}'")
    i += 1
print()

print('# ㄴ)')
for i, key in enumerate(한글사전):
    value = 한글사전[key]
    print( f"[{i}] : '{key}':'{value}'")
print()




'''


================
편집 코드 : {'표제어': '흙', '품사': '명사', '등록자': '세종대왕'}

# ㄱ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

# ㄴ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

'''

