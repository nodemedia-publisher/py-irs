from string_base import str31, str33

# 문자열(str) 처리 예: join

# ㄱ)
joinChar = ' ' # 공백 문자
koreaList = ['대한민국', '코리아', '한국', 'KOREA', '韓國']
str_j1 = joinChar.join(koreaList)
print('ㄱ) :', str_j1)

# ㄴ)
joinChar = '='
koreaTuple = '대한민국', '코리아', '한국', 'KOREA', '韓國'
str_j2 = joinChar.join(koreaTuple)
print('ㄴ) :', str_j2)

# ㄷ)
joinChar = '>'
set1 = {'국어', '영어', '수학', '과학'}
str_j3 = joinChar.join(set1)
print('ㄷ) :', str_j3)

# ㄹ)
joinChar = ','
str_j4 = joinChar.join('아름다운')
print(f'ㄹ) :', str_j4)



'''
처리 결과:
==============================
ㄱ) : 대한민국 코리아 한국 KOREA 韓國
ㄴ) : 대한민국=코리아=한국=KOREA=韓國
ㄷ) : 수학>국어>영어>과학
ㄹ) : 아,름,다,운

'''

