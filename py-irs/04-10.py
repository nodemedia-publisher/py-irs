from sort_base import wordlist101
# 정렬(sorted) 처리 예: lambda
# ㄱ) #= wordlist101.sort(key=lambda wd: (len(wd), wd)) # by len: low->high, ㄱ->ㅎ
wordlist101_s1 = sorted(wordlist101, key=lambda wd: (len(wd), wd))
print('ㄱ)', wordlist101_s1)


# ㄴ) #= wordlist101.sort(key=lambda wd: (-len(wd), wd)) # by len: high->low, ㄱ->ㅎ
wordlist101_s2 = sorted(wordlist101, key=lambda wd: (-len(wd), wd))
print('ㄴ)', wordlist101_s2)


'''
처리 결과
===========================
ㄱ) ['값', '흙', '여덟', '용언', '조사', '체언', '형태', '갈매기', '다람쥐', '하와이']
ㄴ) ['갈매기', '다람쥐', '하와이', '여덟', '용언', '조사', '체언', '형태', '값', '흙']
'''
