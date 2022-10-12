from set_base import hgset1, hgset2, hgset3, hgset21, hgset22, hgset23
# 집합(set) 처리 예: 갱신 연산
print(f'@@@ hgset1 ({len(hgset1)}):', hgset1) # 편집 코드
print(f'@@@ hgset2 ({len(hgset2)}):', hgset2) # 편집 코드
print(f'@@@ hgset3 ({len(hgset3)}):', hgset3) # 편집 코드
print(f'@@@ hgset21({len(hgset21)}):', hgset21) # 편집 코드
print(f'@@@ hgset22 ({len(hgset22)}):', hgset22) # 편집 코드
print(f'@@@ hgset23 ({len(hgset23)}):', hgset23) # 편집 코드
# ㄱ) 교집합(&) 갱신
hgset1 &= hgset2
print('ㄱ) intersection update hgset1:', hgset1)
# ㄴ) 차집합(-) 갱신
hgset2 -= hgset21 # difference
print('ㄴ) difference update hgset2:', hgset2)
# ㄷ) 대칭 차집합(^) 갱신
hgset22 ^= hgset21
print('ㄷ) symmetric difference update hgset22:', hgset22)
# ㄹ) 합집합(|) 갱신
hgset3 |= hgset23
print('ㄹ) union_update hgset3:', hgset3)
"""
set.union_update() 함수는 없지만 이런 효과를 내는 '|=' 연산은 가능하다.
"""

'''

처리 결과:
=========================
@@@ hgset1 (5): {'참새', '비둘기', '까치', '닭', '오리'}
@@@ hgset2 (4): {'참새', '닭', '표범', '사자'}
@@@ hgset3 (3): {'곰', '호랑이', '늑대'}
@@@ hgset21(4): {'닭', '까치', '오리', '까마귀'}
@@@ hgset22 (4): {'닭', '곰', '호랑이', '사자'}
@@@ hgset23 (3): {'표범', '호랑이', '사자'}

ㄱ) intersection update hgset1: {'참새', '닭'}
ㄴ) difference update hgset2: {'참새', '표범', '사자'}
ㄷ) symmetric difference update hgset22: {'곰', '까치', '사자', '오리', '까마귀', '호랑이'}
ㄹ) union_update hgset3: {'곰', '늑대', '표범', '호랑이', '사자'}



'''