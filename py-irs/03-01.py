# 목록(list) 처리 예: 생성
# ㄱ) 대괄호 생성
from list_base import hglist1
# ㄴ) 중복 항목
hglist20 = ['제주도', '거문도', '울릉도', '제주도']
print('ㄴ) hglist20:', hglist20)
# ㄷ) list((,,,)) 생성자: 튜플
hglist21 = list(('제주도', '거문도', '울릉도'))
print('ㄷ) hglist21:', hglist21)
# ㄹ) list([,,,]) 생성자: 목록
hglist22 = list(['제주도', '거문도', '울릉도'])
print('ㄹ) hglist22:', hglist22)
# ㅁ) list(str) 생성자: 문자열
hglist23 = list('제주도')
print('ㅁ) hglist23:', hglist23)
# ㅂ) list({,,,}) 생성자: 집합
hglist24 = list({'서울', '뉴델리', '런던', '자카르타'})
print('ㅂ) hglist24:', hglist24)
# ㅅ) list({,,,}) 생성자: 사전
hglist25 = list({'한국':'서울', '인도':'뉴델리', '영국':'런던'})
print('ㅅ) hglist25:', hglist25)


'''

처리 결과:
=========================
ㄴ) hglist20: ['제주도', '거문도', '울릉도', '제주도']
ㄷ) hglist21: ['제주도', '거문도', '울릉도']
ㄹ) hglist22: ['제주도', '거문도', '울릉도']
ㅁ) hglist23: ['제', '주', '도']
ㅂ) hglist24: ['런던', '자카르타', '뉴델리', '서울']
ㅅ) hglist25: ['한국', '인도', '영국']


'''
