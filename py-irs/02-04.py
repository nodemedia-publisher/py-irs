from string_base import str11, str91

# 문자열(str) 처리 예: 특수 문자(Escape Character)

# 특수문자(Escape Character)
# \"	큰따옴표(Single Quote)
# \'	작은따옴표(Single Quote)
# \\	Backslash	
# \n	새 줄(New Line)
# \r	줄바꿈(Carriage Return)
# \t	탭문자(Tab)

# ㄱ) 
#=str90 = "C:\Users\string.py" # SyntaxError: (unicode error) 'unicodeescape' ~
#=print('ㄱ) str90:', str90)
# ㄴ) 
str90 = "C:\\Users\\string.py"
print('ㄴ) str90:', str90)
# ㄷ)
print('ㄷ1) str11:', str11)
print('ㄷ2) str91:', str91)


"""
처리 결과: (ㄱ, ㄴ 아래에 출력 결과를 두면 실행 오류 때문에 일부 출력 결과를 생략한다.)
==================
ㄴ) ...
ㄷ1) str11: 
안녕하세요.
'파이썬'은 대단한 프로그래밍 언어입니다.
그래서 파이썬을 공부합니다.

ㄷ2) str91: 
안녕하세요.
'파이썬'은 대단한 프로그래밍 언어입니다.
그래서 파이썬을 공부합니다.
"""
