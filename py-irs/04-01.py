from sort_base import wordlist101
# 정렬(sort) 처리 예: 
# ㄱ) 사전 순서
wordlist101.sort()
print('ㄱ):', wordlist101)

# ㄴ) 사전 역순
wordlist101.sort(reverse=True)
print('ㄴ):', wordlist101)

'''
처리 결과
===========================
ㄱ): ['갈매기', '값', '다람쥐', '여덟', '용언', '조사', '체언', '형태', '하와이', '흙']
ㄴ): ['흙', '하와이', '형태', '체언', '조사', '용언', '여덟', '다람쥐', '값', '갈매기']

'''


