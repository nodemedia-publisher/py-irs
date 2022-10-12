# 모듈 호출(import) 예:
import hgsysinc # {mod2.py} 다른 경로에 있기 때문에 경로 지정
import mod2

'''
처리 결과:
==============================
__name__: mod2
외부에서 모듈로 'import'된 상태입니다.
'''

# 모듈에서 '__name__' 변수를 확인하기 위해서 호출하는 예제라서 import 말고는 코드가 없다.
