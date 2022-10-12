from string_base import str3, str31, str41
# 문자열(str) 처리 예: 변경

# ㄱ)
str31_r1 = str31.replace("대한민국", "한국")
print('ㄱ) ', str31, " --> ", str31_r1)

# ㄴ)
str31_r2 = str31.replace("코리아", "한국")
print('ㄴ) ', str31, " --> ", str31_r2)

# ㄷ)
str41_r1 = str41.replace("아름다운", "")
print('ㄷ) ', str41, " --> ", str41_r1)

# ㄹ)
print('ㄹ) 변경 전:', str3[2])
str3[2] = '선'
print('ㄹ) 변경 후:', str3)


'''
처리 결과:
==============================
ㄱ)  아름다운 대한민국  -->  아름다운 한국
ㄴ)  아름다운 대한민국  -->  아름다운 대한민국
ㄷ)  아름다운 대한민국 아름다운 코리아  -->   대한민국  코리아
ㄹ) 변경 전: 썬
Traceback (most recent call last):
  File "~.py", line 18, in <module>
    str3[2] = '선'
TypeError: 'str' object does not support item assignment

'''
