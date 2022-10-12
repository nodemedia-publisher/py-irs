from set_base import hgset1
# 집합(set) 처리 예: 삭제 오류 처리
#----------
# ㄱ)
hgset1.remove('독수리') # 집합에 없는 항목 삭제
'''
처리 결과:
=========================
Traceback (most recent call last):
  File "~.py", line 5, in <module>
    hgset1.remove('독수리') # 집합에 없는 항목 삭제
KeyError: '독수리'
'''
#----------
# ㄴ)
try:
    hgset1.remove('독수리') # 집합에 없는 항목 삭제
    print( "ㄴ) '독수리' 삭제: 성공")
except KeyError: # '독수리'
    print( "ㄴ) '독수리' 삭제: 실패")
print('ㄴ)', hgset1)

#----------
# ㄷ)
print('ㄷ) 삭제 전:', hgset1)
hgset1.discard('독수리')
print('ㄷ) 삭제 후:', hgset1)


'''

처리 결과:
=========================
'독수리' 삭제: 실패
ㄴ) {'닭', '까치', '오리', '참새', '비둘기'}
ㄷ) 삭제 전: {'까치', '닭', '참새', '비둘기', '오리'}
ㄷ) 삭제 후: {'까치', '닭', '참새', '비둘기', '오리'}

'''



