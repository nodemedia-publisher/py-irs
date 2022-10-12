# 텍스트 파일 처리 예:
print('ㄱ): 한꺼번에 모두 읽기')
file = open("text_c_euc-kr.txt")
text = file.read()
print(text)
print('text 길이:', len(text))
file.close()

print(), print('ㄴ): 1글자씩 모두 읽기')
file = open("text_c_euc-kr.txt")
text = ''
while True:
    char = file.read(1)
    if(char):
        text += char
    else:
        break
print(text)
print('text 길이:', len(text))
file.close()

'''
처리 결과
======================
ㄱ): 한꺼번에 모두 읽기
한글 맞춤법은 표준어를 소리대로 적는다.
어법에 맞도록 함을 원칙으로 한다.

ㄴ): 1글자씩 모두 읽기
한글 맞춤법은 표준어를 소리대로 적는다.
어법에 맞도록 함을 원칙으로 한다.
text 길이: 42

'''

