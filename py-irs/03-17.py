from tuple_base import tuple2
# 튜플(tuple) 처리 예: for loop
print('# ㄱ)')
i = 0
for item in tuple2:
    print( f"[{i}] 번째 항목 : '{item}'")
    i += 1

print('# ㄴ)')
for i, item in enumerate(tuple2):
    print( f"[{i}] 번째 항목 : '{item}'")

print('# ㄷ)')
for i in range(len(tuple2)):
    print( f"[{i}] 번째 항목 : '{tuple2[i]}'")

'''
처리 결과:
=========================
# ㄱ)
[0] 번째 항목 : '앞'
[1] 번째 항목 : '형태소'
[2] 번째 항목 : '콩'
# ㄴ)
[0] 번째 항목 : '앞'
[1] 번째 항목 : '형태소'
[2] 번째 항목 : '콩'
# ㄷ)
[0] 번째 항목 : '앞'
[1] 번째 항목 : '형태소'
[2] 번째 항목 : '콩

'''

