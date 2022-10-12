from sort_base import wordlist101
# 정렬(sorted) 처리 예: 길이 순서
# ㄱ) # == wordlist101.sort(key=len)
wordlist101_s1 = sorted(wordlist101, key=len) 
print('ㄱ)', wordlist101_s1)
# ㄴ) # == wordlist101.sort(key=len, reverse=True)
wordlist101_s2 = sorted(wordlist101, key=len, reverse=True)
print('ㄴ)', wordlist101_s2)

'''
처리 결과
===========================
ㄱ) ['흙', '값', '조사', '형태', '여덟', '체언', '용언', '다람쥐', '갈매기', '하와이']
ㄴ) ['다람쥐', '갈매기', '하와이', '조사', '형태', '여덟', '체언', '용언', '흙', '값']
'''
 

