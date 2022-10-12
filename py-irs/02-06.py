# 문자열(str) 처리 예: 탐색 오류 처리
str31 = "아름다운 대한민국"
try:
    result1 = str31[15] # 범위를 벗어나면 오류 발생
    print (result1) 
except IndexError: #=string index out of range
    result1 = ""
if(result1 == ""):
    print ('string index out of range : str31[15]')



'''
처리 결과:
=================
string index out of range : str31[15]

'''
