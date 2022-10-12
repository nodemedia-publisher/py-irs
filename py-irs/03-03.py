from list_base import hglist1
# 목록(list) 처리 예: 탐색 오류 처리
try:
    result1 = hglist1[15] # 범위를 벗어나면 오류 발생
    print (result1) 
except IndexError: # list index out of range
    result1 = ""
if(result1 == ""):
    print ('Not found : hglist1[15]')




'''
처리 결과:
=========================
Not found : hglist1[15]


'''

