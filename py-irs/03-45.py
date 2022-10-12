from set_base import hgset1
# 집합(set) 처리 예: 삭제 오류 처리
hgset1.clear()
hgset1.pop() # 내용이 없는 집합에서 항목을 삭제함.
'''
처리 결과:
=========================
Traceback (most recent call last):
  File "~.py", line 4, in <module>
    hgset1.pop() # 내용이 없는 집합에서 항목을 삭제함.
KeyError: 'pop from an empty set'
'''



