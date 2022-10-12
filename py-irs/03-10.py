from list_base import hglist1
# 목록(list) 처리 예: 복제
# ㄱ)
hglist_new = hglist1[2:5] # 목록에서 일부만 추출하여 새로운 목록 생성
print('ㄱ)', hglist_new)
# ㄴ)
hglist_new = hglist1[:5] # 'start' 생략: 목록에서 일부만 추출하여 새로운 목록 생성
print('ㄴ)', hglist_new)
# ㄷ)
hglist_new = hglist1[3:80] # 'end'(80)가 목록의 범위를 벗어난 경우
print('ㄷ)', hglist_new)
# ㄹ)
hglist_new = hglist1[::] # 목록에서 시작에서 끝까지 추출하여 새로운 목록 생성
print('ㄹ)', hglist_new)
# ㅁ)
hglist_new = hglist1[:] # 목록에서 시작에서 끝까지 추출하여 새로운 목록 생성
print('ㅁ)', hglist_new)
# ㅂ)
hglist_new = hglist1.copy()
print('ㅂ)', hglist_new)
# ㅅ)
hglist_new = hglist1[4:1:-1] # 목록 끝에서부터 일부만 추출하여 새로운 목록 생성
print('ㅅ)', hglist_new)
# ㅇ)
hglist_new = hglist1[::-1] # 목록 끝에서부터 전체를 추출하여 역순으로 새로운 목록 생성
print('ㅇ)', hglist_new)




'''
처리 결과:
=========================
ㄱ) ['값', '형태', '여덟']
ㄴ) ['조사', '흙', '값', '형태', '여덟']
ㄷ) ['형태', '여덟', '체언']
ㄹ) ['조사', '흙', '값', '형태', '여덟', '체언']
ㅁ) ['조사', '흙', '값', '형태', '여덟', '체언']
ㅂ) ['조사', '흙', '값', '형태', '여덟', '체언']
ㅅ) ['여덟', '형태', '값']
ㅇ) ['체언', '여덟', '형태', '값', '흙', '조사']

'''

