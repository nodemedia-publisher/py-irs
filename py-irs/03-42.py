from set_base import hgset1, hgset2, hgset3, hgset31, hgset32
# 집합(set) 처리 예: 검사
print(f'@@@ hgset1 ({len(hgset1)}):', hgset1) # 편집 코드
print(f'@@@ hgset2 ({len(hgset2)}):', hgset2) # 편집 코드
print(f'@@@ hgset3 ({len(hgset3)}):', hgset3) # 편집 코드
print(f'@@@ hgset31 ({len(hgset31)}):', hgset31) # 편집 코드
print(f'@@@ hgset32 ({len(hgset32)}):', hgset32) # 편집 코드
# ㄱ) 공통 항목이 없는지 검사
print('ㄱ1) hgset1 isdisjoint hgset2:', hgset1.isdisjoint(hgset2))
print('ㄱ2) hgset1 isdisjoint hgset3:', hgset1.isdisjoint(hgset3))
# ㄴ) 부분 집합 검사
print('ㄴ1) hgset2 issubset hgset32:', hgset2.issubset(hgset32))
print('ㄴ2) hgset32 issubset hgset2:', hgset32.issubset(hgset2))
print('ㄴ3) hgset2 issubset hgset2:', hgset2.issubset(hgset2))
# ㄷ) 상위 집합 검사
print('ㄷ1) hgset2 issuperset hgset32:', hgset2.issuperset(hgset32))
print('ㄷ2) hgset32 issuperset hgset2:', hgset32.issuperset(hgset2))
print('ㄷ3) hgset2 issuperset hgset2:', hgset2.issuperset(hgset2))



'''

처리 결과:
=========================

@@@ hgset1 (5): {'오리', '비둘기', '까치', '닭', '참새'}
@@@ hgset2 (4): {'참새', '사자', '표범', '닭'}
@@@ hgset3 (3): {'늑대', '곰', '호랑이'}
@@@ hgset31 (6): {'까마귀', '오리', '비둘기', '까치', '닭', '참새'}
@@@ hgset32 (5): {'사자', '표범', '독수리', '닭', '참새'}
ㄱ1) hgset1 isdisjoint hgset2: False
ㄱ2) hgset1 isdisjoint hgset3: True
ㄴ1) hgset2 issubset hgset32: True
ㄴ2) hgset32 issubset hgset2: False
ㄴ3) hgset2 issubset hgset2: True
ㄷ1) hgset2 issuperset hgset32: False
ㄷ2) hgset32 issuperset hgset2: True
ㄷ3) hgset2 issuperset hgset2: True

'''
