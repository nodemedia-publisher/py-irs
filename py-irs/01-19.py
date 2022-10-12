# 텍스트 파일 처리 예:
print('ㄱ):')
file = open("text_c_euc-kr.txt")
textlist = file.readlines()
for text in textlist:
    #=print(text)
    print(text, end='')
file.close()

print(), print('ㄴ):')
file = open("text_c_euc-kr.txt")
while True:
    text = file.readline()
    if(text):
        #=print(text)
        print(text, end='')
    else: # 읽은 것이 없으면 파일 끝이므로 종료
        break
file.close()

'''
처리 결과
======================
ㄱ):
한글 맞춤법은 표준어를 소리대로 적는다.
어법에 맞도록 함을 원칙으로 한다.
ㄴ):
한글 맞춤법은 표준어를 소리대로 적는다.
어법에 맞도록 함을 원칙으로 한다.

'''


