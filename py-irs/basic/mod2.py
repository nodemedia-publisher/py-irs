# module: mod2.py
print('__name__:', __name__)

if __name__ == '__main__':
    print('독립적으로 실행된 상태입니다.')
else:
    print("외부에서 모듈로 'import'된 상태입니다.")

'''
처리 결과:
==============================
__name__: __main__
독립적으로 실행된 상태입니다.
'''