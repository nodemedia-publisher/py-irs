# 텍스트 파일 처리 예:
try:
    file = open('text__000.txt') # 파일이 없는 경우
    print(file.readline())
    file.close()
except FileNotFoundError:
    print("File Not Found: text__000.txt")


'''
처리 결과
======================
File Not Found: text__000.txt
'''
