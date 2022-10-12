from list_base import hglist1, hglist2, hglist3
# 목록(list) 처리 예: 확장과 합성
# ㄱ)
hglist1.extend(hglist2)
print('ㄱ)', hglist1)
# ㄴ)
hglist23 = hglist2 + hglist3
print('ㄴ)', hglist23)


'''

처리 결과:
=========================
ㄱ) ['조사', '흙', '값', '형태', '여덟', '체언', '앞', '형태소', '콩']
ㄴ) ['앞', '형태소', '콩', '뒤', '문법', '해운대']

'''
