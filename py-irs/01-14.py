# 텍스트 파일 처리 예:
print('ㄱ):')
file = open("text__003.txt", encoding='utf-8')
print(file.readline())
file.close()

print("ㄴ): [text__002.txt ==> encoding='euc-kr']")
file = open("text__002.txt", encoding='utf-8')
print(file.readline())
file.close()

'''
처리 결과
======================
ㄱ):
가나다
ㄴ): [text__002.txt ==> encoding='euc-kr']
Traceback (most recent call last):
  File "~.py", line 9, in <module>
    print(file.readline())
  File "Python\Python38\lib\codecs.py", line 322, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
'''
