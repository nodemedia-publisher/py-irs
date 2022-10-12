from dict_base import 한글사전
# 사전(dict) 처리 예: 삭제
# ㄱ)
delitem = 한글사전.popitem() # 사전에서 맨 마지막 항목을 삭제함.
print('ㄱ) delitem:', delitem)
print('ㄱ)', 한글사전)


'''
처리 결과:
=========================
>>> 

ㄱ) delitem: ('등록자', '세종대왕')
ㄱ) {'표제어': '흙', '품사': '명사'}
'''
