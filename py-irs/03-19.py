from dict_base import 한글사전
# 사전(dict) 처리 예: 길이와 탐색
# ㄱ)
print("ㄱ) 사전(dict) 개수:", len(한글사전))
# ㄴ)
print("ㄴ) 사전(dict) '표제어':", 한글사전['표제어']) # 사전(dict)에서 '키:값' 조회
# ㄷ)
print("ㄷ) 사전(dict) '품사':", 한글사전.get('품사')) # 사전(dict)에서 '키:값' 조회
# ㄹ)
print("ㄹ) 사전(dict) '빈도':", 한글사전.get('빈도')) # dict에 없는 키('빈도') 조회하면 'None'
# ㅁ)
print("ㅁ) 사전(dict) '빈도':", 한글사전['빈도']) # dict에 없는 키('빈도') 조회하면 오류 발생
'''
===> 오류 발생
Traceback (most recent call last):
  File "~.py", line 12, in <module>
    print("ㅁ) 사전(dict) '빈도':", 한글사전['빈도']) # dict에 없는 키('빈도') 조회하면 오류 발생
KeyError: '빈도'
'''


'''
처리 결과:
=========================
ㄱ) 사전(dict) 개수: 3
ㄴ) 사전(dict) '표제어': 흙
ㄷ) 사전(dict) '품사': 명사
ㄹ) 사전(dict) '빈도': None
Traceback (most recent call last):
  File "~.py", line 12, in <module>
    print("ㅁ) 사전(dict) '빈도':", 한글사전['빈도']) # dict에 없는 키('빈도') 조회하면 오류 발생
KeyError: '빈도'
>>> 


'''

