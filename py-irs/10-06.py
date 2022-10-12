str1 = '서울 abc'
str2 = '서울(seoul)'

print(str1.split())
print(str2.split())

import re
print(re.findall("[\w]+", str2))
print()


"""
처리 결과:
================================
['서울', 'abc']
['서울(seoul)']
['서울', 'seoul']

"""

