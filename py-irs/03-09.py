from list_base import hglist1
# 목록(list) 처리 예: 삭제 오류 처리
#----------
#----------
# ㄱ)
hglist1.remove('코끼리') # 목록에 없는 항목 삭제
'''
처리 결과:
=========================
Traceback (most recent call last):
  File "~.py", line 6, in <module>
    hglist1.remove('코끼리') # 목록에 없는 항목 삭제
ValueError: list.remove(x): x not in list
'''

#----------
#----------
# ㄴ)
try:
    hglist1.remove('코끼리') # 목록에 없는 항목 삭제
    print( "'코끼리' 삭제: 성공")
except ValueError: # list.remove(x): x not in list
    print( "'코끼리' 삭제: 실패")
print(hglist1)

'''
처리 결과:
=========================
'코끼리' 삭제: 실패
['조사', '흙', '값', '형태', '여덟', '체언']
'''

#----------
#----------
# ㄷ)
del hglist1[21] # 목록을 벗어난 index 위치의 항목을 삭제함.
'''
처리 결과:
=========================
Traceback (most recent call last):
  File "~.py", line 6, in <module>
    del hglist1[21] # 목록을 벗어난 index 위치의 항목을 삭제함.
IndexError: list assignment index out of range
'''

#----------
#----------
# ㄹ)
hglist1.pop(15) # 목록을 벗어난 index 위치의 항목을 삭제함.
'''
처리 결과:
=========================
Traceback (most recent call last):
  File "~.py", line 5, in <module>
    hglist1.pop(15) # 목록을 벗어난 index 위치의 항목을 삭제함.
IndexError: pop index out of range
'''


