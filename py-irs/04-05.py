from sort_base import wordlist101
# 정렬(sort) 처리 예: lambda
wordlist101.sort(key=lambda wd: -len(wd)) # by len: high -> low
print(wordlist101)

'''
처리 결과
===========================
['다람쥐', '갈매기', '하와이', '조사', '형태', '여덟', '체언', '용언', '흙', '값']

'''
