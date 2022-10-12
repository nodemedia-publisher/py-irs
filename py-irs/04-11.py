from sort_base import tuple21
print('@@@ tuple21 = ', tuple21) # 편집코드
# 정렬(sorted) 처리 예: 튜플
# ㄱ) 사전 순서
tuple_sort_s1 = sorted(tuple21) 
print('ㄱ)', tuple_sort_s1)
# ㄴ) 역순 정렬
tuple_sort_s2 = sorted(tuple21, reverse=True)
print('ㄴ)', tuple_sort_s2)
# ㄷ) 정렬 후 튜플 변환
tuple_sort_s3 = tuple(sorted(tuple21))
print('ㄷ)', tuple_sort_s3)

'''
처리 결과
===========================
@@@ tuple21 =  ('김치냉장고', '김치전', '김치', '김치볶음밥', '김치찌게')
ㄱ) ['김치', '김치냉장고', '김치볶음밥', '김치전', '김치찌게']
ㄴ) ['김치찌게', '김치전', '김치볶음밥', '김치냉장고', '김치']
ㄷ) ('김치', '김치냉장고', '김치볶음밥', '김치전', '김치찌게')
'''
 
