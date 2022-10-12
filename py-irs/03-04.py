from list_base import hglist1
# 목록(list) 처리 예: 탐색
# ㄱ)
if '흙' in hglist1: # 목록에 있으면 True, 없으면 False
    print( "'흙' ===> 목록에 있습니다.")
else:
    print( "'흙'===> 목록에 없습니다.")
# ㄴ)
if '황제펭귄' not in hglist1: 
    print( "'황제펭귄'===> 목록에 없습니다.")
else:
    print( "'황제펭귄'===> 목록에 있습니다.")
# ㄷ)
print("'값' count:", hglist1.count('값'))  # 목록에서 '값'의 빈도를 계산
# ㄹ)
print( "'형태' 위치:", hglist1.index('형태'))
# ㅁ)
print( "'황제펭귄' 위치:", hglist1.index('황제펭귄'))

#=# imsi
#=index_res = hglist1.index('황제펭귄') # 이 방식을 써도 프로그램이 중단된다.
#print( "'황제펭귄' 위치:", index_res)

#===
# ㅂ)
#=print( "'형태' 위치:", hglist1.find('형태')) # list()에는 find() 함수 없음.

'''
처리 결과:
=========================
'흙' ===> 목록에 있습니다.
'황제펭귄'===> 목록에 없습니다.
'값' count: 1
'형태' 위치: 3
Traceback (most recent call last):
  File "~.py", line 18, in <module>
    print( "'형태' 위치:", hglist1.index('황제펭귄'))
ValueError: '황제펭귄' is not in list
'''

