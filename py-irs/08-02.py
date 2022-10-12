import hgsysinc
from hgkbd import HGGetSyllable__EngString
#-----------
#-----------
EngString = 'gksrnr'  # 한글 자모: ㅎㅏㄴㄱㅜㄱ <==> '한국'
HGSyllable = HGGetSyllable__EngString(EngString)
print('영문자:', EngString)
print('한글 음절:', HGSyllable)
print()

EngString = 'rsef'  # 한글 자모: ㄱㄴㄷㄹ <==> ㄱㄴㄷㄹ
HGSyllable = HGGetSyllable__EngString(EngString)
print('영문자:', EngString)
print('한글 음절:', HGSyllable)
print()


"""
출력 결과:


#==============================

영문자: gksrnr
한글 음절: 한국

영문자: rsef
한글 음절: ㄱㄴㄷㄹ


"""
