import re
# 하이브리 글자 타입 : cnn news 20200114
str61 = '14-year-old'
str62 = 'out-performed'
str63 = 'commander-in-chief'
str64 = 'U.S.'

print(re.findall("[\w]+", str61))
print(re.findall("[\w]+", str62))
print(re.findall("[\w]+", str63))
print(re.findall("[\w]+", str64))

'''
처리 결과:
===============================
['14', 'year', 'old']
['out', 'performed']        
['commander', 'in', 'chief']
['U', 'S']

'''
