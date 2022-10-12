import hgsysinc
from hgkbd import HGGetSyllable__EngString
#----------
#----------
print('#. 영문자 -> 한글 음절:')
print(HGGetSyllable__EngString('gksrnr'))  # 한국
print(HGGetSyllable__EngString('fksrnr'))  # 란국 --> 한국
print(HGGetSyllable__EngString('ghksdbf')) # 환율
print(HGGetSyllable__EngString('fhksdbf')) # 롼율 --> 환율




"""
처리 결과:
================================
영문자 -> 한글 음절:
한국
란국
환율
롼율

"""

