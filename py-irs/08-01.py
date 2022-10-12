import hgsysinc
from hgkbd import Eng2JaumMoum_Simple
#----------
#----------
EngString = 'gksrnr'  # 한글 자모: ㅎㅏㄴㄱㅜㄱ <==> '한국'
HngKBDCharString = Eng2JaumMoum_Simple(EngString)
print('영문자:', EngString)
print('한글 자모:', HngKBDCharString)



"""
출력 결과:
#==============================
영문자: gksrnr
한글 자모: ㅎㅏㄴㄱㅜㄱ

"""

