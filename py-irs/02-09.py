from string_base import str41
# 문자열(str) 처리 예: 탐색
# ㄱ)
print( "ㄱ) '아름다운' 위치:", str41.rindex('아름다운'))
# ㄴ)
print( "ㄴ) '아름다운' 위치:", str41.rfind('아름다운'))
# ㄷ)
print( "ㄷ) '한국' 위치:", str41.rfind('한국'))
# ㄹ)
print( "ㄹ) '한국' 위치:", str41.rindex('한국'))


'''
처리 결과:
==============================
ㄱ) '아름다운' 위치: 10
ㄴ) '아름다운' 위치: 10
ㄷ) '한국' 위치: -1
==============================
Traceback (most recent call last):
  File "~.py", line 10, in <module>
    print( "ㄹ) '한국' 위치:", str41.rindex('한국'))
ValueError: substring not found
==============================

'''
