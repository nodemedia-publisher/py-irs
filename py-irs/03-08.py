# 목록(list) 처리 예: 범위 삭제
# ㄱ)
from list_base import hglist1
del hglist1[1:3] # 목록에서 지정한 index 범위의 항목을 삭제함.
print('ㄱ)', hglist1)

# ㄴ)
from list_base import hglist2
del hglist2[2:15] # 목록에서 지정한 index 범위 초과 삭제.
print('ㄴ)', hglist2)

# ㄷ)
from list_base import hglist3
del hglist3[-10:2] # 목록에서 지정한 index 범위 초과 삭제.
print('ㄷ)', hglist3)

# ㄹ)
from list_base import hglist101
del hglist101[::3] # '3' 간격으로 
print('ㄹ)', hglist101)

# ㅁ)
from list_base import hglist102
del hglist102[::-4] # 뒤에서 부터 '-4' 간격으로
print('ㅁ)', hglist102)

# ㅂ)
del hglist102[:] # 목록 전체를 삭제함.
print('ㅂ)', hglist102)


'''
처리 결과:
=========================
ㄱ) ['조사', '형태', '여덟', '체언']
ㄴ) ['앞', '형태소']
ㄷ) ['해운대']
ㄹ) ['하나', '둘', '넷', '다섯', '일곱', '여덟']
ㅁ) ['一', '三', '四', '五', '七', '八', '九']  
ㅂ) []

'''
