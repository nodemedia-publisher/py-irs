import hgsysinc
from hgkbd import HGTransString2EngString
#----------
#----------
String = '듄'  # '듄' <==> 'ebs'
EngString = HGTransString2EngString(String)
print('한글:', String)
print('영문자:', EngString)
print()

#=String = 'ㅏㅠㄴ'  # 'ㅏㅠㄴ' <==> 'kbs'
#=EngString = HGTransString2EngString(String)
#=print('입력:', String)
#=print('영문자:', EngString)
#=print()

String = 'ㅏㅐㄱㄷㅁ'  # 'ㅏㅐㄱㄷㅁ' <==> 'korea'
EngString = HGTransString2EngString(String)
print('한글:', String)
print('영문자:', EngString)
print()

String = 'ㅙㅜ됴'  # 'ㅙㅜ됴' <==> 'honey'
EngString = HGTransString2EngString(String)
print('한글:', String)
print('영문자:', EngString)
print()


"""
출력 결과:
----------------------------------------------
한글: 듄
영문자: ebs

한글: ㅏㅐㄱㄷㅁ
영문자: korea

한글: ㅙㅜ됴
영문자: honey

"""

