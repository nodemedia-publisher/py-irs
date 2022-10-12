from sort_base import wordlist101, revlen
# 정렬(sorted) 처리 예: 사용자 함수, lambda
# ㄱ) # == wordlist101.sort(key=revlen)
#=print(sorted(wordlist101, key=len, reverse=True))
wordlist101_s1 = sorted(wordlist101, key=revlen) 
print('ㄱ)', wordlist101_s1)

# ㄴ) # == wordlist101.sort(key=len, reverse=True)
wordlist101_s2 = sorted(wordlist101, key=lambda wd: -len(wd)) # by len: high -> low
print('ㄴ)', wordlist101_s2)

'''
처리 결과
===========================
ㄱ) ['다람쥐', '갈매기', '하와이', '조사', '형태', '여덟', '체언', '용언', '흙', '값']
ㄴ) ['다람쥐', '갈매기', '하와이', '조사', '형태', '여덟', '체언', '용언', '흙', '값']
'''
 

