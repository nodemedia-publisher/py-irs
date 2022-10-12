import hgsysinc
from hgkbd import HGTransString2EngString
print('한글 음절 -> 영문자:')
print(HGTransString2EngString('듄')) # ebs
print(HGTransString2EngString('ㅏㅠㄴ')) # kbs
print(HGTransString2EngString('햎ㄷ구ㅡ둣')) # 'government' (한영변환 오류)
print(HGTransString2EngString('랲ㄷ구ㅡ둣')) # 'fovernment' <--- 'government' (한영변환 오류 + 철자 오류)
print(HGTransString2EngString('퍛새교')) # 'victory' (한영변환 오류)
print(HGTransString2EngString('챷새교')) # 'cictory'<'victory' (한영변환 오류 + 철자 오류)


"""
출력 결과:
----------------------------------------------
한글 음절 -> 영문자:
ebs
kbs
government
fovernment
victory
cictory



"""

