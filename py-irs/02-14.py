from string_base import str31, str33

# 문자열(str) 처리 예: 문자열 합치기('+')

# ㄱ)
str3133 = str31 + ' ' + str33
print('ㄱ) :', str3133)

# ㄴ)
emoji__2 = '❤☘'
str__3 = emoji__2 * 3
print('ㄴ) :', str__3)

# ㄷ)
int__5 = 5
str__5 = emoji__2 +str(int__5) # 문자열과 숫자를 합치기
print('ㄷ) :', str__5)

# ㄹ)
str__5 = emoji__2 + int__5 # 문자열과 숫자를 합치기
print('ㄹ) :', str__5)


'''
처리 결과:
==============================
ㄱ) : 아름다운 대한민국 원더풀 제주도
ㄴ) : ❤☘❤☘❤☘
ㄷ) : ❤☘5
--------------------------
Traceback (most recent call last):
  File "~.py", line 16, in <module>
      str__5 = emoji__2 + int__5 # 문자열과 숫자를 합치기
TypeError: can only concatenate str (not "int") to str
--------------------------
'''

