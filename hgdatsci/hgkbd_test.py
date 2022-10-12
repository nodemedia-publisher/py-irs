#---
#---
import hgsysinc # 이 파일에서는 사용하지 않더라도 이 파일을 부르는 곳에서 사용한다.

#---
#---
from hgbasic import hexUpper

##----------
##----------
def Hng2Jamo_511(string, debugPrint=False):
    from hgkbd import HGTransString2KBDJamo
    if(debugPrint == True):
        hgsysinc._print_function_name_()
    #
    JaumMoumString = HGTransString2KBDJamo(string)
    print(string, ':', JaumMoumString)

    if(debugPrint == True):
        # 편집 코드
        caption = ['순서', '두벌식 자모', '16진수',]
        print(*caption, sep='\t')
        for i, HngKBDChar in enumerate(JaumMoumString):
            print(f'{i}\t{HngKBDChar}\t{hexUpper(ord(HngKBDChar), add_0x=True)}')
    #
    return JaumMoumString

def Hng2Jamo_512(string):
    from hgunicode import hgGetChoJungJongString, hgGetChoJungJongInx, hgGetSyllable_inx
    from 자모 import 자모열_채움문자보충_음절변환
    hgsysinc._print_function_name_()
    
    #
    ChoJungJongInx = hgGetChoJungJongInx(string)
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    print(ChoJungJongInx)
    print()

    print('# 편집 코드 - 자모를 그대로 출력해서 화면에 밀릴 수 있음')
    ChoJungJongString = hgGetChoJungJongString(string)
    caption = ['순서', '초중종 자모', '16진수',]
    print(*caption, sep='\t')
    for i, JamoChar in enumerate(ChoJungJongString):
        print(f'{i}\t{JamoChar}\t{hexUpper(ord(JamoChar), add_0x=True)}')
    print()

    print('# 편집 코드: 음절 인덱스 출력')
    caption = ['순서', '글자', '16진수', '음절 인덱스']
    for i, hgchar in enumerate(string):
        syllable_inx = hgGetSyllable_inx(hgchar)
        print(f'{i}\t{hgchar}\t{hexUpper(ord(hgchar), add_0x=True)}\t{syllable_inx}')
    print()

    print('# 편집 코드 - 자모를 채움문자로 채워서 밀리지 않도록 한 것')
    ChoJungJongString = hgGetChoJungJongString(string)
    caption = ['순서', '초중종 자모', '16진수',]
    print(*caption, sep='\t')
    for i, JamoChar in enumerate(ChoJungJongString):
        자모열_채움문자보충 = 자모열_채움문자보충_음절변환(JamoChar)
        print(f'{i}\t{자모열_채움문자보충}\t{hexUpper(ord(JamoChar), add_0x=True)}')
    print()

    # 편집을 위한 출력
    print('# 화면에서 밀리는 자모를 채움문자를 채워서 밀리지 않는 버전 출력')
    for JamoChar in ChoJungJongString:
        자모열_채움문자보충 = 자모열_채움문자보충_음절변환(JamoChar)
        print(자모열_채움문자보충)
    print()

    # 편집을 위한 출력
    자모열_채움문자보충 = 자모열_채움문자보충_음절변환(ChoJungJongString)
    print(자모열_채움문자보충)
    print()
    
    print('# 편집 코드')
    caption = ['순서', '음절', '16진수',]
    print(*caption, sep='\t')
    for i, Char in enumerate(string):
        print(f'{i}\t{Char}\t{hexUpper(ord(Char), add_0x=True)}')
    print()

    print(), print(), 

def Hng2Jamo_521(JaumMoumString, debugPrint=False):
    from hgkbd import HGGetSyllable_JaumMoumString
    if(debugPrint == True):
        hgsysinc._print_function_name_()
    ##----------
    ##----------
    #=JaumMoumString = 'ㅎㅏㄴㄱㅡㄹ' # <== {한글}
    #=JaumMoumString = 'ㅎㅏㄴ'
    #=JaumMoumString = 'ㅗㅏㄴㄱㅡㄹ'
    #=JaumMoumString = 'ㅗㅏㄱㅡㄹ'
    HGSyllable = HGGetSyllable_JaumMoumString(JaumMoumString)
    print(JaumMoumString, ':', HGSyllable)
    return HGSyllable

def Hng2Eng_411(string, debugPrint=False):
    from hgkbd import HGTransString2EngString
    if(debugPrint == True):
        import hgsysinc
        hgsysinc._print_function_name_()
    #
    EngString = HGTransString2EngString(string) # 한영변환
    print(string, ':', EngString)

    if(debugPrint == True):
        # 편집 코드
        caption = ['순서', '영문자', '16진수',]
        print(*caption, sep='\t')
        for i, EngChar in enumerate(EngString):
            print(f'{i}\t{EngChar}\t{hexUpper(ord(EngChar), add_0x=True)}')
    #
    return EngString

def Hng2Eng_412(string, debugPrint=False):
    from hgunicode import hgGetChoJungJongString, hgGetChoJungJongInx
    from 자모 import 자모열_채움문자보충_음절변환
    from hgkbd import HGTransString2EngString
    #    
    if(debugPrint == True):
        import hgsysinc
        hgsysinc._print_function_name_()
    #
    EngString = HGTransString2EngString(string)
    print(string, ':', EngString)
    print()
    #
    ChoJungJongInx = hgGetChoJungJongInx(string)
    # 형식 : {'cho': chosung_inx, 'jung': jungsung_inx, 'jong':jongsung_inx}
    print(ChoJungJongInx)
    print()


    print('# 편집 코드 - 자모를 그대로 출력해서 화면에 밀릴 수 있음')
    ChoJungJongString = hgGetChoJungJongString(string)
    caption = ['순서', '초중종 자모', '16진수','영문자', '16진수',]
    print(*caption, sep='\t')
    for i, JamoChar in enumerate(ChoJungJongString):
        print(f'{i}\t{JamoChar}\t{hexUpper(ord(JamoChar), add_0x=True)}', end='')
        #        
        EngChar = EngString[i]
        print(f'\t{EngChar}\t{hexUpper(ord(EngChar), add_0x=True)}', end='')
        
        print()
    print()

    print('# 편집 코드 - 자모를 채움문자로 채워서 밀리지 않도록 한 것')
    ChoJungJongString = hgGetChoJungJongString(string)
    print(*caption, sep='\t')
    for i, JamoChar in enumerate(ChoJungJongString):
        자모열_채움문자보충 = 자모열_채움문자보충_음절변환(JamoChar)
        print(f'{i}\t{자모열_채움문자보충}\t{hexUpper(ord(JamoChar), add_0x=True)}', end='')
        #        
        EngChar = EngString[i]
        print(f'\t{EngChar}\t{hexUpper(ord(EngChar), add_0x=True)}', end='')
        
        print()
    print()

    # 편집을 위한 출력
    print('# 화면에서 밀리는 자모를 채움문자를 채워서 밀리지 않는 버전 출력')
    for JamoChar in ChoJungJongString:
        자모열_채움문자보충 = 자모열_채움문자보충_음절변환(JamoChar)
        print(자모열_채움문자보충)
    print()

    # 편집을 위한 출력
    자모열_채움문자보충 = 자모열_채움문자보충_음절변환(ChoJungJongString)
    print(자모열_채움문자보충)
    print()
    
    print('# 편집 코드')
    caption = ['순서', '음절', '16진수',]
    print(*caption, sep='\t')
    for i, Char in enumerate(string):
        print(f'{i}\t{Char}\t{hexUpper(ord(Char), add_0x=True)}')
    print()

    print(), print(), 

def Hng2Eng_421(EngString, debugPrint=False):
    from hgkbd import HGGetJaumMoum__EngString, HGGetSyllable_JaumMoumString
   
    if(debugPrint == True):
        hgsysinc._print_function_name_()
    ##----------
    ##----------
    #=EngString = '듄' # <== {ebs}
    #=EngString = 'ㅏㅠㄴ'  # <== {kbs}
    JaumMoumString = HGGetJaumMoum__EngString(EngString) # 영문 자모 변환
    HGSyllable = HGGetSyllable_JaumMoumString(JaumMoumString) # 자모 음절 변환
    print(EngString, ' ==> ', JaumMoumString, ' ==> ', HGSyllable)
    return HGSyllable

def String2KBDJamo_711(String, debugPrint=False):
    """
    반각 자모가 포함된 경우 두벌식 자모로 변환
    초중종 자모가 포함된 경우 두벌식 자모로 변환
    """
    from hgkbd import HGTransString2KBDJamo, HGGetSyllable_JaumMoumString
    if(debugPrint == True):
        hgsysinc._print_function_name_()
    #
    #=String = 'ﾡￂﾸￂﾱￜ' # 반각(Halfwidth) 자모: <-- 'ㄱㅏㅈㅏㅁㅣ' <-- {가자미}
    #=String = '가자미' # 초중종 자모(Hangul Jamo) 자모: <-- 6글자 길이의 문자열
    KBDString = HGTransString2KBDJamo(String)
    HGSyllable = HGGetSyllable_JaumMoumString(KBDString)
    print(f'입력 ({len(String)}):', String)
    print(f'두벌식 자모 문자열 ({len(KBDString)}):', KBDString)
    print(f'음절 문자열 ({len(HGSyllable)}):', HGSyllable)
    #
    return KBDString, HGSyllable # 두벌식(키보드) 자모, 음절

def StringEng_721(String, debugPrint=False):
    """
    반각 자모가 포함된 경우 영문자로 변환
    """
    from hgkbd import HGTransString2EngString, HGGetJaumMoum__EngString
    if(debugPrint == True):
        hgsysinc._print_function_name_()
    #
    #=String = 'ﾡￂﾸￂﾱￜ' # 반각(Halfwidth) 자모: <-- 'ㄱㅏㅈㅏㅁㅣ' <-- {가자미}
    EngString = HGTransString2EngString(String)
    KBDString = HGGetJaumMoum__EngString(EngString)
    print(f'입력 ({len(String)}):', String)
    print(f'영문자 문자열 ({len(EngString)}):', EngString)
    print(f'두벌식 자모 문자열 ({len(KBDString)}):', KBDString)
    #
    return EngString, KBDString # 영문자, 두벌식(키보드) 자모

#================================
#================================
#================================
from unittest import TestCase, main

class HGTest(TestCase):
    def test_12(self):
        print('테스트')

if __name__ == '__main__':
    #=main()
    pass

