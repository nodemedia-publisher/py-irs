import re
str3 = '3.1운동  3·1운동   한·일'
str4 = '14-year-old'
str5 = 'K-POP K-팝'
str6 = 'apple애플ａｐｐｌｅㅁㅔㅔㅣㄷAPPLEﾱￇￇￜﾧＡＰＰＬＥ'
str7 = '사과沙果ᄉᆞ과'

print(re.findall("[\w]+", str3))
print(re.findall("[\w]+", str4))
print(re.findall("[\w]+", str5))
print(re.findall("[\w]+", str6))
print(re.findall("[\w]+", str7))

"""
처리 결과:
================================
['3', '1운동', '3', '1운동', '한', '일']
['14', 'year', 'old']
['K', 'POP', 'K', '팝']
['apple애플ａｐｐｌｅㅁㅔㅔㅣㄷAPPLEﾱￇￇￜﾧＡＰＰＬＥ']
['사과沙果ᄉᆞ과']
"""

