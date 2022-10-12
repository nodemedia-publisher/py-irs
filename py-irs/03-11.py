from list_base import hglist1, hglist102
# 목록(list) 처리 예: 정렬
# ㄱ)
hglist1.sort()
print('ㄱ)', hglist1)
# ㄴ)
hglist1.sort(reverse=True)
print('ㄴ)', hglist1)
# ㄷ)
hglist102.reverse() # 앞은 뒤로 보내고, 뒤는 앞으로 보낸다.
print('ㄷ)', hglist102)



'''
처리 결과:
=========================
ㄱ) ['값', '여덟', '조사', '체언', '형태', '흙']
ㄴ) ['흙', '형태', '체언', '조사', '여덟', '값']
ㄷ) ['十', '九', '八', '七', '六', '五', '四', '三', '二', '一']

'''
