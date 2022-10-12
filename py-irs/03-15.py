from tuple_base import tuple1
# 튜플(tuple) 처리 예: 탐색
# ㄱ)
if '흙' in tuple1: # 튜플에 있으면 True, 없으면 False
    print( "ㄱ) '흙' ===> 튜플에 있습니다.")
else:
    print( "ㄱ) '흙'===> 튜플에 없습니다.")
# ㄴ)
if '황제펭귄' not in tuple1: 
    print( "ㄴ) '황제펭귄'===> 튜플에 없습니다.")
else:
    print( "ㄴ) '황제펭귄'===> 튜플에 있습니다.")
# ㄷ)
print("ㄷ) '값' count:", tuple1.count('값'))  # 튜플에서 '값'의 빈도를 계산
# ㄹ)
print( "ㄹ) '형태' 위치:", tuple1.index('형태'))
# ㅁ)
print( "ㅁ) '황제펭귄' 위치:", tuple1.index('황제펭귄'))


'''
처리 결과:
=========================
ㄱ) '흙' ===> 튜플에 있습니다.
ㄴ) '황제펭귄'===> 튜플에 없습니다.
ㄷ) '값' count: 1
ㄹ) '형태' 위치: 3
Traceback (most recent call last):
  File "~.py", line 18, in <module>
    print( "ㅁ) '황제펭귄' 위치:", tuple1.index('황제펭귄'))
ValueError: tuple.index(x): x not in tuple
>>> 
'''

