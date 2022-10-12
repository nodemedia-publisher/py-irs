from sort_base import wordlist101
# 정렬(sort) 처리 예: lambda
# ㄱ)
wordlist101.sort(key=lambda wd: (len(wd), wd)) # by len: low->high, ㄱ->ㅎ
print('ㄱ) :', wordlist101)


# ㄴ)
wordlist101.sort(key=lambda wd: (-len(wd), wd)) # by len: high->low, ㄱ->ㅎ
print('ㄴ) :', wordlist101)


'''
처리 결과
===========================
ㄱ) : ['값', '흙', '여덟', '용언', '조사', '체언', '형태', '갈매기', '다람쥐', '하와이']
ㄴ) : ['갈매기', '다람쥐', '하와이', '여덟', '용언', '조사', '체언', '형태', '값', '흙']

'''
