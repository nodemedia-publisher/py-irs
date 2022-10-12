# 텍스트 파일 처리 예:
file = open('text__000.txt') # 파일이 없는 경우
print(file.readline())
file.close()


'''
처리 결과
======================
Traceback (most recent call last):
  File "~.py", line 2, in <module>
    file = open('text__000.txt') # 파일이 없는 경우
FileNotFoundError: [Errno 2] No such file or directory: 'text__000.txt'
'''
