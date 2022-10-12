# 텍스트 파일 처리 예:
# ㄱ)
file = open("text__001.txt")
print('ㄱ):', file.read())
print('ㄱ):', file.closed) # 파일이 닫혀 있나? No
#=file.close()

# ㄴ)
with open('text__001.txt') as file:
    print('ㄴ):', file.read())
print('ㄴ):', file.closed) # 파일이 닫혀 있나? Yes


'''
처리 결과
======================
ㄱ): 123
ㄱ): False
ㄴ): 123
ㄴ): True

'''
