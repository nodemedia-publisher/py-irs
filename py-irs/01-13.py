# 텍스트 파일 처리 예:
file = open('text__003.txt') # [text__003.txt ==> encoding='utf-8']
print(file.readline())
file.close()

# UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 2: illegal multibyte sequence
# 시스템이 PC 윈도 운영체제라서 'cp949' 상태로 처리해서 발생한 것이다.
# text_003.txt 파일은 utf8 로 작성된 문서이다.

'''
처리 결과
======================
Traceback (most recent call last):
  File "~.py", line 3, in <module>
    print(file.readline())
UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 2: illegal multibyte sequence
'''

