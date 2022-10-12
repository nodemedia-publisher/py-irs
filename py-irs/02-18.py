from string_base import str31

# 문자열(str) 처리 예: 변경

# ㄱ) 실행할 수 없는 코드
str31[2] = '가' # 항목 내용 변경
print('ㄱ) :', str31)
'''
Traceback (most recent call last):
  File "~.py", line 6, in <module>
    str31[2] = '가' # 항목 내용 변경
TypeError: 'str' object does not support item assignment
'''

# ㄴ) 실행할 수 없는 코드
str31[5:9] = '코리아 ' # 인덱스 5번째 글자부터 9번째 직전(8번째) 글자까지
print('ㄴ) :', str31)
'''
Traceback (most recent call last):
  File "~.py", line 16, in <module>
    str31[5:9] = '코리아 ' # 인덱스 5번째 글자부터 9번째 직전(8번째) 글자까지
TypeError: 'str' object does not support item assignment
'''

