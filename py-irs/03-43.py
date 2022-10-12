from set_base import hgset1
# 집합(set) 처리 예: 삭제
# 편집 코드
print('@@@ 편집 코드: hgset1:', hgset1)
# ㄱ) 
hgset1.remove('참새')
print('ㄱ)', hgset1)
# ㄴ)
hgset1.discard('까치')
print('ㄴ)', hgset1)
# ㄷ)
delitem = hgset1.pop()
print('ㄷ) delitem:', delitem)
print('ㄷ)', hgset1)
# ㄹ)
hgset1.clear()
print('ㄹ)', hgset1)


'''
처리 결과:
=========================
@@@ 편집 코드: hgset1: {'참새', '오리', '닭', '비둘기', '까치'}
ㄱ) {'오리', '닭', '비둘기', '까치'}
ㄴ) {'오리', '닭', '비둘기'}
ㄷ) delitem: 오리
ㄷ) {'닭', '비둘기'}
ㄹ) set()

'''
