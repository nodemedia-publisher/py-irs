# 텍스트 파일 처리 예:
file = open("text__002.txt", encoding='utf-8')
try:
    print('utf-8):', file.readline())
except UnicodeDecodeError as UDError:
    if("'utf-8' codec can't decode" in str(UDError)):
        file.close()
        file = open("text__002.txt", encoding='cp949')
        print('cp949):', file.readline())
file.close()

'''
처리 결과
======================
cp949): 가나다
'''

# text_002.txt 파일은 cp949 로 작성된 문서라서 utf8로 읽으면 오류가 발생한다.
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb0 in position 0: invalid start byte
