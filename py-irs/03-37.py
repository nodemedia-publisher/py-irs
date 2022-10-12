# 집합(set) 처리 예: 빈 집합 생성과 추가
# ㄱ)
hgset11 = set()
print('ㄱ) type(hgset11):', type(hgset11))
hgset11.add('알바트로스')
print('ㄱ) hgset11:', hgset11)

# ㄴ)
hgset12 = {}
print('ㄴ) type(hgset12):', type(hgset12))
hgset12.add('알바트로스')
print('ㄴ) hgset12:', hgset11)
'''
Traceback (most recent call last):
  File "~.py", line 11, in <module>
    hgset12.add('알바트로스')
AttributeError: 'dict' object has no attribute 'add'
'''



'''

처리 결과:
=========================
ㄱ) type(hgset11): <class 'set'>
ㄱ) hgset11: {'알바트로스'}
ㄴ) type(hgset12): <class 'dict'>
Traceback (most recent call last):
  File "~.py", line 11, in <module>
    hgset12.add('알바트로스')
AttributeError: 'dict' object has no attribute 'add'


'''
