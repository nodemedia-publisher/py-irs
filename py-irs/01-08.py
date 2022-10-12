# 실행 시간 측정 예: unittest.TestCase
from unittest import TestCase, main
class HGTest(TestCase):
    def test_1(self):
        import hgsysinc # {인사.py} 다른 경로에 있기 때문에 경로 지정
        import 인사

        인사.한국()
        인사.미국()
        print(인사.중국어인사)

main()
#=if __name__ == '__main__':
#=    main()

'''
처리 결과:
==============================
안녕하세요.
hello.
你好.
----------------------------------------------------------------------
Ran 1 test in 0.004s
'''
