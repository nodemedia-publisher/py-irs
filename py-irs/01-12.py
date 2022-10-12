# 텍스트 파일 처리 예:
import pathlib
if pathlib.Path('text__000.txt').is_file():
    file = open('text__000.txt')
    print(file.readline())
    file.close()
else:
    print("File Not Found: text__000.txt")


'''
처리 결과
======================
File Not Found: text__000.txt
'''
