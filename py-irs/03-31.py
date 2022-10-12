from dict_base import 한글사전
print('@@@ 편집 코드 : 한글사전 =', 한글사전) # 편집 코드
# 사전(dict) 처리 예: dict.items()
print('# ㄱ)')
i = 0
for item in 한글사전.items():
    key = item[0]
    value = item[1]
    print( f"[{i}] : '{key}':'{value}'")
    i += 1
print()

print('# ㄴ)')
for i, item in enumerate(한글사전.items()):
    key = item[0]
    value = item[1]
    print( f"[{i}] : '{key}':'{value}'")
print()

print('# ㄷ)')
i = 0
for key, value in 한글사전.items():
    print( f"[{i}] : '{key}':'{value}'")
    i += 1
print()




'''
처리 결과:
================
@@@ 편집 코드 : 한글사전 = {'표제어': '흙', '품사': '명사', '등록자': '세종대왕'}
# ㄱ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

# ㄴ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

# ㄷ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'


'''

