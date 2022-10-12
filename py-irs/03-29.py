from dict_base import 한글사전
print('@@@ 편집 코드 : 한글사전 =', 한글사전) # 편집 코드
# 사전(dict) 처리 예: dict.keys()
print('# ㄱ) 한글사전.keys() len:', len(한글사전.keys()))
print()

print('# ㄴ)')
i = 0
for key in 한글사전.keys():
    value = 한글사전[key]
    print( f"[{i}] : '{key}':'{value}'")
    i += 1
print()

print('# ㄷ)')
for i, key in enumerate(한글사전.keys()):
    value = 한글사전[key]
    print( f"[{i}] : '{key}':'{value}'")
print()




'''

처리 결과:

================
@@@ 편집 코드 : 한글사전 = {'표제어': '흙', '품사': '명사', '등록자': '세종대왕'}
# ㄱ) 한글사전.keys() len: 3

# ㄴ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

# ㄷ)
[0] : '표제어':'흙'
[1] : '품사':'명사'
[2] : '등록자':'세종대왕'

'''

