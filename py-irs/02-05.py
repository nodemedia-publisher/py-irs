# 문자열(str) 처리 예: 길이와 인덱스
str31 = "아름다운 대한민국"
# ㄱ)
print( "ㄱ) 문자열(str) 길이:", len(str31))
# ㄴ)
print( "ㄴ) 문자열(str) Index [2]:", str31[2]) # 앞에서 세 번째 '다' 출력
# ㄷ)
print( "ㄷ) 문자열(str) Index [-2]:", str31[-2]) # 뒤에서 2번째 '민' 출력
# ㄹ)
print("ㄹ) 문자열(str) Index [15]:", str31[15]) # 범위를 벗어나면 오류 발생


'''
처리 결과:
=================
ㄱ) 문자열(str) 길이: 9
ㄴ) 문자열(str) Index [2]: 다
ㄷ) 문자열(str) Index [-2]: 민
Traceback (most recent call last):
  File "~.py", line 10, in <module>
    print("ㄹ) 문자열(str) Index [15]:", str31[15]) # 범위를 벗어나면 오류 발생
IndexError: string index out of range
'''
