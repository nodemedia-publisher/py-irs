from list_base import hglist1, hglist2, hglist3
# 목록(list) 처리 예: 삭제
# ㄱ)
hglist1.remove('형태')
print('ㄱ)', hglist1)
# ㄴ)
del hglist1[2] # 목록에서 지정한 index 위치에 항목을 삭제함.
print('ㄴ)', hglist1)
# ㄷ)
print('ㄷ) 처리 전:', hglist2)
delitem = hglist2.pop(1) # 목록에서 지정한 index 위치에 항목을 삭제함.
print('ㄷ) delitem:', delitem)
print('ㄷ) 처리 후', hglist2)
# ㄹ)
hglist2.pop() # 목록에서 맨 끝에 있는 항목을 삭제함.
print('ㄹ)', hglist2)
# ㅁ)
print('ㅁ) clear() 전 :', hglist3)
hglist3.clear() # 목록 전체를 삭제
print('ㅁ) clear() 후 :', hglist3)


'''
처리 결과:
=========================
ㄱ) ['조사', '흙', '값', '여덟', '체언']
ㄴ) ['조사', '흙', '여덟', '체언']
ㄷ) 처리 전: ['앞', '형태소', '콩']
ㄷ) delitem: 형태소
ㄷ) 처리 후 ['앞', '콩']
ㄹ) ['앞']
ㅁ) clear() 전 : ['뒤', '문법', '해운대']
ㅁ) clear() 후 : []
'''
