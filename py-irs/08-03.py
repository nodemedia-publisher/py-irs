import hgsysinc
from hgkbd import HGGetSyllable__EngString
#-----------
#-----------
String = 'ｇｋｓｒｎｒ' # 전각(Fullwidth) 아스키: <-- 'gksrnr' <-- {한국}
HGSyllable = HGGetSyllable__EngString(String, FullwidthAsciiTrans=True)
print('입력:', String)
print('한글 음절:', HGSyllable)
print()
String = 'ｚｈｆｌｄｋ' # 전각(Fullwidth) 아스키: <-- 'zhfldk' <-- {코리아}
HGSyllable = HGGetSyllable__EngString(String, FullwidthAsciiTrans=True)
print('입력:', String)
print('한글 음절:', HGSyllable)


"""
출력 결과:
----------------------------------------------
입력: ｇｋｓｒｎｒ
한글 음절: 한국   

입력: ｚｈｆｌｄｋ
한글 음절: 코리아

"""

