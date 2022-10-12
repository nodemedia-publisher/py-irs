import hgsysinc
from hgkbd import HGGetSyllable_JaumMoumString
#---
#----------
#=JaumMoumString = 'ㅎㅏㄴ'
#=JaumMoumString = 'ㅗㅏㄴㄱㅡㄹ'
#=JaumMoumString = 'ㅗㅏㄱㅡㄹ'
#=JaumMoumString = 'ㄹㄱ'
#=JaumMoumString = 'ㄹㄱㅏ'
#=JaumMoumString = 'ㄺㅏ'
JaumMoumString = 'ㅎㅏㄴㄱㅡㄹ' # <== {한글}
HGSyllable = HGGetSyllable_JaumMoumString(JaumMoumString)
print('두벌식 자모:', JaumMoumString)
print('한글 음절:', HGSyllable)



"""
처리 결과:
#=================================================
두벌식 자모: ㅎㅏㄴㄱㅡㄹ
한글 음절: 한글

"""
