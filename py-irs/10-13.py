import hgsysinc
from hgchartype import HGGetToken
# 하이브리 글자 타입
string1 = "벙커C유  대책T/F  워싱턴D.C  갤S10  비타민B1  중2  미그21  미그-21 "
string2 = "2000㏄  2000cc  2천CC   80km/h   1/2   16.6g   1/4분기  06/1/18 "
string3 = "D-데이   e-북    CD-롬    K-팝   M&A   CD-ROM  K-POP "
string4 = " S-Oil   H5N1    A1-광구   U.S. "
string_hybrid = string1 + string2 + string3 + string4 

# HGGetToken()
toknum = 0
toklist = HGGetToken(string_hybrid)
for tok in toklist:
    word = tok['string']
    if(word.isspace() == False):
        print(tok['string'], end='\t')
        toknum += 1
print(), print('HGGetToken toknum :', toknum)

'''
처리 결과
=============================================
벙커C유	대책T/F	워싱턴D.C	갤S10	비타민B1	중2	미그21	미그-21	2000㏄	2000cc	2천CC	80km/h	1/2	16.6g	1/4분기	06/1/18	D-데이	e-북	CD-롬	K-팝	M&A	CD-ROM	K-POP	S-Oil	H5N1	A1-광구	U.S.	
HGGetToken toknum : 27

'''

