from tuple_base import tuple1
# 튜플(tuple) 처리 예: 길이와 인덱스
# ㄱ)
print( "ㄱ) 튜플(tuple) 개수:", len(tuple1))
# ㄴ)
print( "ㄴ) 튜플(tuple) Index [2]:", tuple1[2]) # 앞에서 세 번째 '값' 출력
# ㄷ)
print( "ㄷ) 튜플(tuple) Index [-2]:", tuple1[-2]) # 뒤에서 2번째 '여덟' 출력
# ㄹ)
print("ㄹ) 튜플(tuple) Index [15]:", tuple1[15]) # 범위를 벗어나면 오류 발생
'''
===> 오류 발생
Traceback (most recent call last):
  File "~.py", line 10, in <module>
    print("ㄹ) 튜플(tuple) Index [15]:", tuple1[15]) # 범위를 벗어나면 오류 발생
IndexError: tuple index out of range
'''




'''
처리 결과:
=========================
ㄱ) 튜플(tuple) 개수: 6
ㄴ) 튜플(tuple) Index [2]: 값
ㄷ) 튜플(tuple) Index [-2]: 여덟
Traceback (most recent call last):
  File "~.py", line 10, in <module>
    print("ㄹ) 튜플(tuple) Index [15]:", tuple1[15]) # 범위를 벗어나면 오류 발생
IndexError: tuple index out of range
>>> 
'''

