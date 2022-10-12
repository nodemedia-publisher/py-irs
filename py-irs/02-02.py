# 문자열(str) 처리 예: 특수 문자(Escape Character)로 생성
# ㄱ) 
str1 = 'let's go' # ===> invalid syntax
print('ㄱ) str1:', str1)

# ㄴ) 
str2 = 'let\'s go'
print('ㄴ) str2:', str2)

# ㄷ) 
str3 = "let's go"
print('ㄷ) str3:', str3)



'''
처리 결과:
=============================
str1 = 'let's go' # ===> invalid syntax

ㄴ) str2: let's go
ㄷ) str3: let's go

'''


