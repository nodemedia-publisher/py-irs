from string_base import str50, str51
# 문자열(str) 처리 예: 변경
#----- 아래 두 줄은 편집 코드
print(f'str50 ({len(str50)}):', str50) # 편집 코드
print(f'str51 ({len(str51)}):', str51) # 편집 코드
#-----

# ㄱ)
str50_r1 = str50.lstrip('@')
print(f'ㄱ) ({len(str50_r1)}):', str50_r1)

# ㄴ)
str50_r2 = str50.rstrip('#')
print(f'ㄴ) ({len(str50_r2)}):', str50_r2)

# ㄷ)
str50_r3 = str50.strip('@#$')
print(f'ㄷ) ({len(str50_r3)}):', str50_r3)

# ㄹ)
str51_r1 = str51.lstrip()
print(f'ㄹ) ({len(str51_r1)}):', str51_r1)

# ㅁ)
str51_r2 = str51.rstrip()
print(f'ㅁ) ({len(str51_r2)}):', str51_r2)

# ㅂ)
str51_r3 = str51.strip()
print(f'ㅂ) ({len(str51_r3)}):', str51_r3)




'''
처리 결과:
==============================
ㄱ) (12): 아름다운 대한민국###
ㄴ) (12): @@@아름다운 대한민국
ㄷ) (9): 아름다운 대한민국
ㄹ) (12): 아름다운 대한민국   
ㅁ) (12):    아름다운 대한민국
ㅂ) (9): 아름다운 대한민국

'''

