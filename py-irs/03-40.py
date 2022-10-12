from set_base import hgset1, hgset2, hgset21, hgset22
# 집합(set) 처리 예: 갱신 연산
print(f'@@@ hgset1 ({len(hgset1)}):', hgset1) # 편집 코드
print(f'@@@ hgset2 ({len(hgset2)}):', hgset2) # 편집 코드
print(f'@@@ hgset21 ({len(hgset21)}):', hgset21) # 편집 코드
print(f'@@@ hgset22 ({len(hgset22)}):', hgset22) # 편집 코드

# ㄱ) 교집합 갱신
hgset1.intersection_update(hgset2)
print('ㄱ) intersection update hgset1:', hgset1)
# ㄴ) 차집합 갱신
hgset2.difference_update(hgset21)
print('ㄴ) difference update hgset2:', hgset2)
# ㄷ) 대칭 차집합 갱신
hgset22.symmetric_difference_update(hgset21)
print('ㄷ) symmetric difference update hgset22:', hgset22)
# ㄹ) 합집합 갱신
hgset1.union_update(hgset2) # AttributeError: 'set' object has no attribute 'union_update'
print('ㄹ) union_update hgset1:', hgset1)
print()


'''

처리 결과:
=========================
@@@ hgset1 (5): {'오리', '까치', '닭', '참새', '비둘기'}
@@@ hgset2 (4): {'닭', '표범', '참새', '사자'}
@@@ hgset21 (4): {'까치', '닭', '까마귀', '오리'}
@@@ hgset22 (4): {'호랑이', '곰', '닭', '사자'}

ㄱ) intersection update hgset1: {'닭', '참새'}
ㄴ) difference update hgset2: {'표범', '참새', '사자'}
ㄷ) symmetric difference update hgset22: {'오리', '호랑이', '곰', '까치', '까마귀', '사자'}
Traceback (most recent call last):
  File "~.py", line 18, in <module>
    hgset1.union_update(hgset2) # AttributeError: 'set' object has no attribute 'union_update'
AttributeError: 'set' object has no attribute 'union_update'

'''
