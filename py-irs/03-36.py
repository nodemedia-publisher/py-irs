from set_base import hgset1, hgset2, hgset3
# 집합(set) 처리 예: 추가
# ㄱ)
hgset1.add('알바트로스')
print('ㄱ) hgset1:', hgset1)

# ㄴ)
hgset1.update(hgset2)
print('ㄴ) [후] hgset1:', hgset1)

# ㄷ) # set.add()와 set.update()를 혼동하는 사례
print('ㄷ) [전] hgset3:', hgset3)
hgset3.update('펭귄')
print('ㄷ) [후] hgset3:', hgset3)


'''

처리 결과:
=========================
ㄱ) hgset1: {'알바트로스', '비둘기', '오리', '까치', '참새', '닭'}
ㄴ) [후] hgset1: {'알바트로스', '비둘기', '오리', '까치', '사자', '참새', '표범', '닭'}
ㄷ) [전] hgset3: {'곰', '늑대', '호랑이'}
ㄷ) [후] hgset3: {'곰', '귄', '호랑이', '펭', '늑대'}

'''
