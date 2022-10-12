from string_base import str32
# 문자열(str) 처리 예: 탐색
# ㄱ)
if '대한' in str32: # 문자열에 있으면 True, 없으면 False
    print( "'대한' ===> 문자열에 있습니다.")
else:
    print( "'대한'===> 문자열에 없습니다.")
# ㄴ)
if '한국' not in str32: 
    print( "'한국'===> 문자열에 없습니다.")
else:
    print( "'한국'===> 문자열에 있습니다.")
# ㄷ)
print("'다' count:", str32.count('다'))  # 문자열에서 '다'의 빈도를 계산
# ㄹ)
print( "'대한' 위치:", str32.index('대한'))
# ㅁ)
print( "'코리아' 위치:", str32.index('코리아'))



'''
처리 결과:
=================
'대한' ===> 문자열에 있습니다.
'한국'===> 문자열에 없습니다.
'다' count: 2
'대한' 위치: 5
Traceback (most recent call last):
  File "~.py", line 18, in <module>
    print( "'코리아' 위치:", str32.index('코리아'))
ValueError: substring not found

'''
