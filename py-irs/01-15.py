# 텍스트 파일 처리 예:
file = open("text_30_cp949.txt", encoding='euckr')
print(file.readline())
file.close()

#=file = open("text_30_euc-kr.txt", encoding='euckr')
#=print(file.readline())
#=file.close()

'''
처리 결과
======================
Traceback (most recent call last):
  File "~.py", line 3, in <module>
    print(file.readline())
UnicodeDecodeError: 'euc_kr' codec can't decode byte 0x98 in position 0: illegal multibyte sequence

'''


