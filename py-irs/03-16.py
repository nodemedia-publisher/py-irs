from tuple_base import tuple1, tuple2, tuple3
#----- 편집 코드
print('@@@ tuple2:', tuple2) # 편집 코드
print('@@@ tuple3:', tuple3) # 편집 코드
#-----
# 튜플(tuple) 처리 예: 합성과 복제
# ㄱ)
tuple23 = tuple2 + tuple3
print('ㄱ) tuple23:', tuple23)
# ㄴ) 부분 복제
tuple_new = tuple1[2:5] # 튜플에서 일부만 추출하여 새로운 튜플 생성
print('ㄴ)', tuple_new)
# ㄷ)
tuple_new = tuple1[:5] # 'start' 생략: 튜플에서 일부만 추출하여 새로운 튜플 생성
print('ㄷ)', tuple_new)
# ㄹ)
tuple_new = tuple1[3:80] # 'end'(80)가 튜플의 범위를 벗어난 경우
print('ㄹ)', tuple_new)
# ㅁ) 부분 복제 방식으로 전체 복사
tuple_new = tuple1[::] # 튜플에서 시작에서 끝까지 추출하여 새로운 튜플 생성
print('ㅁ)', tuple_new)
# ㅂ) 부분 복제 방식으로 전체 복사
tuple_new = tuple1[:] # 튜플에서 시작에서 끝까지 추출하여 새로운 튜플 생성
print('ㅂ)', tuple_new)
# ㅅ)
tuple_new = tuple1[4:1:-1] # 튜플 끝에서부터 일부만 추출하여 새로운 튜플 생성
print('ㅅ)', tuple_new)
# ㅇ)
tuple_new = tuple1[::-1] # 튜플 끝에서부터 전체를 추출하여 역순으로 새로운 튜플 생성
print('ㅇ)', tuple_new)

#=# ㅈ)
#=tuple_new = tuple1.copy() # 튜플은 copy() 함수를 지원하지 않아 오류 발생
#=print('ㅈ)', tuple_new)
'''
Traceback (most recent call last):
  File "~.py", line 31, in <module>
    tuple_new = tuple1.copy()
AttributeError: 'tuple' object has no attribute 'copy'
'''



'''
처리 결과:
=========================
@@@ tuple2: ('앞', '형태소', '콩')
@@@ tuple3: ('뒤', '문법', '해운대')
ㄱ) tuple23: ('앞', '형태소', '콩', '뒤', '문법', '해운대')
ㄴ) ('값', '형태', '여덟')
ㄷ) ('조사', '흙', '값', '형태', '여덟')
ㄹ) ('형태', '여덟', '체언')
ㅁ) ('조사', '흙', '값', '형태', '여덟', '체언')
ㅂ) ('조사', '흙', '값', '형태', '여덟', '체언')
ㅅ) ('여덟', '형태', '값')
ㅇ) ('체언', '여덟', '형태', '값', '흙', '조사')

'''
