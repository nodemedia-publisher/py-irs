from sort_base import wordlist101
# 정렬(sort) 처리 예: 
# ㄱ) 길이 순서
wordlist101.sort(key=len)
print('ㄱ)', wordlist101)

# ㄴ) 길이 역순
wordlist101.sort(key=len, reverse=True)
print('ㄴ)', wordlist101)

'''
처리 결과
===========================
ㄱ) ['흙', '값', '조사', '형태', '여덟', '체언', '용언', '다람쥐', '갈매기', '하와이']
ㄴ) ['다람쥐', '갈매기', '하와이', '조사', '형태', '여덟', '체언', '용언', '흙', '값']

'''

