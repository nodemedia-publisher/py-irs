from string_base import str30
# 문자열(str) 처리 예:for loop
print('# ㄱ)')
i = 0
for char_cur in str30:
    print(f'[{i}] 번째 글자:', char_cur)
    i += 1

print('# ㄴ)')
for i, char_cur in enumerate(str30):
    print(f'[{i}] 번째 글자:', char_cur)

print('# ㄷ)')
for i in range(len(str30)):
    print(f'[{i}] 번째 글자:', str30[i])

print('# ㄹ)')
for i in range(len(str30)-1, -1, -1):
    print(f'[{i}] 번째 글자:', str30[i])

'''
처리 결과:
==============================
# ㄱ)
[0] 번째 글자: 대
[1] 번째 글자: 한
[2] 번째 글자: 민
[3] 번째 글자: 국
# ㄴ)
[0] 번째 글자: 대
[1] 번째 글자: 한
[2] 번째 글자: 민
[3] 번째 글자: 국
# ㄷ)
[0] 번째 글자: 대
[1] 번째 글자: 한
[2] 번째 글자: 민
[3] 번째 글자: 국
# ㄹ)
[3] 번째 글자: 국
[2] 번째 글자: 민
[1] 번째 글자: 한
[0] 번째 글자: 대

'''
