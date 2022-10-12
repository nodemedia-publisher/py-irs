# 텍스트 파일 처리 예:
file = open("text__003.txt") # encoding='utf-8'
try:
    print('cp949):', file.readline())
except UnicodeDecodeError as UDError:
    if("'cp949' codec can't decode" in str(UDError)):
        file.close()
        file = open("text__003.txt", encoding='utf-8')
        print('utf-8):', file.readline())
file.close()


'''
처리 결과
======================
utf-8): 가나다
'''

# text_003.txt 파일은 utf8 로 작성된 문서라서 그냥 읽으면 오류가 발생한다.
# UnicodeDecodeError: 'cp949' codec can't decode byte 0x80 in position 2: illegal multibyte sequence
# 시스템이 PC 윈도 운영체제라서 'cp949' 상태로 처리해서 발생한 것이다.
