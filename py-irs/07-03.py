import hgsysinc
from hgkbd import HGTransString2KBDJamo
#----------
# '한글 음절 -> 한글 두벌식(키보드) 자모:'
#=string = '한'
string = '뷁'
KBDCharString = HGTransString2KBDJamo(string)
print('입력 문자열:', string)
print('한글 두벌식 자모:', KBDCharString)

string = 'ㄺㅅ'
KBDCharString = HGTransString2KBDJamo(string)
print('입력 문자열:', string)
print('한글 두벌식 자모:', KBDCharString)

string = 'ㅞa1'
KBDCharString = HGTransString2KBDJamo(string)
print('입력 문자열:', string)
print('한글 두벌식 자모:', KBDCharString)

'''
출력 결과:
----------------------------------------------
한글 음절: 뷁
한글 두벌식 자모: ㅂㅜㅔㄹㄱ
한글 음절: ㄺㅅ
한글 두벌식 자모: ㄹㄱㅅ    
한글 음절: ㅞa1
한글 두벌식 자모: ㅜㅔa1    

'''
