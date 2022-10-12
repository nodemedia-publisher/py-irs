from sort_base import wordlist101
# 정렬(sorted) 처리 예: 사전 순서
# ㄱ) # == wordlist101.sort()
wordlist101_s1 = sorted(wordlist101) 
print('ㄱ)', wordlist101_s1)
# ㄴ) # == wordlist101.sort(reverse=True)
wordlist101_s2 = sorted(wordlist101, reverse=True)
print('ㄴ)', wordlist101_s2)

'''
처리 결과
===========================
ㄱ) ['갈매기', '값', '다람쥐', '여덟', '용언', '조사', '체언', '형태', '하와이', '흙']
ㄴ) ['흙', '하와이', '형태', '체언', '조사', '용언', '여덟', '다람쥐', '값', '갈매기']

'''
 

