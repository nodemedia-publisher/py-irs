# 모듈 호출(import) 예:
#=from basic import 인사
import hgsysinc # {인사.py} 다른 경로에 있기 때문에 경로 지정
import 인사

print('# ㄱ)')
인사.한국()
인사.미국()
인사.中國()

print('# ㄴ)')
print(인사.영어인사)
print(인사.중국어인사)

'''
처리 결과
======================
# ㄱ)
안녕하세요.
hello.     
你好.      
# ㄴ)      
hello.     
你好. 

'''
