from set_base import hgset1, hgset2
# 집합(set) 처리 예: 연산
print(f'@@@ hgset1 ({len(hgset1)}):', hgset1) # 편집 코드
print(f'@@@ hgset2 ({len(hgset2)}):', hgset2) # 편집 코드
# ㄱ) 교집합
hgset12i = hgset1.intersection(hgset2)
print('ㄱ) intersection hgset12i:', hgset12i)

# ㄴ) 합집합
hgset12u = hgset1.union(hgset2)
print('ㄴ) union hgset12u:', hgset12u)

# ㄷ) 차집합
hgset12d = hgset1.difference(hgset2)
print('ㄷ) difference hgset12d:', hgset12d)

# ㄹ) 대칭 차집합
hgset12sd = hgset1.symmetric_difference(hgset2)
print('ㄹ) symmetric difference hgset12sd:', hgset12sd)

# ㅁ) 교집합(&)
hgset12i = hgset1 & hgset2 # intersection
print("ㅁ) intersection(&) hgset12i:", hgset12i)

# ㅂ) 합집합(|)
hgset12u = hgset1 | hgset2 # union
print("ㅂ) union(|) hgset12u:", hgset12u)

# ㅅ) 차집합(-)
hgset12d = hgset1 - hgset2 # difference
print("ㅅ) difference(-) hgset12d:", hgset12d)

# ㅇ) 대칭 차집합(^)
hgset12sd = hgset1 ^ hgset2 # symmetric difference
print('ㅇ) symmetric difference(^) hgset12sd:', hgset12sd)


'''

처리 결과:
=========================
@@@ hgset1 (5): {'참새', '닭', '까치', '오리', '비둘기'}
@@@ hgset2 (4): {'닭', '사자', '표범', '참새'}
ㄱ) intersection hgset12i: {'닭', '참새'}
ㄴ) union hgset12u: {'참새', '닭', '사자', '까치', '오리', '표범', '비둘기'}
ㄷ) difference hgset12d: {'오리', '비둘기', '까치'}
ㄹ) symmetric difference hgset12sd: {'오리', '표범', '사자', '비둘기', '까치'}
ㅁ) intersection(&) hgset12i: {'닭', '참새'}
ㅂ) union(|) hgset12u: {'참새', '닭', '사자', '까치', '오리', '표범', '비둘기'}
ㅅ) difference(-) hgset12d: {'오리', '비둘기', '까치'}
ㅇ) symmetric difference(^) hgset12sd: {'오리', '표범', '사자', '비둘기', '까치'}

'''
