# 튜플(tuple) 처리 예: 생성
# ㄱ) 소괄호 생성
from tuple_base import tuple1
# ㄴ) 중복 항목
tuple20 = ('제주도', '거문도', '울릉도', '제주도')
print('ㄴ) tuple20:', tuple20)
# ㄷ) 쉼표 생성
tuple21 = '제주도', '거문도', '울릉도'
print('ㄷ) tuple21:', tuple21)
# ㄹ) tuple((,,,)) 생성자: 튜플
tuple22 = tuple(('제주도', '거문도', '울릉도'))
print('ㄹ) tuple22:', tuple22)
# ㅁ) tuple((,,,)) 생성자: 목록
tuple23 = tuple(['제주도', '거문도', '울릉도'])
print('ㅁ) tuple23:', tuple23)
# ㅂ) tuple((,,,)) 생성자: 문자열
tuple24 = tuple('제주도')
print('ㅂ) tuple24:', tuple24)
# ㅅ) tuple({,,,}) 생성자: 집합
tuple25 = tuple({'서울', '뉴델리', '런던'})
print('ㅅ) tuple25:', tuple25)
# ㅇ) tuple({,,,}) 생성자: 사전
tuple26 = tuple({'한국':'서울', '인도':'뉴델리', '영국':'런던'})
print('ㅇ) tuple26:', tuple26)



'''
처리 결과:
=========================
ㄴ) tuple20: ('제주도', '거문도', '울릉도', '제주도')
ㄷ) tuple21: ('제주도', '거문도', '울릉도')
ㄹ) tuple22: ('제주도', '거문도', '울릉도')
ㅁ) tuple23: ('제주도', '거문도', '울릉도')
ㅂ) tuple24: ('제', '주', '도')
ㅅ) tuple25: ('뉴델리', '런던', '서울')
ㅇ) tuple26: ('한국', '인도', '영국')

'''

