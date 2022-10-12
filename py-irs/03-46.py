from set_base import hgset3
# 집합(set) 처리 예: for loop
print('# ㄱ)')
i = 0
for item in hgset3:
    print( f'[{i}] 번째 항목 :', item)
    i += 1

print('# ㄴ)')
for i, item in enumerate(hgset3):
    print( f'[{i}] 번째 항목 :', item)

print('# ㄷ)')
num = len(hgset3)
for i in range(num):
    print( f'[{i}] 번째 항목 :', hgset3[i])



'''

처리 결과:
================
# ㄱ)
[0] 번째 항목 : 곰
[1] 번째 항목 : 호랑이
[2] 번째 항목 : 늑대
# ㄴ)
[0] 번째 항목 : 곰
[1] 번째 항목 : 호랑이
[2] 번째 항목 : 늑대
# ㄷ1)
Traceback (most recent call last):
  File "~.py", line 16, in <module>
    print( f'[{i}] 번째 항목 :', hgset3[i])
TypeError: 'set' object is not subscriptable


'''

