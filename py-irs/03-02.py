from list_base import hglist1
# 목록(list) 처리 예: 길이와 인덱스
# ㄱ)
print( "ㄱ) 목록(list) 개수:", len(hglist1))
# ㄴ)
print( "ㄴ) 목록(list) Index [2]:", hglist1[2]) # 앞에서 세 번째 '값' 출력
# ㄷ)
print( "ㄷ) 목록(list) Index [-2]:", hglist1[-2]) # 뒤에서 2번째 '여덟' 출력
# ㄹ)
hglist1[-2] = '접미사' # 항목 내용 변경
print( "ㄹ) 목록(list) Index [-2]:", hglist1[-2]) # 뒤에서 2번째 바뀐 값 '접미사' 출력
# ㅁ)
print("ㅁ) 목록(list) Index [15]:", hglist1[15]) # 범위를 벗어나면 오류 발생
'''
===> 오류 발생
Traceback (most recent call last):
  File "~.py", line 13, in <module>
    print( "목록(list) Index 15:", hglist1[15]) # 범위를 벗어나면 오류 발생
IndexError: list index out of range
'''




'''
처리 결과:
=========================

ㄱ) 목록(list) 개수: 6
ㄴ) 목록(list) Index [2]: 값
ㄷ) 목록(list) Index [-2]: 여덟
ㄹ) 목록(list) Index [-2]: 접미사
Traceback (most recent call last):
  File "~.py", line 13, in <module>
    print("ㅁ) 목록(list) Index [15]:", hglist1[15]) # 범위를 벗어나면 오류 발생
IndexError: list index out of range
>>> 


'''

