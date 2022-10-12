from dict_base import us_speech
print('@@@ 편집 코드 : us_speech = ', us_speech) # 편집 코드
# 사전(dict) 처리 예: dict.values()
print('# ㄱ)')
i = 0
sum = 0
for value in us_speech.values():
    print(f"[{i}] : {value}")
    sum += value
    i += 1
print('sum:', sum)
print()

print('# ㄴ)')
sum = 0
for i, value in enumerate(us_speech.values()):
    print(f"[{i}] : {value}")
    sum += value
print('sum:', sum)
print()



'''

처리 결과:

================
@@@ 편집 코드 : us_speech = {'govern': 19, 'governed': 10, 'governing': 6, 'government': 620, "government's": 6, 'governmental': 10, 'governments': 50, 'governs': 1}
# ㄱ)
[0] : 19
[1] : 10
[2] : 6
[3] : 620
[4] : 6
[5] : 10
[6] : 50
[7] : 1
sum: 722

# ㄴ)
[0] : 19
[1] : 10
[2] : 6
[3] : 620
[4] : 6
[5] : 10
[6] : 50
[7] : 1
sum: 722
'''

