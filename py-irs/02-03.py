# 문자열(str) 처리 예: 특수 문자(Escape Character)로 생성
# ㄱ) 15초를 기호로 표시할 때
str1 = "[15초: 15"]" # ===> unmatched ']' <=== invalid syntax
print('ㄱ) str1:', str1)

# ㄴ) 
str2 = "[15초: 15\"]"
print('ㄴ) str2:', str2)

# ㄷ) 
str3 = '[15초: 15"]'
print('ㄷ) str3:', str3)


'''
처리 결과:
==================
#=str1 = "[15초: 15"]" # ===> unmatched ']' <=== invalid syntax

ㄴ) str2: [15초: 15"]
ㄷ) str3: [15초: 15"]
'''



