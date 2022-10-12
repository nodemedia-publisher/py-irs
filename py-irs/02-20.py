from string_base import str61, str92

# 문자열(str) 처리 예: split

# ㄱ)
str92_list = str92.split('=')
print(f'ㄱ) {len(str92_list)}:', str92_list)

# ㄴ)
str61_list = str61.split()
print(f'ㄴ) {len(str61_list)}:', str61_list)






'''
처리 결과:
==============================
ㄱ) 5: ['대한민국', '코리아', '한국', 'KOREA', '韓國']
ㄴ) 7: ['문장의', '각', '단어는', '띄어', '씀을', '원칙으로', '한다']

'''

