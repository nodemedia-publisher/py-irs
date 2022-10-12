from list_base import hglist2
# 목록(list) 처리 예: for loop
print('# ㄱ)')
i = 0
for item in hglist2:
    print( f"[{i}] 번째 항목 : '{item}'")
    i += 1
print()

print('# ㄴ)')
for i, item in enumerate(hglist2):
    print( f"[{i}] 번째 항목 : '{item}'")
print()

print('# ㄷ)')
for i in range(len(hglist2)):
    item = hglist2[i]
    print( f"[{i}] 번째 항목 : '{item}'")
print()



'''
처리 결과:
================
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
[2] 번째 항목 : '콩'

'''

