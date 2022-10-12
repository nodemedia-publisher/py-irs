# 모듈 호출(import) 예:
import hgsysinc # {인사.py} 다른 경로에 있기 때문에 경로 지정
from 인사 import 한국, 중국어인사

print('# ㄱ)')
한국()
print(중국어인사)

print('# ㄴ)')
인사.한국()
print(인사.중국어인사)

'''
처리 결과
======================
# ㄱ)
안녕하세요.
你好.
# ㄴ)
Traceback (most recent call last):
  File "~.py", line 10, in <module>
    인사.한국()
NameError: name '인사' is not defined
'''
